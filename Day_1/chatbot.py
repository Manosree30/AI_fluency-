from openai import OpenAI
from config import MODEL, GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

print("=== PLAIN CHATBOT ===")

question = input("User: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": """
You are a helpful general chatbot.
Answer the user's question naturally.
You do not have access to the user's private expense data.
Do not invent private expense information.
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nChatbot:")
print(response.choices[0].message.content)