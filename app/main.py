from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib
#initizaling templates path
BASE_DIR  = pathlib.Path(__file__).parent


app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))



@app.get("/", tags=["users"], response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(name="base.html", context={"request": request})


@app.post("/")
def get_home():
    return {"welcome To Home"}
