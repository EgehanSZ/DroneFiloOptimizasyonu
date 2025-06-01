from data_loader import load_sample_data
from data_generator import generate_random_data
from a_star import a_star
from genetic_algorithm import genetic_algorithm
from visualizer import plot_routes_from_cache
from test_performance import evaluate_cached_routes

def run_all_once():
    # SENARYO 1 — Sabit veri
    drones1, deliveries1, zones1 = load_sample_data()
    a_star_routes_1 = [(drone, a_star(drone, deliveries1, zones1)) for drone in drones1]
    ga_routes_1 = [(drone, genetic_algorithm(deliveries1, drone, zones1)) for drone in drones1]

    print("📊 [GRAFİK] A* – Senaryo 1")
    plot_routes_from_cache(a_star_routes_1, zones1, "A* – Senaryo 1")

    print("📊 [GRAFİK] GA – Senaryo 1")
    plot_routes_from_cache(ga_routes_1, zones1, "GA – Senaryo 1")

    print("📊 [TEST] Senaryo 1")
    evaluate_cached_routes(a_star_routes_1, "A*")
    evaluate_cached_routes(ga_routes_1, "GA")

    # SENARYO 2 — Rastgele veri
    drones2, deliveries2, zones2 = generate_random_data(10, 50, 5)
    a_star_routes_2 = [(drone, a_star(drone, deliveries2, zones2)) for drone in drones2]
    ga_routes_2 = [(drone, genetic_algorithm(deliveries2, drone, zones2)) for drone in drones2]

    print("📊 [GRAFİK] A* – Senaryo 2")
    plot_routes_from_cache(a_star_routes_2, zones2, "A* – Senaryo 2")

    print("📊 [GRAFİK] GA – Senaryo 2")
    plot_routes_from_cache(ga_routes_2, zones2, "GA – Senaryo 2")

    print("📊 [TEST] Senaryo 2")
    evaluate_cached_routes(a_star_routes_2, "A*")
    evaluate_cached_routes(ga_routes_2, "GA")

if __name__ == "__main__":
    run_all_once()
