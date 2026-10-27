from openai import OpenAI

from config import API_KEY, BASE_URL

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

SKIP = ["audio", "live", "tts", "image", "robotics", "translate", "embedding", "lyria"]

for model in client.models.list():
    name = model.id.replace("models/", "")
    if "flash" in name and not any(word in name for word in SKIP):
        print(name)