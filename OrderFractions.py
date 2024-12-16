import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL= os.getenv("MODEL_NAME")
URL=os.getenv("BASE_URL")

print(MODEL, URL, API_KEY)

model_config =[
    {
        "model":MODEL,
        "base_url":URL,
        "api_key":"NULL" # Always use NULL else local llm with Ollama with throw up connection error
    }
]
llm_model = {
        "temperature":0,
        "config_list":model_config
}

#Define the assistant
assistant = AssistantAgent(
    name="4th Grade Math teacher",
    system_message="You are math teacher",
    llm_config=llm_model,

)

#Define the user proxt agent

user_proxy = UserProxyAgent(
    name="4th Grade Math teacher proxy",
    human_input_mode ="NEVER",
    max_consecutive_auto_reply=2,
    code_execution_config= False,
    llm_config=llm_model,
    system_message="Reply TERMINATE if the response is complete else reply CONTINUE",
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
)

#initiate the user chat

chat_results= user_proxy.initiate_chat(
    assistant,
    message="You are an experienced math teacher for 4th grade math."
            "You are trying to teach the 4th grade students in comparing factions and subsequently ordering them from "
            "smallest to larget. "
            "To ensure students undertand the concept please detail out the approach to follow single logical steps with "
            "detailed explanation in English language using math terminology that a 4th grader can easily understand for each step"
            "Let us assume 4th graders have not been taught the concepts of Least Common Denominator( LCD) or Least Common Multiple (LCM)"
            "The output should be clear bulleted list of steps that you have used to solve the problem with detailed explanation"
            "for every step. Please use the fractions 1/2, 1/4, 3/4, 4/5, 2/7"

)

print(chat_results)