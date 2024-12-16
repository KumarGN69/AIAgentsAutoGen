import os
from dotenv import load_dotenv
from openai import OpenAI
from pprint import pprint

load_dotenv() # load the environment functions
# Get the environment variables
API_KEY = os.getenv("API_KEY")
MODEL= os.getenv("MODEL_NAME")
URL=os.getenv("BASE_URL")

# Create an OpenAI client with the local model
client = OpenAI(
    base_url= URL,
    # required but ignored.Without this API call will fail
    api_key=API_KEY,
)
# Get the response from the chat
response = client.chat.completions.create(
    messages=[
        {
            "role":"user", # set the role to a user
            "content":"Tell me why sky is blue?" # the prompt to be used. Knowledge is limited to the timeline when training was done
        }
    ],
    model=MODEL,
    stream = False
)
pprint(response.choices[0].message.content)