
# PHASE 1 – Problem Design and Planning

## 1. Project Overview

Mini Courier Planner is a Python-based courier delivery planning system developed using Design and Analysis of Algorithms.

## 2. Problem Statement

The system is designed to prioritize parcels, select parcels within the courier's weight capacity and plan delivery routes using graph algorithms.

## 3. Parcel Attributes

Each parcel contains the following information:

- Parcel ID
- Destination
- Weight
- Priority
- Deadline
- Value

## 4. Delivery Network Design

The delivery network is represented using a weighted adjacency list.

Locations:
- W – Warehouse
- A, B, C, D, E – Delivery locations

Road distances are represented as edge weights in kilometres.

## 5. Algorithm Selection

| Algorithm | Purpose |
|---|---|
| Merge Sort | Parcel prioritization |
| 0/1 Knapsack | Parcel selection |
| Dijkstra | Shortest path calculation |
| Nearest Neighbor | Delivery route approximation |

## 6. Courier Capacity

The sample courier capacity is 8 kg.

## 7. Tools Used

- Python 3
- Visual Studio Code
- JSON

## 8. Expected Outcome

The system should prioritize parcels, select valuable parcels within the capacity limit and generate a delivery route.
