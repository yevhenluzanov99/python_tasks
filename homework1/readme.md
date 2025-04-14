# Homework 1: Custom Hash Table Implementation

## Task Description

Implement a class with the following features:

1. **Base Properties**: The class should behave like a `dict`.
2. **Hash Table Mechanism**:
    - Add a new key-value pair.
    - Insert a new pair into the correct position in the hash table by calculating the index.
    - Retrieve a value by its key.
3. **Resizing**:
    - Scale the hash table when it reaches a certain fill percentage by rehashing (migration).
4. **Collision Handling** (Optional):
    - Implement a mechanism to handle collisions (e.g., linear probing).

## Running Tests

To run the tests, execute the following command:

```bash
python -m homework1.tests
```