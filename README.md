# AI Agent – Local Tool-Using Coding Assistant

## Overview

AI Agent is a locally hosted, tool-using coding assistant built using Python and Ollama.  
It integrates a local Large Language Model (LLM) with controlled execution tools to perform real development tasks such as:

- Creating Python files
- Creating folders
- Generating complete working code
- Providing concise responses
- Fetching the current system time

The agent runs entirely on your local machine and does not depend on cloud-based AI services once the model is installed.

---

## Model Information

- LLM Runtime: Ollama
- Model Used: llama3:8b
- Execution Mode: Local (offline after download)

The Llama 3 (8B parameter) model provides a good balance between reasoning capability and performance on consumer systems.

Recommended System:
- 16GB RAM
- Python 3.9 or higher

---

## Features

- Local LLM-powered decision engine
- Tool-based action execution
- Sandboxed file creation
- Automatic Markdown cleanup from generated code
- Conversation memory support
- Infinite interactive CLI loop
- Strict decision format for predictable behavior
- No external API dependency after setup

---

## Architecture

The system consists of:

1. Decision Layer  
   The LLM determines which action to perform using a strict response format.

2. Tool Layer  
   - create_file() → Creates Python files inside a safe directory  
   - create_folder() → Creates folders inside a safe directory  
   - get_time() → Returns system time  

3. Sandbox Directory  
   All generated files are stored inside:
   project_files/

This prevents access to unsafe system paths.

---

## Installation Requirements

### 1. Install Python

Python 3.9 or higher is recommended.

### 2. Install Required Python Package

Install dependency:

pip install requests

Only one external Python package is required:
- requests (used to communicate with Ollama API)

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

After installation, download the required model:

ollama pull llama3:8b

This downloads the Llama 3 (8B) model locally.

---

## Start Ollama

Ensure Ollama is running before starting the agent.

If not running automatically:

ollama serve

You can verify by opening:

http://localhost:11434

---

## How to Run the Project

1. Clone the repository:

git clone <your-repository-url>
cd <repository-name>

2. (Optional but Recommended) Create a virtual environment:

python -m venv .venv

Activate on Windows:

.venv\Scripts\activate

3. Install dependency:

pip install requests

4. Run the agent:

python agent.py

---

## How to Use

After running, the CLI will display:

You:

You can type commands such as:

Create a file called calculator.py

Create a folder called utils

Create a file called password_generator.py

What is the current time?

To exit:

bye

All generated files will be stored inside:

project_files/

---

## Project Structure

AI_AGENT/
│
├── agent.py
├── project_files/
│   ├── generated Python files
│   └── generated folders
└── README.md

---

## Security Measures

- Only .py files are allowed for creation
- Path traversal prevention implemented
- Sandboxed file generation directory
- No system-level command execution
- Local execution only

---

## Future Improvements

- JSON-based structured action parsing
- Multi-file project generation
- File reading and modification capability
- Controlled code execution
- GUI interface
- Logging and monitoring system

---

## Purpose

This project demonstrates:

- Local LLM integration
- Tool-using AI agent design
- Safe execution boundaries
- Structured decision-based control flow
- Practical AI system architecture

This project is intended for educational, experimental, and development purposes.
