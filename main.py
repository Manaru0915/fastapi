from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉", "中吉", "小吉", "吉",
        "半吉", "末吉", "末小吉",
        "凶", "小凶", "大凶"
    ]
    return {"result": random.choice(omikuji_list)}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>自己紹介ページ</title>
        </head>
        <body>
            <h1>こんにちは！</h1>
            <p>田中マナルです。</p>
            <p>趣味はONE OK ROCKの音楽を聴くことです。</p>
            <p>FastAPIで作成したWebページです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

    @app.post("/artist")
async def artist(name):
    return {
        "message": f"{name}は私の好きなアーティストです。特にONE OK ROCKがおすすめです。"
    }