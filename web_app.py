from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import json
import sys
import subprocess
from agent_manager import generate_agents
from session_manager import save_agents_to_file

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/create", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("create_agents.html", {"request": request})


@app.post("/create_agents/", response_class=HTMLResponse)
async def create_agents(request: Request, tasks: str = Form(...)):
    task_list = [t.strip() for t in tasks.split("\n") if t.strip()]
    agents = generate_agents(task_list)
    session_file = save_agents_to_file(agents)
    session_filename = os.path.basename(session_file)
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "agents": agents,
            "session_filename": session_filename
        }
    )


@app.get("/load_session/", response_class=HTMLResponse)
def load_session(request: Request):
    session_files = [
        f for f in os.listdir("sessions")
        if f.startswith("agents_session_") and f.endswith(".json")
    ]
    session_files.sort(reverse=True)
    return templates.TemplateResponse(
        "sessions.html",
        {
            "request": request,
            "sessions": session_files
        }
    )


@app.get("/view_session/{session_filename}", response_class=HTMLResponse)
def view_session(request: Request, session_filename: str):
    with open(f"sessions/{session_filename}", "r", encoding="utf-8") as f:
        agents = json.load(f)
    return templates.TemplateResponse(
        "session_detail.html",
        {
            "request": request,
            "agents": agents,
            "session_filename": session_filename
        }
    )


@app.get("/download/{session_filename}")
def download_session(session_filename: str):
    return FileResponse(path=f"sessions/{session_filename}", filename=session_filename)


@app.get("/deploy/{session_filename}", response_class=HTMLResponse)
async def deploy_agents(request: Request, session_filename: str, background_tasks: BackgroundTasks):
    session_path = f"sessions/{session_filename}"

    def run_deployment():
        subprocess.run([sys.executable, "agent_creation_automation.py", session_path])
    background_tasks.add_task(run_deployment)
    return templates.TemplateResponse(
        "deploy.html",
        {
            "request": request,
            "session_filename": session_filename
        }
    )

if __name__ == "__main__":
    uvicorn.run("web_app:app", reload=True)
