import requests


# I used ollama local LLM

def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:8b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def get_time():
    import datetime
    return str(datetime.datetime.now())

def agent(user_input):

    decision_prompt = f"""
    You are an AI agent.
    If the user is asking for current time, respond with: USE_TIME_TOOL
    Otherwise respond with: USE_LLM

    User input: {user_input}
    """

    decision = ask_llm(decision_prompt)

    if "USE_TIME_TOOL" in decision:
        return get_time()
    else:
        return ask_llm(user_input)


# run's an infinite loop of conversation
while True:
    user = input("You: ")
    if user.lower()=="bye":
        print("Agent: Good-Bye")
        break
    print("Agent:", agent(user))
