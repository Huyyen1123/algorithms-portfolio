# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 05/04/2026
- Course: COSC 2436

## Algorithm Summary

In this lab, I used dynamic programming to solve the knapsack problem. The idea is to break the problem into smaller subproblems and store the results in a table. This avoids repeating the same calculations and makes the solution more efficient. The grid helps track the best combination of items for each weight.

## Test Results

Program runs successfully:
- Grid is built correctly  
- Subproblems are solved step by step  
- Best combination of items is selected  
- Final values are calculated correctly  

## Reflection Questions

1. What is dynamic programming?  
It is a method that solves problems by breaking them into smaller parts and storing results to avoid repeating work.

2. How is it different from greedy algorithms?  
Dynamic programming checks all possible combinations, while greedy only makes the best choice at each step.

3. Why is it more efficient than brute force?  
Because it saves previous results and does not recompute the same subproblems again.

## Challenges Encountered

Understanding how the grid stores solutions was confusing at first. I had to trace how each row builds on the previous one to see how the final answer is formed.