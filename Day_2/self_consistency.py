from collections import Counter
from config import client, MODEL, banner


QUESTION = """
A student has ₹5000.

They spend ₹1200 on a workshop and ₹800 on books.
Then they receive a scholarship of ₹1500.

How much money do they have now?

Solve the problem carefully and give only the final amount in the format:

ANSWER: ₹XXXX
"""


def get_answer(temperature=0.8):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    banner("SELF-CONSISTENCY EXPERIMENT")

    print("QUESTION:")
    print(QUESTION)

    answers = []

    print("\nRunning 5 reasoning attempts...\n")

    for i in range(5):

        result = get_answer(temperature=0)

        print("=" * 70)
        print(f"RUN {i + 1}")
        print("=" * 70)
        print(result)

        answers.append(result)

    print("\n" + "=" * 70)
    print("COLLECTED ANSWERS")
    print("=" * 70)

    for i, answer in enumerate(answers, 1):
        print(f"Run {i}: {answer}")

    print("\n" + "=" * 70)
    print("MAJORITY ANSWER")
    print("=" * 70)

    # Extract the final ANSWER line
    extracted = []

    for answer in answers:

        for line in answer.splitlines():

            if line.strip().upper().startswith("ANSWER:"):
                value = line.split(":", 1)[1].strip()
                extracted.append(value)

    if extracted:

        counts = Counter(extracted)
        majority = counts.most_common(1)[0]

        print(f"Majority answer: {majority[0]}")
        print(f"Occurrences: {majority[1]} / {len(extracted)}")

    else:

        print("Could not automatically extract the ANSWER field.")