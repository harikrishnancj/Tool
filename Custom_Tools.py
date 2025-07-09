#using @tool

from langchain_core.tools import tool

@tool
def mult(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

result = mult.invoke({"a": 3, "b": 5})
print(result)

#using structure tool and pydantic

from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool

class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")

def mult(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

multiply_tool = StructuredTool.from_function(
    name="Multiplication",
    args_schema=MultiplyInput,
    description="Multiply two numbers",
    func=mult
)

result = multiply_tool.invoke({'a': 3, 'b': 3})

# Outputs
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args_schema)
