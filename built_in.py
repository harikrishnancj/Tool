#Built-in Tool - DuckDuckGo Search
from langchain_community.tools import DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchResults()

results = search_tool.invoke('top news in india today')

#print(results)
'''
from ddgs import DDGS

with DDGS() as ddgs:
    results = ddgs.text("India news", max_results=5)
    for result in results:
        print("Title:", result.get("title"))
        print("Snippet:", result.get("body"))
        print("URL:", result.get("href"))
        print("-" * 50)
'''
#Built-in Tool - Shell Tool
from langchain_community.tools import ShellTool

s_tool=ShellTool()

res = s_tool.invoke('dir')
print(s_tool.invoke("echo Hello, world!"))
print(s_tool.invoke("whoami"))
print(s_tool.invoke("pwd"))  

print(res)