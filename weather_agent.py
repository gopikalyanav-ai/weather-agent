from weather_llm_connection_gemini import ask_llm
def run_agent(user_message):
    print(f"user: {user_message}")
    
    response=ask_llm(user_message)
    print(f"agent: {response.text}")
    return response