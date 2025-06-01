# data_generator.py

import random
from models import Drone, DeliveryPoint, NoFlyZone

def generate_random_data(num_drones, num_deliveries, num_zones):
    drones = [
        Drone(
            id=i+1,
            max_weight=random.uniform(2.0, 6.0),
            battery=random.randint(8000, 20000),
            speed=random.uniform(5.0, 12.0),
            start_pos=(random.uniform(0, 100), random.uniform(0, 100))
        ) for i in range(num_drones)
    ]

    deliveries = [
        DeliveryPoint(
            id=i+1,
            pos=(random.uniform(0, 100), random.uniform(0, 100)),
            weight=random.uniform(1.0, 5.0),
            priority=random.randint(1, 5),
            time_window=(0, 120)
        ) for i in range(num_deliveries)
    ]

    zones = [
        NoFlyZone(
            id=i+1,
            coordinates=[(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(4)],
            active_time=(0, 120)
        ) for i in range(num_zones)
    ]

    return drones, deliveries, zones
