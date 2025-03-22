# AI Agent Generator

This project is an AI-powered tool that generates specialized AI agents based on user-defined tasks. It uses OpenAI's GPT-4 model to create detailed instructions and descriptions for each agent.

## Features

- Generate AI agents based on user-provided tasks
- Save generated agents to JSON files for future reference
- Load previously generated agent sessions
- RESTful API endpoint for agent generation

## Project Structure

- `main.py`: The main script that runs the program
- `agent_manager.py`: Contains functions related to agent creation and management
- `session_manager.py`: Handles saving and loading sessions
- `api.py`: Contains the Flask app and API-related code
- `config.py`: Loads and manages configuration
- `config.json`: Contains configuration settings
- `.env`: Stores environment variables (like API keys)

## Setup

1. Clone the repository:
   git clone https://github.com/your-username/ai_agent_building_team.git
   cd ai-agent-generator

2. Install the required dependencies:

   pip install -r requirements.txt

3. Set up your OpenAI API key:
   - Create a `.env` file in the `.venv` directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

4. Configure the `config.json` file with your desired system message and user message template.

## Usage

Run the main script:
python main.py



Follow the prompts to either create new agents or load a previous session.

### Creating New Agents

1. Choose option 1 when prompted
2. Enter up to 10 tasks for agent creation
3. The program will generate agents based on your tasks
4. Generated agents will be displayed and saved to a JSON file in the `sessions` directory

### Loading a Previous Session

1. Choose option 2 when prompted
2. Select a session from the list of available sessions
3. The program will load and display the agents from the selected session

## API Usage

To use the API endpoint for agent generation:

1. Uncomment the `app.run(debug=True, use_reloader=False)` line in `main.py`
2. Run the Flask app
3. Send a POST request to `http://localhost:5000/generate_agents` with a JSON body containing a list of tasks:
   

### json

{
     "tasks": ["Design a logo", "Write a blog post"]
   }

### Contributing
Contributions to improve the AI Agent Generator are welcome. Please feel free to submit a Pull Request.


### License

This project is licensed under the MIT License - see the LICENSE file for details.



This README provides an overview of your project, explains its structure, and gives instructions on how to set up and use the AI Agent Generator. It also includes information about the API usage and how to contribute to the project.
You may want to adjust some details, such as the GitHub repository URL, based on your actual setup. Also, consider adding a license file (like MIT License) if you haven't already, and update the license section accordingly.