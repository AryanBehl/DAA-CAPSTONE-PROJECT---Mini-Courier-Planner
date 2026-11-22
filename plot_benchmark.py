import csv
import os
import matplotlib.pyplot as plt

sizes = []
sorting = []
knapsack = []
dijkstra = []
tsp = []

with open("output/benchmark_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sizes.append(int(row["Dataset Size"]))
        sorting.append(float(row["Sorting Time"]))
        knapsack.append(float(row["Knapsack Time"]))
        dijkstra.append(float(row["Dijkstra Time"]))
        tsp.append(float(row["TSP Time"]))

plt.figure(figsize=(10, 6))

plt.plot(sizes, sorting, marker="o", label="Merge Sort")
plt.plot(sizes, knapsack, marker="o", label="0/1 Knapsack")
plt.plot(sizes, dijkstra, marker="o", label="Dijkstra")
plt.plot(sizes, tsp, marker="o", label="Nearest Neighbor TSP")

plt.xlabel("Dataset Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Algorithm Performance Comparison")
plt.legend()
plt.grid(True)

os.makedirs("output", exist_ok=True)
plt.savefig("output/performance_chart.png", dpi=300)
plt.show()

print("Performance chart saved in output/performance_chart.png")
