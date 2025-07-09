from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
# Custom tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

#tool binding

from langchain_openai import ChatOpenAI

Model=ChatOpenAI()

llm_with_tool=Model.bind_tools([add])

#tool calling
llm_with_tool.invoke('Hi how are you')# for this message it wilm at as normal chatmodel
query = HumanMessage('can you add 3 with 1000')


messages = [query]#for chat history

result = llm_with_tool.invoke(messages)

messages.append(result)
#tool execution
tool_result = add.invoke(result.tool_calls[0])
messages.append(tool_result)
llm_with_tool.invoke(messages).content#output