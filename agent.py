import requests
import os

def create_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File {filename} created successfully."

def create_folder(foldername):
    os.makedirs(foldername, exist_ok=True)
    return f"Folder {foldername} created."



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

    Try to answer in less words, don't explain too much, until asked.

    If the user wants to create a file, respond like:
    CREATE_FILE: filename.py

    If the user wants to create a folder, respond like:
    CREATE_FOLDER: foldername

    If the user is asking for current time, respond with: USE_TIME_TOOL
    Otherwise respond with: USE_LLM

    User input: {user_input}
    """

    decision = ask_llm(decision_prompt)

    if "USE_TIME_TOOL" in decision:

        return get_time()
    
    elif "CREATE_FILE:" in decision:

        filename = decision.split("CREATE_FILE:")[1].strip()
        code = ask_llm(f"Generate full Python code for {filename}")
        return create_file(filename, code)
    
    elif "CREATE_FOLDER:" in decision:

        foldername = decision.split("CREATE_FOLDER:")[1].strip()
        return create_folder(foldername)
    
    else:
        return ask_llm(user_input)


# run's an infinite loop of conversation
while True:
    user = input("You: ")
    if user.lower()=="bye":
        print("Agent: Good-Bye")
        break
    print("Agent:", agent(user))
