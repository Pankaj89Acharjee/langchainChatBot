from fastmcp import FastMCP

mcp = FastMCP("arithmatic_server") #The name of the server is "weather"

#Defining Tools
@mcp.tool()
def add(num1: int, num2: int) -> int:
    """ Add two numbers given by user """
    return num1 + num2

@mcp.tool()
def sub(num1: int, num2: int) -> int:
    """Subtract two numbers when the second one is smaller than the first number"""
    if num2 > num1:
        return "The second number should be smaller than the first one, other wise you'll get the result in negative"
    
    return num1 - num2

@mcp.tool()
def mul(num1: int, num2: int) -> int:
    """multiply two numbers given by user """
    return num1 * num2

@mcp.tool()
def div(num1: int, num2: int) -> int:
    """Divide two numbers when the second number is not equal to zero"""
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

#Running the MCP server. Here __main__ means it will run only when the script is run directly. The "stdio" is used as a transport type which uses Standard Input/Output to communicate with the client. This transport communicates through standard input and output streams, making it perfect for command-line tools and desktop applications like Claude Desktop. 

if __name__ == "__main__":
    mcp.run(transport="stdio")