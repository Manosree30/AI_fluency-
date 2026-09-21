from openai import OpenAI
from config import MODEL, GROQ_API_KEY
from tools import calculate_category_total, get_budget


client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def agent(user_question):

    print("\n=== AI AGENT ===")

    # --------------------------------
    # STEP 1: Receive user request
    # --------------------------------
    print("1. Agent received the request")

    question = user_question.lower()

    # --------------------------------
    # STEP 2: Decide which tool to use
    # --------------------------------
    if "food" in question:
        tool_name = "calculate_category_total"
        category = "Food"

    elif "travel" in question:
        tool_name = "calculate_category_total"
        category = "Travel"

    elif "shopping" in question:
        tool_name = "calculate_category_total"
        category = "Shopping"

    elif "budget" in question:
        tool_name = "get_budget"
        category = None

    else:
        print("\n2. Agent could not find a suitable tool.")
        print("I don't know how to handle this request.")
        return

    print("\n2. Agent selected tool:")

    if category:
        print(f"{tool_name}('{category}')")
    else:
        print(f"{tool_name}()")

    # --------------------------------
    # STEP 3: Use the selected tool
    # --------------------------------
    if tool_name == "calculate_category_total":
        result = calculate_category_total(category)

    elif tool_name == "get_budget":
        result = get_budget()

    print("\n3. Tool result:")
    print("₹" + str(result))

    # --------------------------------
    # STEP 4: Agent observes result
    # --------------------------------
    print("\n4. Agent observed the tool result")

    # --------------------------------
    # STEP 5: LLM generates final answer
    # --------------------------------
    final_response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are a helpful student expense assistant.
Answer the user's question using only the tool result.
Do not invent numbers.
Give a complete natural-language answer.
"""
            },
            {
                "role": "user",
                "content": f"""
User question:
{user_question}

Tool result:
₹{result}

Give a complete natural-language answer to the user's question.
For example:
"You spent ₹470 on food."

Do not answer with only the number.
"""
            }
        ]
    )

    print("\n5. Agent final answer:")
    print(final_response.choices[0].message.content)


# --------------------------------
# MAIN PROGRAM
# --------------------------------

question = input("User: ")

agent(question)