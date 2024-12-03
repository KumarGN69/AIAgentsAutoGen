import os
import autogen
from autogen import AssistantAgent,UserProxyAgent, register_function
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from dotenv import load_dotenv
from tool import get_news
from pprint import pprint

##load the environment functions
load_dotenv()

##load the environment variables from the .env file
API_KEY = os.getenv("API_KEY")
URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

#llm_config = { "config_list": [{ "model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY") }] }

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
            # "api_rate_limit":60.0,
            # "seed":42,
            "config_list":config_list,
            "temperature":0
}

##Define assisstant agent
assistant = AssistantAgent(
            name= "assistant", 
            llm_config=llm_config,
            
            system_message="You stock trader"

    )


user_proxy = UserProxyAgent(
    name="Stock_News_user_proxy",
    human_input_mode ="NEVER",
    max_consecutive_auto_reply=2,
    code_execution_config= False,
    llm_config=llm_config,
    system_message="Reply TERMINATE if the response is complete else reply CONTINUE"
    )

task = """
        get_news("TSLA",period="5d")
       """
# Start the chat
# Register the calculator function to the two agents.
register_function(
    get_news,
    caller=assistant,  # The assistant agent can suggest calls to the calculator.
    executor=user_proxy,  # The user proxy agent can execute the calculator calls.
    name="get_news",  # By default, the function name is used as the tool name.
    description="A news reporter",  # A description of the tool.
)

chat_results = user_proxy.initiate_chat(
    assistant,
    message=" What is the latest news about TSLA in last 5d?"
)

pprint(chat_results.chat_history)