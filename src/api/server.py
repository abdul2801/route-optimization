from fastapi import FastAPI
from pydantic import BaseModel
from ..utils.config import load_config
from ..core.simulate import make_orders
from ..core.dispatch import plan_routes
from ..metrics.kpis import kpis_summary


class OptimizeRequest(BaseModel):
    config_path: str
    orders: int = 28
    riders: int | None = None
    seed: int = 42


app = FastAPI(title="Food Delivery Optimizer (India-aware)")


@app.post("/optimize")
def optimize(req: OptimizeRequest):
    cfg = load_config(req.config_path)
    if req.riders is not None:
        cfg["riders"]["count"] = req.riders
    orders = make_orders(cfg, n_orders=req.orders, seed=req.seed)
    plan = plan_routes(cfg, orders)
    summary = kpis_summary(plan)
    return {"summary": summary, "plan": plan}