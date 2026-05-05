# Chapter 2: Selection Sort — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 2/21/2026
- Course: COSC 2436

## Algorithm Summary

Selection sort is a simple sorting algorithm that works by repeatedly finding the smallest element in a list and placing it at the front. It scans the remaining unsorted part of the list each time and swaps the smallest value into the correct position. This process continues until the entire list is sorted.

#### Selection Sort
- **Time Complexity:** O(n²)
- **How it works:** The algorithm goes through the list, finds the smallest value, and swaps it into place. Then it repeats this process for the rest of the list.

#### Arrays vs Linked Lists

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        | Array can access any index directly, while linked lists must traverse node by node. |
| Insert    | O(n)  | O(1)*       | Arrays may shift elements, while linked lists just update pointers. |
| Delete    | O(n)  | O(1)*       | Arrays shift elements after deletion, linked lists adjust pointers. |

## Test Results

Program runs successfully:
- Selection Sort performs correctly  
- Comparisons and swaps are counted  
- Smallest and largest cities are printed correctly  

## Reflection Questions

1. Why is selection sort O(n²)?  
Because it loops through the list and for each position, it scans the remaining elements to find the smallest value.

2. When would you choose a linked list over an array?  
When you need fast insertions and deletions and do not need fast random access.

3. Why does Python use arrays (lists) as the default sequence type?  
Because arrays allow fast access by index and are efficient for most use cases.

## Challenges Encountered

Understanding how selection sort repeatedly finds the smallest value was challenging at first. Tracing the algorithm step by step helped me understand how it works.