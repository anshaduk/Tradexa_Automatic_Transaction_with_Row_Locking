## E-Commerce Concurrency Problem ##


This project demonstrates how to handle a concurrency issue in an e-commerce application where two customers attempt to book overlapping inventory simultaneously. The goal is to ensure that the system prevents overselling and maintains data consistency.

## Problem Scenario ##

An e-commerce website has 5 products in stock.

Customer A arrives and books 4 products, confirming the order.

At the same time, Customer B tries to book products, but due to a technical issue, they see outdated inventory and attempt to book products that are no longer available.

## The challenge is to ensure that: ##

Customer A's booking is successful.

Customer B's booking fails gracefully, and they are notified of the stock unavailability.

The system maintains data consistency and prevents overselling.

## Solution ##

The solution involves:

Database Transactions: Using Django’s transaction.atomic() to ensure atomicity.

Row-Level Locking: Using select_for_update() to lock rows during critical operations.

Concurrency Control: Handling simultaneous requests gracefully to prevent race conditions.

## Key Features ##

Atomic Transactions: Ensures that all operations within a transaction are completed successfully or rolled back.

Row-Level Locking: Prevents race conditions by locking rows during critical operations.

Graceful Error Handling: Notifies users of stock unavailability without crashing the system.





## II. elevator optimization ##

First, let's verify the distance calculations:

Going up first (upward_distance):

Current floor: 2
Path: 2 → 3 → 4 → 1
Distance: |3-2| + |4-3| + |1-4| = 1 + 1 + 3 = 5 units

Going down first (downward_distance):

Current floor: 2
Path: 2 → 1 → 3 → 4
Distance: |1-2| + |3-1| + |4-3| = 1 + 2 + 1 = 4 units

Since downward_distance (4) < upward_distance (5), the algorithm correctly chose "down" as the direction.

The output shows:

Direction: "down" 
Path: [1, 3, 4] 

## Here using DSA Concepts:- 

1. Sorting: Ensures that the lift serves requests in the most efficient order.

2. Grouping: Helps categorize requests based on direction, simplifying decision-making.

3. Greedy Algorithm: Provides a locally optimal solution (minimizing distance at each step).

4. Decision-Making: Ensures the lift moves in the most efficient direction.

