import os
import subprocess
import sys
from agent_manager import generate_agents
from session_manager import save_agents_to_file, list_sessions


def create_new_agents():
    tasks = []
    print("Enter up to 10 tasks for agent creation. Type 'done' when finished.")
    while len(tasks) < 10:
        task = input(f"Task {len(tasks) + 1}: ")
        if task.lower() == 'done':
            break
        tasks.append(task)

    if tasks:
        print("\nGenerating agents...")
        agents = generate_agents(tasks)
        saved_file = save_agents_to_file(agents)
        print(f"\nAgents data saved to: {saved_file}")

        # Ask user to select session file for upload immediately after creation
        upload_agents(saved_file)
    else:
        print("No tasks provided. Exiting.")


def upload_agents(session_file=None):
    if not session_file:
        sessions = list_sessions()
        if not sessions:
            print("No saved sessions found. Exiting.")
            return

        print("Available sessions:")
        for i, session in enumerate(sessions, 1):
            print(f"{i}. {session}")

        session_choice = int(input("Enter the number of the session to upload from: ")) - 1
        if session_choice < 0 or session_choice >= len(sessions):
            print("Invalid choice. Exiting.")
            return

        session_file = f"sessions/{sessions[session_choice]}"

    print(f"Uploading agents from session: {session_file}")
    venv_python = os.path.join(".venv", "Scripts", "python.exe")  # Windows
    # venv_python = os.path.join(".venv", "bin", "python")  # macOS/Linux

    print(f"Using Python: {venv_python}")  # Debugging statement
    subprocess.run([venv_python, "agent_creation_automation.py", session_file])


if __name__ == "__main__":
    print("1. Create new agents")
    print("2. Load a previous session")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        create_new_agents()
    elif choice == '2':
        upload_agents()
    else:
        print("Invalid choice. Exiting.")
