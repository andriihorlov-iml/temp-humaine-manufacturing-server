from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request
import uvicorn
import os

app = FastAPI()


class Bid(BaseModel):
    task: float
    machine: int
    bid: float


class MachineMetrics(BaseModel):
    machine_id: int
    down_time: float
    setup_time: float
    idle_time: float
    production_time: float


class Metrics(BaseModel):
    throughput: float
    energy: float
    lateness: float


class Objectives(BaseModel):
    throughput: float
    energy: float
    lateness: float


@app.post("/bids")
async def bids(bid: Bid):
    print("Bids:", bid)
    return bid


@app.post("/machine_metrics")
async def machine_metrics(metrics: MachineMetrics, request: Request):
    raw = await request.body()
    print("RAW BODY:", raw)
    print("Machine metrics:", metrics)
    return metrics

@app.post("/metrics")
async def metrics(metrics: Metrics):
    print("Metrics:", metrics)
    return metrics


@app.post("/objectives_init")
async def objectives_init(obj: Objectives):
    print("Objectives init:", obj)
    return obj


@app.post("/objectives")
async def objectives(obj: Objectives):
    print("Objectives:", obj)
    return obj

@app.middleware("http")
async def log_raw_request(request: Request, call_next):
    body = await request.body()
    print("=== RAW REQUEST ===")
    print("PATH:", request.url.path)
    print("METHOD:", request.method)
    print("HEADERS:", dict(request.headers))
    print("BODY RAW:", body)
    print("===================")
    response = await call_next(request)
    return response


if __name__ == '__main__':
    uvicorn.run("server:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8081)), reload=False)

