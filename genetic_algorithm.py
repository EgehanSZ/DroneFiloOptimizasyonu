# genetic_algorithm.py

import random
from utils import distance
from constraints import is_valid_move

def fitness(route, drone, zones):
    delivered = 0
    violations = 0
    energy = 0
    pos = drone.start_pos
    current_time = 0

    for delivery in route:
        d = distance(pos, delivery.pos)
        travel_time = d / drone.speed
        arrival_time = current_time + travel_time
        energy += d

        if is_valid_move(drone, pos, delivery, arrival_time, zones):
            delivered += 1
            current_time = arrival_time
            pos = delivery.pos
        else:
            violations += 1

    return delivered * 1000 - energy * 1.0 - violations * 500

def crossover(p1, p2):
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = p1[start:end] + [item for item in p2 if item not in p1[start:end]]
    return child

def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

def genetic_algorithm(deliveries, drone, zones, generations=100, population_size=30):
    population = [random.sample(deliveries, len(deliveries)) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda r: -fitness(r, drone, zones))
        new_population = population[:5]  # elit

        while len(new_population) < population_size:
            p1, p2 = random.sample(population[:10], 2)
            child = crossover(p1, p2)
            if random.random() < 0.2:
                mutate(child)
            new_population.append(child)

        population = new_population

    best = max(population, key=lambda r: fitness(r, drone, zones))
    return best
