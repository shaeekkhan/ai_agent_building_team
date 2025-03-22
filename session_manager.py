import os
import json
from datetime import datetime


def save_agents_to_file(agents):
    if not os.path.exists('sessions'):
        os.makedirs('sessions')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sessions/agents_session_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(agents, f, indent=4)
    return filename


def load_agents_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def list_sessions():
    return sorted([f for f in os.listdir('sessions') if f.startswith('agents_session_') and f.endswith('.json')])
