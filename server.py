from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

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
async def machine_metrics(metrics: MachineMetrics):
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


if __name__ == '__main__':
    uvicorn.run('server:app', host='localhost', port=8081, reload=False)
