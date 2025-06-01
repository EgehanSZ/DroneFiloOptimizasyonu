# models.py

from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Drone:
    id: int
    max_weight: float         # kg
    battery: int              # mAh
    speed: float              # m/s
    start_pos: Tuple[float, float]

@dataclass
class DeliveryPoint:
    id: int
    pos: Tuple[float, float]
    weight: float             # kg
    priority: int             # 1-5
    time_window: Tuple[int, int]  # dakika cinsinden (ör: 540 = 09:00)

@dataclass
class NoFlyZone:
    id: int
    coordinates: List[Tuple[float, float]]
    active_time: Tuple[int, int]
