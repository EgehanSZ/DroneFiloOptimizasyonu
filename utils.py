# utils.py

import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def point_in_polygon(point, polygon):
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        intersect = (yi > y) != (yj > y) and x < (xj - xi)*(y - yi)/(yj - yi + 1e-10) + xi
        if intersect:
            inside = not inside
    return inside

def segment_intersects_polygon(p1, p2, polygon):
    def ccw(a, b, c):
        return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])

    def intersect(a, b, c, d):
        return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

    for i in range(len(polygon)):
        if intersect(p1, p2, polygon[i], polygon[(i + 1) % len(polygon)]):
            return True
    return False
