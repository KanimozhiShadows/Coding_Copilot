from langchain.tools import Tool
from duckduckgo_search import DDGS

def web_search_tool(query: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query)
        return "\n".join([r['body'] for r in results[:3]])

WebSearch = Tool(
    name="WebSearch",
    func=web_search_tool,
    description="Search the web for up-to-date information"
)
