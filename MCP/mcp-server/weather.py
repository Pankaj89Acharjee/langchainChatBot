from fastmcp import FastMCP

mcp = FastMCP("weather") #The name of the server is "weather"

#Defining Tools
@mcp.tool()
def forecast_weather(place: str) -> str:
    reply_msg = 'The weather is windy today at {place}'
    return reply_msg

#Running the MCP server. Here __main__ means it will run only when the script is run directly. The "streamable-http" is used as a transport type which uses Server-Sent-Events to communicate with the client.  
if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port= 9000)