#import anthropic
#from openai import OpenAI
import google.generativeai
import os
from dotenv import load_dotenv
load_dotenv()
#anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
#openai_api_key=os.getenv("OPENAI_API_KEY")
gemini_api_key=os.getenv("GEMINI_API_KEY")
#client=anthropic.Anthropic(api_key=anthropic_api_key)
#client=OpenAI(api_key=openai_api_key)
client=genai.configure(api_key=gemini_api_key)

tools=[
    {
        "name":"get_weather",
        "description":"get current weather",
        # "input_schema":{
         "parameters":{
            "type":"object",
            "properties":{
                "city":{
                    "type":"string",
                    "description":"Name of the city"
                }
            },
            "required":["city"]
        }
    }
]
#def ask_claude(user_message):
def ask_gemini(user_message):
    #response=client.messages.create(
        
    #response=client.chat.completions.create(
    response=
        #model="claude-hiku-4-5-20251001"
        #model="gpt-4o-mini",
        
        max_tokens=1000,
        tools=tools,
        messages=[
            {
            "role":"user",
            "content":user_message
            }
        ]
    ) 
    return response
result=ask_claude("what is the weather in London?")
print(result)