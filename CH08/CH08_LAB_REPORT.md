# Chapter 8: Balanced Trees — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 4/4/2026
- Course: COSC 2436

## Algorithm Summary

An AVL tree is a self-balancing binary search tree. After inserting a value, the tree checks if it is balanced by comparing the height of the left and right sides. If it becomes unbalanced, rotations are used to fix it. This keeps the tree height small so operations stay fast.


#### AVL Trees
- **Balance Factor Range:** -1, 0, 1
- **Why rebalance?** If the tree gets uneven, it slows down a lot, so rebalance keeps it fast.
- **Time Complexity (all operations):** O(log n)

#### Rotation Cases
| Case | Imbalance                           | Fix                               |
|------|-------------------------------------|-----------------------------------|
| LL   |   Too heavy on the left side        | Rotate right                      |
| RR   |   Too heavy on the right side       | Rotate left                       |
| LR   |   Left side, but leaning right      | Left rotate, then right rotate    |
| RL   |   Right side, but leaning left      | Right rotate, then left rotate    |

## Test Results

Program runs successfully:
- Tree remains balanced after insertions  
- Rotations are applied when needed  
- Inorder traversal returns sorted values  

## Reflection Questions

1. Why is an unbalanced BST bad?
If the tree becomes unbalanced, it can turn into a straight line. This makes operations like search and insert slow (O(n)) instead of fast.

2. How do rotations maintain the BST property?
Rotations only move nodes around without changing their order. Smaller values stay on the left and bigger values stay on the right.

3. What other self-balancing trees exist?
Red Black Trees, Splay Trees, and B-Trees.

## Challenges Encountered

Understanding how rotations work was confusing at first. I had to visualize how nodes move during rotations to understand how the tree stays balanced.
