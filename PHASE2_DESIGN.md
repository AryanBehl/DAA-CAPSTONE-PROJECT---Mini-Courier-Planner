
# PHASE 2 – Parcel Prioritization and Vehicle Loading

## 1. Objective

To prioritize parcels based on priority and deadline and select the best combination of parcels within the courier's weight capacity.

## 2. Parcel Sorting

Merge Sort is used to arrange parcels according to:

1. Higher priority first.
2. Earlier deadline first when priorities are equal.

## 3. Dynamic Programming

The 0/1 Knapsack algorithm is used to maximize the total parcel value without exceeding the courier's weight capacity.

## 4. Sample Input

| Parcel | Weight | Priority | Deadline | Value |
|---|---:|---:|---:|---:|
| P1 | 2 kg | 3 | 10 | 100 |
| P2 | 4 kg | 2 | 12 | 200 |
| P3 | 3 kg | 3 | 11 | 150 |
| P4 | 5 kg | 1 | 15 | 250 |
| P5 | 1 kg | 3 | 9 | 80 |

## 5. Courier Capacity

Maximum capacity: 8 kg.

## 6. Selected Parcels

- P5 – 1 kg
- P3 – 3 kg
- P2 – 4 kg

Total weight: 8 kg

Total parcel value: 430

## 7. Conclusion

Merge Sort prioritizes parcels, while Dynamic Programming selects the combination that maximizes total parcel value within the courier's capacity.
