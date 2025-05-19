import argparse, json
from .utils.config import load_config
from .core.simulate import make_orders
from .core.dispatch import plan_routes
from .metrics.kpis import kpis_summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="YAML config path")
    parser.add_argument("--orders", type=int, default=28)
    parser.add_argument("--riders", type=int, default=None, help="override rider count")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    cfg = load_config(args.config)
    if args.riders is not None:
        cfg["riders"]["count"] = args.riders

    orders = make_orders(cfg, n_orders=args.orders, seed=args.seed)
    plan = plan_routes(cfg, orders)
    summary = kpis_summary(plan)

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()