[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22692980&assignment_repo_type=AssignmentRepo)
# Lab 02: Selection Sort

## Overview
Implement selection sort and understand arrays vs linked lists.

## Learning Objectives
- Implement selection sort O(n²)
- Understand array vs linked list tradeoffs
- Analyze algorithm complexity

## Files to Complete
- `sort.py` - Implement `find_smallest()` and `selection_sort()` functions

## Instructions

### Part 1: Implement find_smallest
Find the index of the smallest element in a list starting from a given position.

### Part 2: Implement selection_sort
Use find_smallest to implement selection sort from Chapter 2.

### Part 3: Run Tests
```bash
python -m pytest tests/ -v
```

---

## Lab Report

### Student Information
- **Name:** Huy Nguyen
- **Date:** 2/21/2026

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

### Reflection Questions

1. Why is selection sort O(n²)?
Because for each position in the list, it scans the rest of the list to find the smallest (or largest).

2. When would you choose a linked list over an array?
If you need lots of insertions/deletions at the front (head) and you don’t care about fast random access by index.

3. Why does Python use arrays (lists) as the default sequence type?
Because arrays are fast for reading by index (O(1)), and most programs do a lot of reading. Python lists also resize automatically, so they’re convenient and efficient for common use.