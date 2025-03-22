from config import client, config


def create_agent(task_description):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": config["system_message"]},
            {"role": "user", "content": config["user_message_template"].format(task_description=task_description)}
        ]
    )
    response = completion.choices[0].message.content.strip()

    parts = response.split('\n')
    agent_info = {}
    current_key = None
    for part in parts:
        if part.startswith("Name:"):
            current_key = "name"
            agent_info[current_key] = part.replace("Name:", "").strip()
        elif part.startswith("Instructions:"):
            current_key = "instructions"
            agent_info[current_key] = ""
        elif part.startswith("Description:"):
            current_key = "description"
            agent_info[current_key] = part.replace("Description:", "").strip()
        elif current_key:
            agent_info[current_key] += part.strip() + "\n"

    for key in ["name", "instructions", "description"]:
        if key not in agent_info:
            agent_info[key] = "N/A"
        else:
            agent_info[key] = agent_info[key].strip()

    return agent_info


def generate_agents(task_list):
    return [create_agent(task) for task in task_list]
