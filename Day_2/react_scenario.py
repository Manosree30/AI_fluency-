from agent import agent
from config import banner


QUESTION = """
I am choosing between the AI Engineering and Full Stack Development
workshops.

Find the fee, duration and placement relevance score of both workshops.
Calculate the fee difference.

Then tell me which workshop has the higher placement relevance score
and explain the comparison using the information obtained from the tools.
"""


if __name__ == "__main__":

    banner("REACT AGENT - WORKSHOP SELECTION")

    print("SCENARIO:")
    print(QUESTION)

    print("\n--- REACT TRACE ---")

    answer = agent(
        QUESTION,
        max_steps=8
    )

    print("\n--- FINAL RESULT ---")
    print(answer)