import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    parents = {node: None for node in graph}

    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current = heapq.heappop(pq)

        if current_distance > distances[current]:
            continue

        for neighbor, weight in graph[current]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current
                heapq.heappush(pq, (new_distance, neighbor))

    return distances, parents


def get_path(parents, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = parents[current]

    return path[::-1]
