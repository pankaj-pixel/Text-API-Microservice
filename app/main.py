from fastapi import (FastAPI,Request,UploadFile,Depends,File )
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import pathlib
import uuid
import os
import io 
#initizaling templates path
BASE_DIR  = pathlib.Path(__file__).parent
UPLOAD_DIR =BASE_DIR /"uploads"


app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))


@app.get("/", tags=["users"], response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(name="base.html", context={"request": request})


@app.post("/")
def get_home():
    return {"welcome To Home"}



@app.post("/upload", response_class=FileResponse)
async def post_upload(file: UploadFile = File(...) ):
    UPLOAD_DIR.mkdir( exist_ok=True) 
    file_bytes = io.BytesIO(await file.read())  # Read the file asynchronously
    
    img = Image.open(file_bytes)
    print(img)
    


    fname = pathlib.Path(file.filename)
    fext = fname.suffix
    des = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"
    with open(des, 'wb') as out_file:
        out_file.write(file_bytes.read())
    print(f"File saved to {des}")
    return des
