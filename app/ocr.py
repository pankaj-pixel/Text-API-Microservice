import pathlib
import pytesseract
from PIL import Image

BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR = BASE_DIR / "images"

img_1 = IMG_DIR / "text-img.png"

img = Image.open(img_1)

pred = pytesseract.image_to_string(img)
req_test = [x for x in pred.split("\n")]
print(req_test)