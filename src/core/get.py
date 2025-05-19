import math
from typing import Tuple

Point = Tuple[float, float]

def dist_km(a: Point, b: Point) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])