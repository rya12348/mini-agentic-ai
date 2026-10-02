import os

from langchain.agents import initialize_agent, Tool, AgentType

from langchain_openai import ChatOpenAI



# This is a simplified agentic framework.

# To run this, you will need an OPENAI_API_KEY environment variable.



def get_weather(location):

    \"\"\"Simulated tool to get weather.\"\"\"

    return f\"The weather in {location} is sunny and 75 degrees.\"



def get_stock_price(symbol):

    \"\"\"Simulated tool to get stock prices.\"\"\"

    return f\"The stock price of {symbol} is $150.00.\"



def main():

    # Initialize the LLM

    llm = ChatOpenAI(model=\"gpt-4\", temperature=0)



    # Define the tools the agent can use

    tools = [

        Tool(

            name=\"WeatherTool\",

            func=get_weather,

            description=\"Useful for when you need to ask about the weather.\"

        ),

        Tool(

            name=\"StockTool\",

            func=get_stock_price,

            description=\"Useful for when you need to ask about stock prices.\"

        ),

    ]



    # Initialize the agent

    agent = initialize_agent(

        tools, 

        llm, 

        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 

        verbose=True

    )



    # Example request

    query = \"What is the weather in New York and what is the price of AAPL stock?\"

    print(f\"Query: {query}\")

    agent.run(query)



if __name__ == \"__main__\":

    main()

