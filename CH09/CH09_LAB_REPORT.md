# Chapter 9: Dijkstra’s Algorithm — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 05/04/2026
- Course: COSC 2436

## Algorithm Summary

Dijkstra’s algorithm finds the shortest path in a weighted graph. It starts from a source node and always selects the node with the smallest distance. Then it updates the distances of its neighbors. This continues until the shortest path to all nodes is found.

## Test Results

Program runs successfully:
- Shortest path is calculated correctly  
- Distances update properly  
- Algorithm finds optimal path  

## Reflection Questions

1. What problem does Dijkstra solve?  
It finds the shortest path between nodes in a weighted graph.

2. Why does it pick the smallest distance first?  
Because it ensures the path is optimal and avoids longer paths.

3. What is a limitation of Dijkstra’s algorithm?  
It does not work with negative edge weights.

## Challenges Encountered

Understanding how distances update step by step was difficult at first. Tracing the algorithm helped me understand how it finds the shortest path.

