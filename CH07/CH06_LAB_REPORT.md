# Chapter 7: Binary Trees — Lab Report


## Student Information
- **Name:** Huy Nguyen
- **Date:** 3/29/2026
- Course: COSC 2436

## Algorithm Summary

A binary search tree is a way to store numbers so they stay organized. Each node has a value, and smaller values go to the left while bigger values go to the right. This makes it easier to find things later. When I use inorder traversal, it goes left first, then the current node, then right, which ends up printing the numbers in sorted order.

## Test Results

Program runs correctly:
- Inorder traversal prints: [1, 3, 5, 7, 8, 9, 10]  
- Searching for 5 → True  
- Searching for 11 → False  

#### Binary Search Tree
- **Search Time (balanced):** O(log n)
- **Search Time (unbalanced):** O(n)
- **BST Property:** A binary search tree maintains the property that for each node, all elements in the left subtree are less, and all elements in the right subtree are greater.

#### Traversals
| Traversal | Order | Use Case |
|-----------|-------|----------|
| Preorder  | Root, Left, Right | Copying a tree |
| Inorder   | Left, Root, Right | Getting sorted elements |
| Postorder | Left, Right, Root | Deleting a tree |

### Reflection Questions

1. Why does inorder traversal give sorted output?
In order traversal visits nodes in ascending order for a binary search tree, as it processes the left subtree, then the node, and finally the right subtree.

2. When would a BST become unbalanced?
A BST becomes unbalanced when nodes are inserted in a sorted order, leading to a linear structure similar to a linked list.

3. What's the difference between BFS and DFS for trees?
BFS explores nodes level by level using a queue, while DFS explores as deep as possible along each branch before backtracking, typically using recursion or a stack.

## Challenges Encountered

Understanding how recursion works in tree traversal was confusing at first. I had to trace each step to see the order nodes were visited.