
# PHASE 4 – Performance Testing and Optimization

## 1. Objective

To evaluate and compare the execution time of implemented algorithms using different dataset sizes.

## 2. Dataset Sizes

The following dataset sizes were tested:

- 10 parcels
- 20 parcels
- 40 parcels
- 80 parcels
- 120 parcels

## 3. Testing Methodology

1. Generate datasets of different sizes.
2. Execute each algorithm three times.
3. Calculate average execution time.
4. Store benchmark results in a CSV file.
5. Generate a performance comparison chart.

## 4. Algorithms Tested

- Merge Sort
- 0/1 Knapsack
- Dijkstra's Algorithm
- Nearest Neighbor TSP Approximation

## 5. Performance Results

The benchmark showed that execution time generally increases as dataset size increases.

The 0/1 Knapsack algorithm showed a noticeable increase in execution time as the dataset size and capacity increased.

## 6. Generated Files

- output/benchmark_results.csv
- output/performance_chart.png

## 7. Conclusion

Performance testing helps compare algorithm execution times and understand their behaviour with increasing input sizes.
