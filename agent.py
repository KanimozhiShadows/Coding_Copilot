from langchain_community.chat_models import ChatOllama
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import WebSearch
from memory import get_memory
import os

def create_agent():
    mode = os.getenv("LLM_MODE", "ollama")

    if mode == "openai":
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    else:
        llm = ChatOllama(model="llama3")  # You can use mistral, codellama, etc.

    memory = get_memory()
    tools = [WebSearch]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory
    )
    return agent
