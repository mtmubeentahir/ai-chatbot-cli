from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Say hello and tell me one fun fact about python."}
    ]
)

print("Reply: ", response.choices[0].message.content)
print("Model used: ", response.model)

if response.usage:
    print("Token:", response.usage.prompt_tokens, "in, ", response.usage.completion_tokens, "out")
    
