import csv
import os
import random
import statistics
import time

from sorting import sort_parcels
from knapsack import knapsack
from dijkstra import dijkstra
from tsp import nearest_neighbor


random.seed(42)


def create_parcels(size):
    parcels = []

    for i in range(size):
        parcels.append({
            "id": f"P{i + 1}",
            "destination": f"N{i + 1}",
            "weight": random.randint(1, 10),
            "priority": random.randint(1, 3),
            "deadline": random.randint(1, 24),
            "value": random.randint(50, 500)
        })

    return parcels


def create_graph(size):
    graph = {f"N{i}": [] for i in range(size)}

    for i in range(size):
        a = f"N{i}"
        b = f"N{(i + 1) % size}"
        weight = random.randint(1, 20)

        graph[a].append((b, weight))
        graph[b].append((a, weight))

    for i in range(size):
        for j in range(i + 2, size):
            if random.random() < 0.08:
                weight = random.randint(1, 20)
                graph[f"N{i}"].append((f"N{j}", weight))
                graph[f"N{j}"].append((f"N{i}", weight))

    return graph


def create_distance_matrix(size):
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i + 1, size):
            distance = random.randint(1, 50)
            matrix[i][j] = distance
            matrix[j][i] = distance

    return matrix


def measure_average(function, *args):
    times = []

    for _ in range(3):
        start = time.perf_counter()
        function(*args)
        end = time.perf_counter()
        times.append(end - start)

    return statistics.mean(times)


def run_benchmark():
    sizes = [10, 20, 40, 80, 120]
    results = []

    print("\n========== PERFORMANCE BENCHMARK ==========")
    print("Average execution time of 3 runs\n")

    for size in sizes:
        parcels = create_parcels(size)
        graph = create_graph(size)
        matrix = create_distance_matrix(size)

        sorting_time = measure_average(sort_parcels, parcels)
        knapsack_time = measure_average(knapsack, parcels, size * 5)
        dijkstra_time = measure_average(
            dijkstra, graph, "N0"
        )
        tsp_time = measure_average(
            nearest_neighbor, matrix, 0
        )

        results.append([
            size,
            sorting_time,
            knapsack_time,
            dijkstra_time,
            tsp_time
        ])

        print(f"Dataset Size: {size}")
        print(f"Sorting:  {sorting_time:.8f} seconds")
        print(f"Knapsack: {knapsack_time:.8f} seconds")
        print(f"Dijkstra: {dijkstra_time:.8f} seconds")
        print(f"TSP:      {tsp_time:.8f} seconds")
        print("-" * 40)

    os.makedirs("output", exist_ok=True)

    with open("output/benchmark_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Dataset Size",
            "Sorting Time",
            "Knapsack Time",
            "Dijkstra Time",
            "TSP Time"
        ])

        writer.writerows(results)

    print("\nBenchmark completed!")
    print("Results saved in output/benchmark_results.csv")


if __name__ == "__main__":
    run_benchmark()
