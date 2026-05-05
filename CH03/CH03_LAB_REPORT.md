# Chapter 3: Recursion — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 05/04/2026
- Course: COSC 2436

## Algorithm Summary

Recursion is a technique where a function calls itself to solve smaller parts of a problem. Every recursive function has a base case and a recursive case. The base case stops the recursion, while the recursive case reduces the problem into smaller subproblems.

### Two Parts of Every Recursive Function
1. **Base Case:** The base case is the stopping condition. It is the simplest version of the problem. Without it, the function would keep calling itself forever and crash.
2. **Recursive Case:** The recursive case is when the function calls itself with a smaller input. Each call moves closer to the base case.

### The Call Stack
When a recursive function runs, each call is placed on the call stack. The computer pauses the current call and waits for the smaller call to finish.

For example, `fact(4)` works like this:

fact(4)  
→ 4 × fact(3)  
→ 3 × fact(2)  
→ 2 × fact(1)  
→ return 1 (base case reached)  
→ return 2  
→ return 6  
→ return 24  

The function goes down until it hits the base case, then it comes back up multiplying the results.

## Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|-----------|----------------|-----------------|
| countdown | i <= 0 | countdown(i-1) | O(n) |
| fact | x <= 1 | x * fact(x-1) | O(n) |
| recursive_sum | empty list | first + sum(rest) | O(n) |
| recursive_count | empty list | 1 + count(rest) | O(n) |
| recursive_max | single item | max(first, max(rest)) | O(n) |

## Test Results

Program correctly executes recursive functions:
- Countdown prints values until reaching the base case  
- Factorial returns correct values  
- Recursive sum, count, and max functions work correctly  

## Reflection Questions

1. **What happens if you forget the base case?**  
The function will keep calling itself infinitely and eventually cause a recursion error due to stack overflow.

2. **Why is the naive Fibonacci implementation inefficient?**  
Because it repeats the same calculations multiple times, making it very slow for larger inputs.

3. **What is the purpose of the call stack in recursion?**  
The call stack keeps track of each function call and returns values back in the correct order once the base case is reached.

## Challenges Encountered

One challenge was understanding how recursive calls return values through the call stack. I solved this by tracing each step manually and testing small inputs to see how the function behaves.

