import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-120b"


questions = [
    "What is an AI agent?",
    "If I buy 5 notebooks at ₹60 each, what is the total cost?",
    "What is the difference between a tool and a tool call?"
]


for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:")
    print(question)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    print("\nLLM ANSWER:")
    print(answer)