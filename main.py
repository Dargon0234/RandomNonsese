import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime, timezone

app = FastAPI()

latest      = {"text": "", "timestamp": ""}
vm_latest   = {}
tree_latest  = {}
event_latest = {}
npc_latest       = {}
ask_queue        = {"question": "", "timestamp": ""}
response_latest  = {"question": "", "response": "", "tick": 0}


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
    vm_latest.update(json.loads(body))
    return {"status": "ok"}


@app.get("/vm")
async def get_vm():
    return JSONResponse(vm_latest)


@app.post("/tree")
async def receive_tree(request: Request):
    body = await request.body()
    tree_latest.clear()
    tree_latest.update(json.loads(body))
    return {"status": "ok"}


@app.get("/tree")
async def get_tree():
    return JSONResponse(tree_latest)


@app.post("/event")
async def receive_event(request: Request):
    body = await request.body()
    event_latest.clear()
    event_latest.update(json.loads(body))
    return {"status": "ok"}


@app.get("/event")
async def get_event():
    return JSONResponse(event_latest)


@app.post("/npc")
async def receive_npc(request: Request):
    body = await request.body()
    npc_latest.clear()
    npc_latest.update(json.loads(body))
    return {"status": "ok"}


@app.get("/npc")
async def get_npc():
    return JSONResponse(npc_latest)


@app.post("/ask")
async def receive_ask(request: Request):
    body = await request.body()
    data = json.loads(body)
    ask_queue["question"]  = data.get("question", "")
    ask_queue["timestamp"] = datetime.now(timezone.utc).isoformat()
    return {"status": "ok"}


@app.get("/ask")
async def get_ask():
    return JSONResponse(ask_queue)


@app.post("/response")
async def receive_response(request: Request):
    body = await request.body()
    response_latest.clear()
    response_latest.update(json.loads(body))
    return {"status": "ok"}


@app.get("/response")
async def get_response():
    return JSONResponse(response_latest)


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html") as f:
        return f.read()


@app.get("/visualizer", response_class=HTMLResponse)
async def visualizer():
    with open("static/visualizer.html") as f:
        return f.read()
