import json

from config import client, MODEL
from tools import get_workshop_details, calculator


SYSTEM_PROMPT = """
You are a ReAct agent.

Solve the user's question by reasoning and using tools when necessary.

Available tools:

1. get_workshop_details
   Use this to retrieve workshop information.

2. calculator
   Use this to perform calculations.

After receiving tool results, continue reasoning until you have enough
information to provide the final answer.
"""


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_workshop_details",
            "description": "Get the fee, duration and placement relevance score of a workshop.",
            "parameters": {
                "type": "object",
                "properties": {
                    "workshop_name": {
                        "type": "string",
                        "description": "Name of the workshop"
                    }
                },
                "required": ["workshop_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to calculate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


def agent(question, max_steps=8):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    print("\n--- REACT TRACE ---\n")

    for step in range(max_steps):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        # Add assistant response to conversation
        messages.append(message)

        # If no tool is requested, this is the final answer
        if not message.tool_calls:

            print("FINAL ANSWER:")
            print(message.content)

            return message.content

        # Process each requested tool
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            try:
                arguments = json.loads(
                    tool_call.function.arguments
                )
            except json.JSONDecodeError:

                arguments = {}

            print(f"Action: {tool_name}")
            print(f"Arguments: {arguments}")

            # Tool 1
            if tool_name == "get_workshop_details":

                workshop_name = arguments.get(
                    "workshop_name"
                )

                result = get_workshop_details(
                    workshop_name
                )

            # Tool 2
            elif tool_name == "calculator":

                expression = arguments.get(
                    "expression"
                )

                result = calculator(expression)

            else:

                result = f"Unknown tool: {tool_name}"

            print(f"Observation: {result}")
            print()

            # Give the observation back to the model
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

    return "Maximum reasoning steps reached."