# constraints.py

from models import Drone, DeliveryPoint, NoFlyZone
from utils import segment_intersects_polygon

def check_capacity(drone: Drone, delivery: DeliveryPoint):
    return delivery.weight <= drone.max_weight

def check_time_window(delivery: DeliveryPoint, arrival_time: float):
    return delivery.time_window[0] <= arrival_time <= delivery.time_window[1]

def check_no_fly_zone(current_pos, delivery, current_time, zones):
    penalty = 0
    for z in zones:
        if z.active_time[0] <= current_time <= z.active_time[1]:
            if segment_intersects_polygon(current_pos, delivery.pos, z.coordinates):
                penalty += 10000  # büyük bir ceza (ama geçişi engellemez)
    return True, penalty

def is_valid_move(drone: Drone, current_pos, delivery: DeliveryPoint, current_time: float, zones):
    if not check_capacity(drone, delivery):
        return False, 0
    if not check_time_window(delivery, current_time):
        return False, 0
    valid, penalty = check_no_fly_zone(current_pos, delivery, current_time, zones)
    return True, penalty
