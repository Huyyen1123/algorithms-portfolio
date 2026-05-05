# Chapter 5: Hash Tables — Lab Report

## Student Information

- **Name:** Huy Nguyen
- **Date:** 2/25/2026
- Course: COSC 2436

## Algorithm Summary

A hash table stores keys and values in a list. A hash function changes a key into a number, and that number tells us where to put the value in the list. Sometimes two keys go to the same spot, which is called a collision. To fix this, we move to the next spot until we find an empty one. This is called linear probing. In this lab, I learned how to create the table, insert values, search for values, and handle collisions step by step.

## Test Results

Program runs successfully:
- apple → 100  
- banana → 200  
- orange → 300  
- grape → None  

## Reflection Questions

1. Why are hash tables useful?  
Hash tables allow fast insertion and lookup, usually in O(1) time.

2. How does the hash function affect performance?  
A good hash function spreads keys evenly. Poor distribution causes more collisions and slower performance.

3. What are other ways to handle collisions?  
Chaining, quadratic probing, and double hashing.


## Challenges Encountered

Understanding how linear probing works during collisions was challenging. Tracing the code step by step helped clarify how the algorithm moves through the table.