from agent import create_agent
from executor import try_execute
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    agent = create_agent()
    print("Coding Copilot is ready!")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break

        if user_input.startswith("execute:"):
            code = user_input[len("execute:"):].strip()
            output = try_execute(code)
            print(f"Executed Output:\n{output}")
        else:
            response = agent.invoke(user_input)
            print(f"Copilot: {response}")
