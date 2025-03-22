from agent_manager import generate_agents
from session_manager import save_agents_to_file, load_agents_from_file, list_sessions
from api import app


def print_agents(agents):
    for i, agent in enumerate(agents, 1):
        print(f"\nAgent {i}:")
        print(f"Name: {agent.get('name', 'N/A')}")
        print(f"Instructions: {agent.get('instructions', 'N/A')}")
        print(f"Description: {agent.get('description', 'N/A')}")


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
        print("\nGenerated Agents:")
        print_agents(agents)
        saved_file = save_agents_to_file(agents)
        print(f"\nAgents data saved to: {saved_file}")
    else:
        print("No tasks provided. Exiting.")


def load_previous_session():
    sessions = list_sessions()
    if not sessions:
        print("No saved sessions found.")
        return

    print("Available sessions:")
    for i, session in enumerate(sessions, 1):
        print(f"{i}. {session}")
    session_choice = int(input("Enter the number of the session to load: ")) - 1
    if 0 <= session_choice < len(sessions):
        loaded_agents = load_agents_from_file(f"sessions/{sessions[session_choice]}")
        print("\nLoaded Agents:")
        print_agents(loaded_agents)
    else:
        print("Invalid session number.")


if __name__ == "__main__":
    print("1. Create new agents")
    print("2. Load a previous session")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        create_new_agents()
    elif choice == '2':
        load_previous_session()
    else:
        print("Invalid choice. Exiting.")

    # Uncomment the following line to run the Flask app
    # app.run(debug=True, use_reloader=False)
