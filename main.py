from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime, timezone

app = FastAPI()

latest    = {"text": "", "timestamp": ""}
vm_latest = {}


@app.post("/output")
async def receive_output(request: Request):
    body = await request.body()
    latest["text"]      = body.decode("utf-8")
    latest["timestamp"] = datetime.now(timezone.utc).isoformat()
    return {"status": "ok"}


@app.get("/output")
async def get_output():
    return JSONResponse(latest)


@app.post("/vm")
async def receive_vm(request: Request):
    body = await request.body()
    vm_latest.clear()
    vm_latest.update(__import__("json").loads(body))
    return {"status": "ok"}


@app.get("/vm")
async def get_vm():
    return JSONResponse(vm_latest)


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html") as f:
        return f.read()


@app.get("/visualizer", response_class=HTMLResponse)
async def visualizer():
    with open("static/visualizer.html") as f:
        return f.read()
