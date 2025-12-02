from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import random
import json
from typing import Dict, Any

app = FastAPI()

# ===  CONSTANTS ===
MachineMetricsMaxDownTime = 1.0
MachineMetricsMaxIdleTime = 1.0
MachineMetricsMaxProductionTime = 1.0
MachineMetricsMaxSetupTime = 1.0

BidMaxTask = 10.0
BidMax = 1.0

PerformanceMetricsMaxThroughput = 99.0
PerformanceMetricsMaxEnergy = 2000
PerformanceMetricsMaxLateness = 10.0

ObjectivesInitMax = 0.3

CONFIG_DATA = {
    "stayDuration": 15,
    "EnergyBoundaries": {
        "Min": 1,
        "Max": 10
    },
    "ThroughputBoundaries": {
        "Min": 1,
        "Max": 100
    },
    "LatenessBoundaries": {
        "Min": 1,
        "Max": 10
    }
}

# === MODELS ===
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

@app.get("/config")
async def get_config() -> Dict[str, Any]:
    print("Serving Config:", CONFIG_DATA)
    return CONFIG_DATA

# === RANDOM RESPONSES ===

@app.post("/bids")
async def bids(bid: Bid):
    random_bid = Bid(
        task=random.uniform(0.0, BidMaxTask),
        machine=bid.machine,
        bid=random.uniform(0.0, BidMax)
    )
    print("Random Bid:", random_bid)
    return random_bid


@app.post("/machine_metrics")
async def machine_metrics(metrics: MachineMetrics):
    random_metrics = MachineMetrics(
        machine_id=metrics.machine_id,
        down_time=random.uniform(0.0, MachineMetricsMaxDownTime),
        setup_time=random.uniform(0.0, MachineMetricsMaxSetupTime),
        idle_time=random.uniform(0.0, MachineMetricsMaxIdleTime),
        production_time=random.uniform(0.0, MachineMetricsMaxProductionTime)
    )
    print("Random Machine Metrics:", random_metrics)
    return random_metrics


@app.post("/metrics")
async def metrics(metrics: Metrics):
    random_metrics = Metrics(
        throughput=random.uniform(0.0, PerformanceMetricsMaxThroughput),
        energy=random.uniform(0.0, PerformanceMetricsMaxEnergy),
        lateness=random.uniform(0.0, PerformanceMetricsMaxLateness)
    )
    print("Random Metrics:", random_metrics)
    return random_metrics


@app.post("/objectives_init")
async def objectives_init(obj: Objectives):
    random_obj = Objectives(
        throughput=random.uniform(0.0, ObjectivesInitMax),
        energy=random.uniform(0.0, ObjectivesInitMax),
        lateness=random.uniform(0.0, ObjectivesInitMax)
    )
    print("Random Objectives Init:", random_obj)
    return random_obj


@app.post("/objectives")
async def objectives(obj: Objectives):
    print("Set Objectives:", obj)
    return obj


if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=8081)
