# Chapter 7: Binary Trees — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 3/29/2026
- Course: COSC 2436

## Algorithm Summary

A binary search tree is a way to store numbers so they stay organized. Each node has a value, and smaller values go to the left while bigger values go to the right. This makes it easier to find things later. When I use inorder traversal, it goes left first, then the current node, then right, which prints the numbers in sorted order.

#### Binary Search Tree
- **Search Time (balanced):** O(log n)
- **Search Time (unbalanced):** O(n)
- **BST Property:** For each node, all values on the left are smaller and all values on the right are larger.

#### Traversals
| Traversal | Order | Use Case |
|-----------|-------|----------|
| Preorder  | Root, Left, Right | Copying a tree |
| Inorder   | Left, Root, Right | Getting sorted elements |
| Postorder | Left, Right, Root | Deleting a tree |

## Test Results

Program runs correctly:
- Inorder traversal prints: [1, 3, 5, 7, 8, 9, 10]  
- Searching for 5 → True  
- Searching for 11 → False  

## Reflection Questions

1. Why does inorder traversal give sorted output?  
Inorder traversal visits nodes in ascending order because it processes left subtree, then the node, then the right subtree.

2. When would a BST become unbalanced?  
When values are inserted in sorted order, making it act like a linked list.

3. What's the difference between BFS and DFS for trees?  
BFS explores level by level using a queue, while DFS goes deep into one branch using recursion or a stack.

## Challenges Encountered

Understanding how recursion works in tree traversal was confusing at first. Tracing each step helped me understand the order nodes are visited.