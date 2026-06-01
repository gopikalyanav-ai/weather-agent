from weather_agent import run_agent
print("Agent is ready to run")
print("Type quit to stop Agent")
while True:
    user_input=input("ask about weather in the place which you want: ")
    if user_input=="quit":
        print("THANK YOU")
        break
    run_agent(user_input)
