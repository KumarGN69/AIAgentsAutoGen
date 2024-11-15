import os
import autogen
from autogen import AssistantAgent,UserProxyAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from dotenv import load_dotenv

##load the environment functions
load_dotenv()

##load the environment variables from the .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

#llm_config = { "config_list": [{ "model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY") }] }

##Define the model configuration details
config_list= [
    {
        "model": "llama3.2",
        "api_key":"NULL",
        "base_url": "http://localhost:11434/v1",
    
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
    name="RAG_user_proxy",
    human_input_mode ="NEVER",
    max_consecutive_auto_reply=2,
    code_execution_config= False,
    llm_config=llm_config,
    system_message="Reply TERMINATE if the response is complete else reply CONTINUE"
    )

task = """
        get today's TSLA stock price from https://www.google.com/finance/?hl=en
       """
# Start the chat
user_proxy.initiate_chat(
    assistant,
    message=task,
) 