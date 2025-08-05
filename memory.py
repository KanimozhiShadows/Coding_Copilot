from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory

def get_memory():
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def get_vectorstore():
    embeddings = OpenAIEmbeddings()
    return Chroma(collection_name="code_copilot", embedding_function=embeddings)
