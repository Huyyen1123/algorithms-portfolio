"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    cities = load_cities('data/cities.json')
    print(f"Loaded {len(cities)} cities\n")

    
    print("=" * 60)
    print("PART 1: SELECTION SORT")
    print("=" * 60)

    print("\nSorting cities by population (smallest first)...")
    sorted_asc = selection_sort(cities, key=lambda x: x['population'])

    print("\nTop 5 smallest cities:")
    for city in sorted_asc[:5]:
        print(f"  {city['name']}: {city['population']:,}")

    print("\nSorting cities by population (largest first)...")
    sorted_desc = selection_sort(cities, key=lambda x: x['population'], reverse=True)

    print("\nTop 5 largest cities:")
    for city in sorted_desc[:5]:
        print(f"  {city['name']}: {city['population']:,}")

    print("\n" + "-" * 40)
    print("Comparison with Python's built-in sort:")
    python_builtin_sort(cities, key=lambda x: x['population'])
    
    
    print("\n" + "=" * 60)
    print("PART 2: ARRAY VS LINKED LIST")
    print("=" * 60)

    print("\n--- Python List (Array) Operations ---")

    city_names = [c['name'] for c in cities]

    start = time.time()
    middle_city = city_names[len(city_names) // 2]
    elapsed = (time.time() - start) * 1000000
    print(f"Array access by index: '{middle_city}' - O(1) - {elapsed:.2f} µs")

    start = time.time()
    city_names_copy = city_names.copy()
    city_names_copy.insert(0, "New City")
    elapsed = (time.time() - start) * 1000000
    print(f"Array insert at beginning: O(n) - {elapsed:.2f} µs")

    print("\n--- Linked List Operations ---")

    linked_cities = LinkedList()
    for city in cities:
        linked_cities.insert_at_tail(city)

    print(f"Created linked list with {len(linked_cities)} cities")

    start = time.time()
    linked_cities.insert_at_head({"name": "New City", "population": 0})
    elapsed = (time.time() - start) * 1000000
    print(f"LinkedList insert at head: O(1) - {elapsed:.2f} µs")

    print("\nSearching for 'Dallas' in linked list...")
    linked_cities.search("Dallas", key=lambda x: x['name'])
    
    
    print("\n" + "=" * 60)
    print("PART 3: BIG O SUMMARY")
    print("=" * 60)

    print("""
Selection Sort: O(n²)
Python's Timsort: O(n log n)

Array vs Linked List:
- Read: Array O(1), Linked List O(n)
- Insert: Array O(n), Linked List O(1) at head
- Delete: Array O(n), Linked List O(1) at head
""")

if __name__ == "__main__":
    main()
