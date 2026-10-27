from ai_client import AIClient
from config import MODEL
from conversation import Conversation

HISTORY_FILE = "chat_history.json"

COMMANDS = {
    "/help": "show this list",
    "/clear": "start a fresh conversation",
    "/stats": "show message and token counts",
    "/model": "show which AI model is used",
    "/save": "save the chat to a custom file",
    "/quit": "save and exit",
}

chat = Conversation()
chat.load(HISTORY_FILE)
ai = AIClient()

print(f"==== Bot (AI) - {MODEL} ====")
if chat.messages:
    print(f"Loaded {len(chat.messages)} previous messages.")
print("Type /help for commands.")

while True:
    text = input("You: ").strip()
    if not text:
        continue

    if text == "/quit":
        chat.save(HISTORY_FILE)
        print("Chat saved. Goodbye!")
        break
    
    if text == "/help":
        for k, v in COMMANDS.items():
            print(f"{k}     {v}")
        continue
    
    if text == "/clear":
        chat.messages = []
        chat.save(HISTORY_FILE)
        print("History cleared.")
        continue

    if text == "/stats":
        print(f"{len(chat.messages)} messages are in this chat")
        print("Token sent: ", ai.tokens_in)
        print("Token received: ", ai.tokens_out)
        continue
    
    if text == "/model":
        print(f"Model: {MODEL}")
        continue
    
    if text == "/save":
        file_name = input("Enter filename: ").strip()
        if not file_name:
            print("No filename given, Not saved.")
            continue
        chat.save(f"{file_name}.json")
        print(f"Saved to {file_name}.json")
        continue
    
    if text.startswith("/"):
        print("Unknown command. Type /help.")
        continue    
        
    chat.add("user", text)
    print("Bot is thinking...")
    reply = ai.ask(chat.to_api())

    if reply.startswith("[Error]"):
        chat.messages.pop()        # remove the failed user message
    else:
        chat.add("assistant", reply)

    print(f"Bot: {reply}")