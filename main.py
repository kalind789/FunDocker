from model_dev import model_pipeline
from fastapi import FastAPI, UploadFile
from typing import Union
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))

    result = model_pipeline(text=text, image=image)

    return {"result": result}