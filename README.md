# Coding Assistant 
---

## 🧠 Coding Assistant

Coding Assistant is an agentic AI assistant that helps you with coding tasks, powered by OpenAI’s GPT model and enhanced with memory and real-time web search capabilities. It offers both a **command-line interface (CLI)** and a **web interface (via Streamlit)** for a user-friendly developer experience.

---

### 🚀 Features

* 💬 Chat with an AI agent backed by GPT-3.5-turbo.
* 🧠 Retains conversation context using memory buffers.
* 🌐 Real-time web search using DuckDuckGo API.
* 📚 Persistent vector store integration (ChromaDB-ready).
* 🌐 Simple Streamlit web UI for accessible usage.
* 🔐 Securely loads API keys from `.env`.

---

### 🧩 Tech Stack

* **Python**
* **LangChain**
* **OpenAI API**
* **Streamlit**
* **DuckDuckGo Search (DDGS)**
* **ChromaDB**
* **dotenv**

---

### 📁 Project Structure

```bash
├── agent.py             # Creates the LangChain agent with tools and memory
├── tools.py             # Custom web search tool using DuckDuckGo
├── memory.py            # Setup for memory and vector store
├── main.py              # CLI entry point to run the copilot
├── ui_streamlit.py      # Web UI using Streamlit
├── .env                 # Stores API keys (do not expose publicly)
├── requirements.txt     # Python dependencies
├── api.txt              # Instructions for setting env vars (alternative)
```

---

### ⚙️ Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <your-repo-url>
   cd coding-copilot
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**

   Create a `.env` file with the following content (already provided):

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

   Optionally, include `SERPAPI_API_KEY` or configure the system environment using:

   ```bash
   $env:OPENAI_API_KEY="your-api-key"
   ```

4. **Run the CLI Version**

   ```bash
   python main.py
   ```

5. **Run the Streamlit UI**

   ```bash
   streamlit run ui_streamlit.py
   ```

---

### 🔄 Process Flow

Here’s a simplified step-by-step process:

```
User Input
   │
   ▼
[ Streamlit UI ] OR [ CLI Interface ]
   │
   ▼
create_agent()  ← agent.py
   │
   ├── Loads LLM (ChatOpenAI)
   ├── Adds memory (ConversationBufferMemory)
   └── Adds tools (WebSearch via DuckDuckGo)
   │
   ▼
Agent handles input using:
   - LLM for reasoning
   - Tool invocation (search)
   - Memory for context
   │
   ▼
Agent generates response
   │
   ▼
Output to user
```






