from typing import Dict, Tuple, List
from .geo import dist_km


def baseline_time_min(a, b, base_speed_kmph: float = 20.0) -> Tuple[float, float]:
    d = dist_km(a, b)
    t = d / (base_speed_kmph / 60.0)
    return d, t


def active(zone: dict, t_min: int) -> bool:
    lo, hi = zone.get("active_min", [0, 1440])
    return lo <= (t_min % 1440) <= hi


def in_band(zone: dict, r: float) -> bool:
    band = zone.get("band")
    if not band:
        return True
    return band[0] <= r <= band[1]


def zone_multiplier(zones: List[dict], p_mid: Tuple[float, float], t_min: int) -> float:
    """Multiplicative stacking of active zone multipliers."""
    mult = 1.0
    x, y = p_mid
    r_mid = (x**2 + y**2) ** 0.5
    for z in zones:
        if not active(z, t_min):
            continue
        cx, cy = z["center"]
        r = ((x-cx)**2 + (y-cy)**2) ** 0.5
        if r <= z["radius_km"] and in_band(z, r_mid):
            mult *= z.get("multiplier", 1.0)
    return mult


def dynamic_time_min(a, b, t_min: int, cfg: Dict) -> Tuple[float, float]:
    d, t = baseline_time_min(a, b, base_speed_kmph=cfg.get("base_speed_kmph", 20.0))
    mid = ((a[0]+b[0])/2, (a[1]+b[1])/2)
    mult = zone_multiplier(cfg.get("zones", []), mid, t_min)
    return d, t * mult