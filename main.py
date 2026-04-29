from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime, timezone

app = FastAPI()

latest = {"text": "", "timestamp": ""}


@app.post("/output")
async def receive_output(request: Request):
    body = await request.body()
    latest["text"] = body.decode("utf-8")
    latest["timestamp"] = datetime.now(timezone.utc).isoformat()
    return {"status": "ok"}


@app.get("/output")
async def get_output():
    return JSONResponse(latest)


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html") as f:
        return f.read()
