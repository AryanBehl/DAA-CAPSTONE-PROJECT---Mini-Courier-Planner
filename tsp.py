def nearest_neighbor(distance_matrix, start=0):
    n = len(distance_matrix)

    if n == 0 or start < 0 or start >= n:
        return [], 0

    visited = {start}
    route = [start]
    total_distance = 0
    current = start

    while len(visited) < n:
        next_city = min(
            (city for city in range(n) if city not in visited),
            key=lambda city: distance_matrix[current][city]
        )

        total_distance += distance_matrix[current][next_city]
        route.append(next_city)
        visited.add(next_city)
        current = next_city

    total_distance += distance_matrix[current][start]
    route.append(start)

    return route, total_distance
