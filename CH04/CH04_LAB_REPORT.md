# Lab 04: Quicksort

## Student Information
- **Name:** Huy Nguyen
- **Date:** 2/18/2026
- Course: COSC 2436
## Algorithm Summary

Quicksort is a divide-and-conquer algorithm. It works by selecting a pivot element, then splitting the list into values smaller and greater than the pivot. Each part is sorted recursively and combined.

### The Three Steps
1. **Choose pivot:** I used the first number in the list as the pivot to compare all other values
2. **Partition:** I split the rest of the list into two groups, number less than or equal to the pivot and numbers greater than the pivot
3. **Recurse and combine:** I run quicksort again on both groups, then put them togther with the pivot in the middle

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])

Pivot = 3
less = [2,1]
greater = [5,4]

left side:
pivot = 2
less = [1]
greater = []

Right side:
pivot = 5
less = [4]
greater = []

Final result:
[1,2] + [3] + [4,5] = [1,2,3,4,5]


## Complexity Analysis

| Case    | Time Complexity | Why? |
|--------|----------------|------|
| Best   | O(n log n)     | Balanced splits |
| Average| O(n log n)     | Usually balanced |
| Worst  | O(n²)          | Very unbalanced splits |
## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
Quicksorts will keeps putting almost everything on one side. This causes many unnecessary recursive calls and make the algorithm slowers

2. How could you improve pivot selection to avoid worst-case performance?
I could chooese a random elements or take the middle value. This helps prevents uneven splits and keeps the algorithm running faster

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
Compared to bubble sort, quicksort is more effiecent for large lists. Bubble sort compares everything repeatedly, while quicksort breaks the list into smaller parts. Merge sort is more consistent in speed, but quicksort usually runs faster and uses less extra memory

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
we use array[1:] because the first element is already chosen as the pivot. Removing it prevents the pivot from being compared to itself and avoids repeating values during recursion

## Challenges Encountered

Understanding how quicksort splits the list using a pivot was challenging. I solved this by tracing each recursive step and checking how the list was divided and combined.

## Test Results

Program runs successfully and correctly sorts all test cases.