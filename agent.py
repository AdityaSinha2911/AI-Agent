import requests
import os

# saves history of conversation for further use
conversation_history = []

# creating limits, so that it changes within an environment
BASE_DIR = "project_files"
os.makedirs(BASE_DIR, exist_ok=True)

def create_file(filename, content):

    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File {filename} created inside {BASE_DIR}."

def create_folder(foldername):

    folderpath = os.path.join(BASE_DIR, foldername)

    os.makedirs(folderpath, exist_ok=True)

    return f"Folder {foldername} created inside {BASE_DIR}."



# I used ollama local LLM

def ask_llm(prompt):

    global conversation_history

    conversation_history.append(f"User: {prompt}")

    full_prompt = "\n".join(conversation_history)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:8b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    conversation_history.append(f"Agent: {answer}")

    # making it store only 20 recent conversation
    
    if len(conversation_history) > 20:
        conversation_history[:] = conversation_history[-20:]

    return answer

def get_time():
    import datetime
    return str(datetime.datetime.now())

def agent(user_input):

    decision_prompt = f"""
    You are an AI agent.

    You MUST respond in ONLY ONE of the following exact formats:

    1) USE_TIME_TOOL
    2) CREATE_FILE: filename.py
    3) CREATE_FOLDER: foldername
    4) USE_LLM

    Do NOT explain.
    Do NOT add extra text.
    Return only one line.

    User input: {user_input}
    """

    decision = ask_llm(decision_prompt).strip()

    if decision == "USE_TIME_TOOL":
        return get_time()

    elif decision.startswith("CREATE_FILE:"):

        filename = decision.replace("CREATE_FILE:", "").strip()

        # Safety check, so file is not made on some dangerous path
        if not filename.endswith(".py"):
            return "Only .py files allowed."

        if any(x in filename for x in ["..", "/", "\\"]):
            return "Invalid filename."

        code_prompt = f"""
            Generate complete working Python code for {filename}.
            Return ONLY the raw code.
            Do NOT explain anything."""
        
        code = ask_llm(code_prompt)

        # issue resolved for ''' before code generation

        if "```" in code:
            code = code.replace("```python", "")
            code = code.replace("```", "")
            code = code.strip()

        return create_file(filename, code)

    elif decision.startswith("CREATE_FOLDER:"):

        foldername = decision.replace("CREATE_FOLDER:", "").strip()

        if any(x in foldername for x in ["..", "/", "\\"]):
            return "Invalid folder name."

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
