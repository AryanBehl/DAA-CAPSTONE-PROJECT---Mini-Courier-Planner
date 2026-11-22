import json

from sorting import sort_parcels
from knapsack import knapsack
from dijkstra import dijkstra
from tsp import nearest_neighbor
from performance import measure_time


with open("parcels.json", "r") as file:
    parcels = json.load(file)

graph = {
    "W": [("A", 4), ("B", 6), ("C", 5)],
    "A": [("W", 4), ("B", 2), ("C", 3)],
    "B": [("W", 6), ("A", 2), ("C", 2), ("D", 4)],
    "C": [("W", 5), ("A", 3), ("B", 2), ("D", 3), ("E", 6)],
    "D": [("B", 4), ("C", 3), ("E", 2)],
    "E": [("C", 6), ("D", 2)]
}


sorted_parcels, sort_time = measure_time(
    sort_parcels, parcels
)


capacity = 8

(selected_parcels, total_value), knapsack_time = measure_time(
    knapsack, sorted_parcels, capacity
)


def build_distance_matrix(locations):
    matrix = []

    for start in locations:
        distances, _ = dijkstra(graph, start)

        row = [distances[destination] for destination in locations]
        matrix.append(row)

    return matrix


locations = ["W"] + [
    parcel["destination"] for parcel in selected_parcels
]

distance_matrix, dijkstra_time = measure_time(
    build_distance_matrix, locations
)


(route, route_distance), tsp_time = measure_time(
    nearest_neighbor, distance_matrix, 0
)


print("\n========== MINI COURIER PLANNER ==========")

print("\n1. PARCEL PRIORITIZATION")
for parcel in sorted_parcels:
    print(
        parcel["id"],
        "Priority:", parcel["priority"],
        "Deadline:", parcel["deadline"]
    )

print("\n2. OPTIMAL PACKING PLAN")
for parcel in selected_parcels:
    print(
        parcel["id"],
        "Destination:", parcel["destination"],
        "Weight:", parcel["weight"], "kg",
        "Value:", parcel["value"]
    )

print("Total Weight:",
      sum(p["weight"] for p in selected_parcels), "kg")

print("Total Parcel Value:", total_value)
print("Courier Capacity:", capacity, "kg")

print("\n3. SHORTEST DELIVERY ROUTE")

print("Delivery Locations:", locations)

print("\nDistance Matrix:")
for row in distance_matrix:
    print(row)

print("\nFinal Route:")
print(" -> ".join(locations[i] for i in route))

print("Total Route Distance:", route_distance, "km")

print("\n4. PERFORMANCE ANALYSIS")
print(f"Sorting Time: {sort_time:.8f} seconds")
print(f"Knapsack Time: {knapsack_time:.8f} seconds")
print(f"Dijkstra Time: {dijkstra_time:.8f} seconds")
print(f"TSP Time: {tsp_time:.8f} seconds")

print("\n========== PROJECT COMPLETED ==========")
