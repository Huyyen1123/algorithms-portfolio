# Lab 02: Selection Sort - Lab Report

### Student Information
- **Name:** Huy Nguyen
- **Date:** 2/21/2026
- Course: COSC 2436

### Algorithm Analysis

#### Selection Sort
- **Time Complexity:** O(n^2)
- **How it works:** Selection sort goes through the list and finds the smallest item, then swaps it into the first position.
  Then, it finds the smallest item in the remaining unsorted part and swaps it into the next position.
  It repeats until the whole list is sorted.

#### Arrays vs Linked Lists

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        | Array can jump to an index instantly. Linked list must walk node-by-node to reach an index. |
| Insert    | O(n)  | O(1)*       | Array may need to shift many items to make space. Linked list can change pointers quickly once you’re at the spot. |
| Delete    | O(n)  | O(1)*       | Array may need to shift items after removing. Linked list can bypass a node by changing pointers once you’re at the spot. |

## Test Results

Program output (example):

- Selection Sort: 190 comparisons, 10 swaps  
- Top 5 smallest cities printed correctly  
- Top 5 largest cities printed correctly

### Reflection Questions

1. Why is selection sort O(n²)?
Because for each position in the list, it scans the rest of the list to find the smallest (or largest).

2. When would you choose a linked list over an array?
If you need lots of insertions/deletions at the front (head) and you don’t care about fast random access by index.

3. Why does Python use arrays (lists) as the default sequence type?
Because arrays are fast for reading by index (O(1)), and most programs do a lot of reading. Python lists also resize automatically, so they’re convenient and efficient for common use.

## Challenges Encountered

One challenge was understanding how selection sort repeatedly finds the smallest value. I solved this by tracing the algorithm step by step and testing with small inputs.