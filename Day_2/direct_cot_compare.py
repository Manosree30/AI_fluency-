from config import client, MODEL, banner


WORKSHOP_DATA = """
Workshop 1: AI Engineering
Fee: ₹2500
Duration: 3 days
Placement relevance score: 9/10

Workshop 2: Full Stack Development
Fee: ₹1800
Duration: 2 days
Placement relevance score: 8/10
"""


QUESTION = """
I am choosing between two technical workshops.

Using the information below:

1. Calculate the fee difference.
2. Find which workshop has the higher placement relevance score.
3. Explain the difference clearly.

""" + WORKSHOP_DATA


def direct_prompt():
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


def cot_prompt():
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": QUESTION + """

Solve this step by step.

First identify the important values.
Then calculate the fee difference.
Then compare the placement relevance scores.
Finally give the answer with a short explanation.
"""
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    banner("DIRECT PROMPTING VS CHAIN-OF-THOUGHT")

    print("QUESTION:")
    print(QUESTION)

    print("\n" + "=" * 70)
    print("DIRECT PROMPTING OUTPUT")
    print("=" * 70)

    direct_answer = direct_prompt()
    print(direct_answer)

    print("\n" + "=" * 70)
    print("CHAIN-OF-THOUGHT PROMPTING OUTPUT")
    print("=" * 70)

    cot_answer = cot_prompt()
    print(cot_answer)