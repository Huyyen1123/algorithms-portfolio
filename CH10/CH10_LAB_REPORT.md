# Chapter 10: Greedy Algorithm (Truck Packing) — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 05/04/2026
- Course: COSC 2436

## Algorithm Summary

In this lab, I used a greedy algorithm to pack boxes into a truck. The idea is to always choose the largest box first and keep adding boxes as long as they fit. The algorithm does not try every possible combination. Instead, it makes the best choice at each step, which makes it fast but not always perfect.

## Test Results

Program runs successfully:
- Boxes are sorted by volume  
- Larger boxes are selected first  
- Total volume does not exceed the truck capacity  
- Output correctly shows packed boxes  

## Reflection Questions

1. What is a greedy algorithm?  
A greedy algorithm makes the best choice at each step without looking ahead at future choices.

2. Does greedy always give the best solution?  
No, it does not always give the optimal solution. It works well for some problems but can fail for others.

3. Why does greedy work for this problem?  
It works because choosing larger boxes first helps fill the truck space efficiently in most cases.

## Challenges Encountered

One challenge was understanding why greedy does not always give the best answer. After testing different inputs, I saw that sometimes a different combination of smaller boxes could give a better result.
