# AI Chatbot CLI 🤖

A command-line AI chatbot built with Python and the **Google Gemini API**. It remembers the conversation, saves chat history between runs, and handles API errors without crashing.

This is part of my learning journey. For the Python fundamentals behind it, see [PythonLearning](https://github.com/mtmubeentahir/PythonLearning).

## ✨ Features

- **Real AI replies** from Google's Gemini models
- **Conversation memory**: the bot remembers what you said earlier in the chat
- **System prompt** that gives the bot its personality and rules
- **Saved history**: the chat is stored in `chat_history.json` and loaded on the next run
- **Error handling** for invalid keys, rate limits and connection problems
- **Token tracking** to see how much each conversation uses
- **Data validation** with Pydantic models

## 💬 Example

```
==== Bot (AI) - gemini-3.5-flash-lite ====
Type /help for commands.
You: My name is Ahmad
Bot is thinking...
Bot: Nice to meet you, Ahmad! How can I help you with Python today?
You: What is my name?
Bot is thinking...
Bot: Your name is Ahmad.
```

## ⌨️ Commands

| Command | What it does |
|---|---|
| `/help` | show all commands |
| `/clear` | start a fresh conversation |
| `/stats` | show message and token counts |
| `/model` | show which AI model is used |
| `/save` | save the chat to a custom file |
| `/quit` | save and exit |

## 🚀 Setup

**Requirements:** Python 3.10 or newer, and a free Gemini API key (no credit card needed).

1. **Clone the repository**
   ```bash
   git clone https://github.com/mtmubeentahir/ai-chatbot-cli.git
   cd ai-chatbot-cli
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

3. **Install the packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**
   - Get a free key at [Google AI Studio](https://aistudio.google.com).
   - Copy the example settings file:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and paste your key:
     ```
     GEMINAI_API_KEY=your-gemini-key-here
     BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
     MODEL=gemini-3.5-flash-lite
     ```

5. **Run the bot**
   ```bash
   python main.py
   ```

> ⚠️ Never share your `.env` file or commit it to GitHub. It is listed in `.gitignore`.

## 📁 Project structure

```
ai-chatbot-cli/
├── main.py            # chat loop and commands
├── ai_client.py       # sends requests to the AI, handles errors, counts tokens
├── conversation.py    # chat history, system prompt, save and load
├── models.py          # Pydantic Message model
├── config.py          # loads settings from .env
├── hello_ai.py        # minimal first API call
├── list_models.py     # lists the models available for your key
├── .env.example       # settings template (copy to .env)
└── requirements.txt   # Python packages
```

## ⚙️ How it works

1. You type a message, and `main.py` adds it to the conversation history.
2. `conversation.py` builds the request: the **system prompt** plus the **last 20 messages**.
3. `ai_client.py` sends it to Gemini's chat completions endpoint and reads the reply from `choices[0].message.content`.
4. The reply is added to the history, so the next request includes it too.

AI models have no memory of their own. The bot "remembers" because the whole recent conversation is sent with every request. That is also why token usage grows as the chat gets longer.

## 🧠 What I learned

- Calling an AI model API (endpoints, API keys, request and response JSON)
- Keeping secrets safe with `.env` files and `.gitignore`
- How chat memory works with roles: `system`, `user` and `assistant`
- Handling real-world API errors: authentication, rate limits and connection problems
- Validating data with Pydantic
- Organizing a project into modules, each with one job

## 🗺️ Next steps

- [ ] Automatic fallback to another model when one is rate-limited
- [ ] Streaming replies (show the answer word by word)
- [ ] A web interface with FastAPI
- [ ] Answering questions about my own documents (RAG)

## 👤 Author

**Mubeen Tahir** · [GitHub](https://github.com/mtmubeentahir)