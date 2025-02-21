from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain_core.tools import Tool
from ..llms.llmSelector import getLLMFromModelName
from ..tools.getLatestBlockTool import getLatestBlockTool
from ..tools.getWalletBalance import getWalletBalance
from ..tools.currentTime import get_current_time
from ..tools.searchWikipedia import search_wikipedia

# Load environment variables from .env file

def get_agent_executor(model:str):   
    # List of tools available to the agent
    try:
        tools = [
            Tool(
                name="Time",  # Name of the tool
                func=get_current_time,  # Function that the tool will execute
                # Description of the tool
                description="Useful for when you need to know the current time",
            ),
            Tool(
                name="Wikipedia",
                func=search_wikipedia,
                description="Useful for when you need to know information about a topic.",
            ),
            Tool(
                name="Get Current Block",
                func=getLatestBlockTool,
                description="Useful for when you need to know the current block of a network.It supports 'ethereum','polygon','arbitrum','zksync','optimism','fantom','mantle','base' networks as input",
            ),
                Tool(
                name="WalletBalance",
                func=getWalletBalance,
                description="Useful for when you need to know the balance of a address on a specific network.It takes in network as input as the first parameter and the second parameter is the wallet address provided. If no network is provided , use 'ethereum' as the first input",
            ),
            
        ]

        # Pull the prompt template from the hub
        # ReAct = Reason and Action
        # https://smith.langchain.com/hub/hwchase17/react
        prompt = hub.pull("hwchase17/react")

        # Initialize a ChatOpenAI model
        llm = getLLMFromModelName(model)

        # Create the ReAct agent using the create_react_agent function
        agent = create_react_agent(
            llm=llm,
            tools=tools,
            prompt=prompt,
            stop_sequence=True,
        )

        # Create an agent executor from the agent and tools
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=tools,
            verbose=True,
        )
        return agent_executor
    except:
        print(f"Error occured inside get_agent_executor")
        return None

# Run the agent with a test query
# response = agent_executor.invoke({"input": "What time is it?"})

# # Print the response from the agent
# print("response:", response)