# Lab 06: 2436 Ch06

## Student Information
- **Name:** Huy Nguyen
- **Date:** 3/4/2026
- Course: COSC 2436

## Algorithm Summary

In this lab I learned about graphs and the Breadth First Search (BFS) algorithm. A graph has nodes and edges. In this lab the nodes are cities in Texas and the edges are the roads between them. The graph was stored using an adjacency list. BFS uses a queue to visit cities level by level. This helps find the shortest path between two cities.

## Test Results

Program runs successfully:
- Correct shortest path between cities  
- Distances from starting city calculated correctly  
- BFS traversal works as expected  

## Reflection Questions

1. BFS uses a queue so cities are checked in the order they are found. This makes the search go level by level.

2. BFS finds the shortest path by number of edges. It does not look at real distance or weight.

3. BFS is used when we want the shortest path in an unweighted graph. DFS is used when we want to explore deeper paths first.

## Challenges Encountered

One challenge was fixing indentation errors in the loop. Once corrected, the BFS traversal worked as expected.