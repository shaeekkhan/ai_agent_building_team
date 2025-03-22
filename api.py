from flask import Flask, request, jsonify
from agent_manager import generate_agents

app = Flask(__name__)


@app.route("/generate_agents", methods=["POST"])
def generate_agents_api():
    data = request.json
    tasks = data.get("tasks", [])
    agents = generate_agents(tasks)
    return jsonify(agents)
