import asyncio
import os
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

async def main():
    client = MultiServerMCPClient(
    #Passing the servers with their names 
        {
            # First one was Stdio server, so command is given instead of URL
            "mathserver": {
                "transport": "stdio",
                "command": "python",
                "args": ["../mcp-server/mathserver.py"] #Direct path to the server file (Absolute path)
            },

            #Second server was http, so used URL
            "weatherserver": {
                "transport": "streamable-http",
                "url": "http://localhost:9000"
            }
        }
    )


    tools = await client.get_tools() #Means I am getting the above two tools inside the client variable viz., "mathserver" tool and "weatherserver" tool
    model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
    # agent = create_react_agent(model, tools)
    agent = create_agent(model, tools)


    # Invoke and get response
    response = await agent.ainvoke({
    "messages": [
        {
            "role": "user", 
            "content": "Hello"
        }
    ]
    })
    print(response)


asyncio.run(main())