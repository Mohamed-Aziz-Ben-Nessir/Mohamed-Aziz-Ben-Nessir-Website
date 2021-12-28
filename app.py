import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,FileResponse
path="./posts/"
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/blog/{file}')
def read(file):
    file_path = os.path.join(path,file)
    if os.path.exists(file_path):
        return FileResponse(file_path,media_type="text/plain")
    return {"error" : "File not found!"}

@app.get('/blog', response_class=HTMLResponse)
def Blog(request: Request):
    files=list_files()
    return templates.TemplateResponse("blog.html", {"request": request,"files":files})

def list_files():
    files = []
    for filename in os.listdir(path):
        files.append(filename)
    return files

if __name__ == '__main__':
    uvicorn.run(app) 
