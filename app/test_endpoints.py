from main import app
from fastapi.testclient import TestClient
from main import BASE_DIR,UPLOAD_DIR
import shutil
from PIL import Image,ImageChops
import io




client = TestClient(app)


def test_root():
    response = client.get("/")
    print(response)
    assert response.status_code == 200
    print(response.headers)
    assert "text/html" in  response.headers['content-type']

def test_get_home():
    response = client.post("/")
    print(response)
    assert response.status_code == 200
    print(response.headers)
    assert "application/json" in  response.headers['content-type']
   
def test_post_upload():
    image_saved_path = BASE_DIR / "images"
    for path in image_saved_path.glob("*"):
        try:
            img =Image.open(path)
        except:
            img = None

        response = client.post("/upload",files={"file":open(path,'rb')})
        if img is None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200 
            data = response.json()
            print(data)
            assert len(data.keys()) ==2
            
    #print(path)
    shutil.rmtree(UPLOAD_DIR)    

        