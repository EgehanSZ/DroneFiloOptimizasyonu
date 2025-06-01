# test_performance.py

import time
from utils import distance
from data_generator import generate_random_data
from a_star import a_star
from genetic_algorithm import genetic_algorithm

def run_test(drones, deliveries, zones, algorithm_fn, algo_name):
    total_deliveries = len(drones) * len(deliveries)
    total_completed = 0
    total_energy = 0
    start_time = time.perf_counter()

    for drone in drones:
        # Genetik algoritma önce teslimatları, sonra drone'u alır
        if algorithm_fn.__name__ == "genetic_algorithm":
            route = algorithm_fn(deliveries, drone, zones)
        else:
            route = algorithm_fn(drone, deliveries, zones)

        total_completed += len(route)

        # Enerji = toplam uçuş mesafesi (örnek basitleştirilmiş model)
        pos = drone.start_pos
        energy = 0
        for d in route:
            energy += distance(pos, d.pos)
            pos = d.pos
        total_energy += energy

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"🔍 Algoritma: {algo_name}")
    print(f"✅ Tamamlanan Teslimat Yüzdesi: {total_completed / total_deliveries * 100:.2f}%")
    print(f"⚡ Ortalama Enerji Tüketimi: {total_energy / len(drones):.2f} birim")
    print(f"⏱️  Çalışma Süresi: {elapsed:.3f} saniye\n")

def run_all_tests():
    print("=== 📦 SENARYO 1: 5 Drone, 20 Teslimat, 2 No-Fly Zone ===")
    d1, dp1, z1 = generate_random_data(5, 20, 2)
    run_test(d1, dp1, z1, a_star, "A* Algoritması")
    run_test(d1, dp1, z1, genetic_algorithm, "Genetik Algoritma")

    print("=== 📦 SENARYO 2: 10 Drone, 50 Teslimat, 5 No-Fly Zone ===")
    d2, dp2, z2 = generate_random_data(10, 50, 5)
    run_test(d2, dp2, z2, a_star, "A* Algoritması")
    run_test(d2, dp2, z2, genetic_algorithm, "Genetik Algoritma")

def evaluate_cached_routes(drone_routes, algo_name):
    from utils import distance
    import time

    total_completed = 0
    total_energy = 0
    start = time.perf_counter()

    for drone, route in drone_routes:
        total_completed += len(route)
        energy = 0
        pos = drone.start_pos
        for d in route:
            energy += distance(pos, d.pos)
            pos = d.pos
        total_energy += energy

    end = time.perf_counter()
    print(f"🔍 Algoritma: {algo_name}")
    print(f"✅ Tamamlanan Teslimat: {total_completed}")
    print(f"⚡ Ortalama Enerji: {total_energy / len(drone_routes):.2f}")
    print(f"⏱️  Süre: {end - start:.3f} saniye\n")


