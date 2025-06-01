def plot_routes_from_cache(drone_routes, zones, title):
    import matplotlib.pyplot as plt
    from matplotlib.cm import get_cmap

    cmap = get_cmap("tab20")
    plt.figure(figsize=(12, 10))
    print(f"🎨 Grafik çiziliyor: {title}")
    for i, (drone, route) in enumerate(drone_routes):
        if not route:
            continue
        xs = [drone.start_pos[0]] + [d.pos[0] for d in route]
        ys = [drone.start_pos[1]] + [d.pos[1] for d in route]
        color = cmap(i % 20)
        plt.plot(xs, ys, marker='o', label=f"Drone {drone.id}", color=color)
        plt.scatter(*drone.start_pos, color=color, s=100, marker='s')

    for z in zones:
        coords = z.coordinates + [z.coordinates[0]]
        xz, yz = zip(*coords)
        plt.fill(xz, yz, alpha=0.2, color='red', label=f"NFZ {z.id}")

    plt.title(title)
    plt.xlabel("X Koordinat")
    plt.ylabel("Y Koordinat")
    plt.grid(True)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
