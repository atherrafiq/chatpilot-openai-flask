# AI Chatbot Powered by Flask & OpenAI

Welcome to a smart chatbot experience, built with Flask and supercharged by OpenAI's API. This project brings conversational AI to life using intuitive design and powerful NLP models. Whether you're exploring customer service automation, personal assistants, or just experimenting with generative AI, this chatbot is built to get you started quickly and efficiently.

![Chatbot Interface](screenshot.png)

## ⚙️ Requirements

Before running the app, make sure you have the following:

- Python 3.9+
- Flask framework
- Langchain
- OpenAI API key
- `openai` Python SDK

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/atherrafiq/chatpilot-openai-flask
cd your-chatbot-repo
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

- Open "Edit the system environment variables"
- Go to **Environment Variables**
- Add a new **User Variable**:  
  `OPENAI_API_KEY = your_openai_secret_key`

### 4. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:{port}/` in your browser to interact with the chatbot.

## 💬 How It Works

Type your messages into the chat interface. The bot uses OpenAI's models to understand your input and respond in real-time — no predefined scripts, just adaptive AI-driven conversations.

## 🚢 Deploying to Production

To move beyond local testing, deploy this app using a production-grade WSGI server like **Gunicorn** or **uWSGI**. For best practices, refer to the official Flask deployment guide.

## 📄 License

This project is released under the [MIT License](LICENSE). Feel free to modify and reuse it.

## 🤝 Contributions

Got ideas or found an issue? Open a pull request or submit a GitHub issue — collaboration is always welcome!
