# a_star.py

import heapq
from utils import distance
from constraints import is_valid_move

def a_star(drone, deliveries, zones):
    path = []
    visited = set()
    current_pos = drone.start_pos
    current_time = 0

    while len(visited) < len(deliveries):
        heap = []

        for d in deliveries:
            if d.id in visited:
                continue

            dist = distance(current_pos, d.pos)
            arrival_time = current_time + dist / drone.speed

            valid, penalty = is_valid_move(drone, current_pos, d, arrival_time, zones)
            if not valid:
                continue

            cost = dist * d.weight + d.priority * 100 + penalty
            heapq.heappush(heap, (cost, d, arrival_time))

        if not heap:
            print("🚫 A* çıkmazda: teslim edilemeyen noktalar kaldı.")
            break

        _, chosen, arrival_time = heapq.heappop(heap)
        path.append(chosen)
        visited.add(chosen.id)
        current_time = arrival_time
        current_pos = chosen.pos

    print(f"✅ A* algoritması {len(path)} teslimat ile tamamlandı.")
    return path
