import os
import json

from openai import OpenAI
from dotenv import load_dotenv

from tool import calculate_expense


load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


MODEL = "openai/gpt-oss-120b"


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_expense",
            "description": "Calculate the total expense when the price of one item and the quantity are given.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "Price of one item in Indian Rupees"
                    },
                    "quantity": {
                        "type": "integer",
                        "description": "Number of items"
                    }
                },
                "required": ["amount", "quantity"]
            }
        }
    }
]


questions = [
    "What is an AI agent?",
    "If I buy 5 notebooks at ₹60 each, what is the total cost?",
    "What is the difference between a tool and a tool call?"
]


for question in questions:

    print("\n" + "=" * 70)

    print("QUESTION:")
    print(question)

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]


    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )


    assistant_message = response.choices[0].message


    # Check whether the model requested a tool
    if assistant_message.tool_calls:

        print("\nTOOL CALL:")

        messages.append(assistant_message)


        for tool_call in assistant_message.tool_calls:

            function_name = tool_call.function.name

            arguments = json.loads(tool_call.function.arguments)

            print("Tool name:", function_name)
            print("Arguments:", arguments)


            if function_name == "calculate_expense":

                result = calculate_expense(
                    arguments["amount"],
                    arguments["quantity"]
                )

            else:

                result = "Unknown tool"


            print("TOOL RESULT:")
            print(result)


            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )


        # Ask the LLM to produce the final answer
        final_response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools
        )


        final_answer = final_response.choices[0].message.content

        print("\nFINAL ANSWER:")
        print(final_answer)


    else:

        print("\nNO TOOL CALL")

        print("\nFINAL ANSWER:")
        print(assistant_message.content)