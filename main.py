import os
from pytube import YouTube
from fastapi import FastAPI

try: os.mkdir("music")
except: ...

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/download/{url}")
def download():
    file_name = YouTube("https://youtu.be/olWvy0PiLfA").streams.filter(only_audio=True).first().download()
    os.rename(file_name, "./music" + file_name[:len(file_name)-4].replace(os.getcwd(), "") + '.mp3')
    print(os.listdir("./music"))