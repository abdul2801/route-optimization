from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Order:
    id: int
    x: float
    y: float
    ready_min: int
    sla_min: int
    service_min: int = 2


@dataclass
class Rider:
    id: int
    x: float
    y: float
    available_min: int = 0
    route: List[int] = None

    def __post_init__(self):
        if self.route is None:
            self.route = []


Point = Tuple[float, float]