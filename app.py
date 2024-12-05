import os
import autogen
from autogen import AssistantAgent,UserProxyAgent, register_function
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from dotenv import load_dotenv
from tool import get_stocknews
from pprint import pprint

##load the environment functions
load_dotenv()

##load the environment variables from the .env file
API_KEY = os.getenv("API_KEY")
URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

##Define the model configuration details
config_list= [
    {
        "model": MODEL_NAME,
        "api_key":"NULL",
        "base_url": URL,
    
    }
]

## Define the llm model with the requsite configuations
llm_config = {
            "config_list":config_list,
            "temperature":0
}

##Define assisstant agent
assistant = AssistantAgent(
            name= "assistant", 
            llm_config=llm_config,
            
            system_message="You are a stock trader"

    )

##Define User Proxy Agent
user_proxy = UserProxyAgent(
    name="Stock_News_user_proxy",
    human_input_mode ="NEVER",
    max_consecutive_auto_reply=2,
    code_execution_config= False,
    llm_config=llm_config,
    system_message="Reply TERMINATE if the response is complete else reply CONTINUE",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    )

# Register the function to be used by the two agents.
register_function(
    get_stocknews,
    caller=assistant,  # The assistant agent can suggest calls to the calculator.
    executor=user_proxy,  # The user proxy agent can execute the calculator calls.
    name="get_stocknews",  # By default, the function name is used as the tool name.
    description="A news reporter",  # A description of the tool.
)

# Start the chat
chat_results = user_proxy.initiate_chat(
    assistant,
    message=" What are the important news items impacting the stock price of WMT in last 1mo?"
)

#print the results
# pprint(chat_results.chat_history)