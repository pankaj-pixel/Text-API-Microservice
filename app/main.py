from fastapi import (FastAPI,Request,UploadFile,Depends,File,HTTPException )
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import pathlib
import uuid
import os
import io 
import pytesseract
import time

#initizaling templates path
BASE_DIR  = pathlib.Path(__file__).parent
UPLOAD_DIR =BASE_DIR /"uploads"


app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))


@app.get("/", tags=["users"], response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(name="base.html", context={"request": request})


@app.post("/")
async def get_home(file: UploadFile = File(...) ):

    UPLOAD_DIR.mkdir( exist_ok=True) 
    file_bytes = io.BytesIO(await file.read())  # Read the file asynchronously    
    try:
         img = Image.open(file_bytes)
        
    except:
        raise HTTPException(detail="Invalid Image",status_code=400)
    
    pred = pytesseract.image_to_string(img)
    print(pred)
    req_result = [x for x in pred.split(" ")]
    print(req_result)

    return {"Results ": req_result , "Originals" :pred}   



@app.post("/upload", response_class=FileResponse)
async def post_upload(file: UploadFile = File(...) ):

    UPLOAD_DIR.mkdir( exist_ok=True) 
    file_bytes = io.BytesIO(await file.read())  # Read the file asynchronously    
    try:
         img = Image.open(file_bytes)
         pred = pytesseract.image_to_string(img)
         print(pred)


    except:
        raise HTTPException(detail="Invalid Image",status_code=400)
    fname = pathlib.Path(file.filename)
    fext = fname.suffix
    des = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"
    img.save(des)
    return des
