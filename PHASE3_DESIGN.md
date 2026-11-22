
# PHASE 3 – Route Master and Delivery Optimization

## 1. Objective

To calculate the shortest delivery distances and generate an efficient delivery route using graph algorithms.

## 2. Graph Representation

The road network is represented using a weighted adjacency list.

- W – Warehouse
- A, B, C, D, E – Delivery locations
- Edge weights represent road distances in kilometres.

## 3. Dijkstra's Algorithm

Dijkstra's Shortest Path Algorithm calculates the shortest distance between delivery locations.

It uses a priority queue to process the nearest unvisited location.

## 4. Nearest Neighbor TSP Approximation

The Nearest Neighbor algorithm generates an approximate delivery route.

It starts from the warehouse, visits the nearest unvisited location and finally returns to the starting point.

## 5. Sample Delivery Route

W → C → B → E → W

Total Route Distance: 23 km

## 6. Conclusion

Dijkstra calculates shortest paths between locations, while Nearest Neighbor generates an approximate delivery route for the selected parcels.
