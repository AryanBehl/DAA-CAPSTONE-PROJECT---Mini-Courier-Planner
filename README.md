# Mini Courier Planner

An algorithm-based courier delivery planning system developed using Python.

## Project Objective

The objective is to optimize courier parcel prioritization, vehicle loading and delivery routes using Design and Analysis of Algorithms (DAA).

The system selects valuable parcels within the courier's weight capacity and generates an efficient delivery route using graph algorithms.

## Technologies Used

- Python 3
- JSON
- CSV
- Visual Studio Code

## Algorithms Implemented

1. Merge Sort
2. 0/1 Knapsack using Dynamic Programming
3. Dijkstra's Shortest Path Algorithm
4. Nearest Neighbor TSP Approximation
5. Performance Analysis using Execution Time Measurement

## Project Phases

| Phase | Description |
|---|---|
| 1 | Problem Design and Planning |
| 2 | Parcel Prioritization and Optimal Package Selection |
| 3 | Shortest Delivery Paths and Route Optimization |
| 4 | Performance Testing and Optimization |
| 5 | Final Report and Demonstration |

## Sample Results

- Total Parcels: 5
- Delivery Locations Selected: 3
- Courier Capacity: 8 kg
- Selected Parcels: 3
- Total Loaded Weight: 8 kg
- Total Parcel Value: 430
- Delivery Route: W → C → B → E → W
- Total Route Distance: 23 km

*Results are based on the sample dataset provided with the project.*

## How to Run

Run these commands from the project root directory.

**Run the main application:**

```bash
python main.py
```

**Run performance benchmarking:**

```bash
python benchmark.py
```

## Project Structure

```text
Mini-Courier-Planner/
│
├── main.py
├── sorting.py
├── knapsack.py
├── dijkstra.py
├── tsp.py
├── performance.py
├── benchmark.py
├── parcels.json
├── README.md
│
├── data/
├── output/
│
├── Phase1_Screenshots/
├── Phase2_Screenshots/
├── Phase3_Screenshots/
├── Phase4_Screenshots/
└── Phase5_Screenshots/
```

## Output

The application displays:

- Prioritized parcel list
- Optimal parcel selection
- Total loaded weight and parcel value
- Shortest distance matrix
- Optimized delivery route
- Execution time of each algorithm

Benchmark results are saved in the `output` directory as a CSV file.

## Project Limitations

- Uses a predefined road network.
- Uses sample parcel data.
- Does not integrate live traffic information.
- Nearest Neighbor provides an approximate TSP route, not a guaranteed optimal route.

## Future Scope

- Live traffic integration
- Interactive delivery maps
- Multiple courier vehicles
- Real-time parcel tracking
- Larger delivery datasets

## Author

**Aryan Behl**  
K.R. Mangalam University  
B.Tech – Computer Science and Engineering  
Design and Analysis of Algorithms (DAA) Capstone Project