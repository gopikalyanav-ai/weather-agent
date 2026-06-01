
from google import genai
import os
from dotenv import load_dotenv
from weather_tool import get_weather
load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=gemini_api_key)
# model=genai.GenerativeModel(

#        model_name="gemini-1.5-flash",
#        tools=[get_weather]
#)
def ask_llm(user_message):
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_message,
        config={
            "tools":[get_weather],
            "automatic_function_calling":{"disable":False}
        }
    )    
    return response
# result=ask_llm("what is the weather in chirala")
# print(result.text)