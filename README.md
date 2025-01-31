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