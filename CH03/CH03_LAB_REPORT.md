# Chapter 3: Recursion — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 05/04/2026
- Course: COSC 2436

## Algorithm Summary

Recursion is a technique where a function calls itself to solve smaller parts of a problem. Every recursive function has a base case and a recursive case. The base case stops the recursion, while the recursive case reduces the problem into smaller subproblems.

### Two Parts of Every Recursive Function
1. **Base Case:** The stopping condition. Without it, the function would run forever.
2. **Recursive Case:** The function calls itself with a smaller input.

### The Call Stack
Each recursive call is placed on a call stack. The function pauses and waits for smaller calls to finish.

Example: fact(4)

fact(4)  
→ 4 × fact(3)  
→ 3 × fact(2)  
→ 2 × fact(1)  
→ return 1  
→ return 2  
→ return 6  
→ return 24  

### Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|-----------|----------------|-----------------|
| countdown | i <= 0 | countdown(i-1) | O(n) |
| fact | x <= 1 | x * fact(x-1) | O(n) |
| recursive_sum | empty list | first + sum(rest) | O(n) |
| recursive_count | empty list | 1 + count(rest) | O(n) |
| recursive_max | single item | max(first, max(rest)) | O(n) |

## Test Results

Program runs successfully:
- Countdown prints correctly  
- Factorial returns correct values  
- Recursive functions (sum, count, max) work properly  

## Reflection Questions

1. What happens if you forget the base case?  
The function will run forever and cause a recursion error.

2. Why is naive Fibonacci inefficient?  
It repeats the same calculations many times.

3. What is the purpose of the call stack?  
It keeps track of function calls and returns values in order.

## Challenges Encountered

Understanding how recursion returns values through the call stack was confusing. Tracing each step helped me understand the process.

