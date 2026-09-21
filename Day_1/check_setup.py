from openai import OpenAI
from config import PROVIDER, MODEL, GROQ_API_KEY

print("=== SETUP CHECK ===")

print("Provider :", PROVIDER)
print("Model    :", MODEL)

if not GROQ_API_KEY:
    print("ERROR: GROQ_API_KEY not found in .env")
    exit()

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: SETUP OK"
            }
        ]
    )

    print("Model replied :", response.choices[0].message.content)

except Exception as e:
    print("ERROR:", e)