from imp import reload
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from fastapi.templating import Jinja2Templates 

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def main():
    return FileResponse('index.html')

@app.get("/commands")
def read_root():
    return FileResponse('commands.html')

@app.get("/notice")
def read_root():
    return FileResponse('notice.html')

@app.get("/discord")
def read_root():
    return FileResponse('discord.html')

@app.get("/invite")
def read_root():
    return FileResponse('invite.html')

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
