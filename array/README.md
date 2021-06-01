# Arrays

Used to store a list of items (strings, numbers, objects etc) sequentially in memory

# Runtime of Operations

## LookUp : O(1) / O(n)

- Given its index, calculation of the memory address of an item in an array is fast and straight forward. Its retrieval occurs at constant time.
- If we are looking up an item by value, its O(n) because in the worst case, the item could be at the end of the array. Hence, traversing all the way to the end to find it.

## Insertion : O(n)

- **Best Case** : When the array is not full and so the item is inserted at the end of the array. This happens in O(1)

- **Worst Case 1**: When the array is full and a larger array is created to accommodate incoming items and the subsequent copying of the contents of the previous array into the new one in the process. **Copying/Transferring items into new array happens in O(n)**

- **Worst Case 2**: Insertion at the beginnin of array. The other items are shifted to the right to make space for the new item to be inserted. This happens in O(n)

## Removal : O(n)

- **Best Case** : If the item is at the end, look it up by index and clear memory(set to null). Happens in O(1)

- **Worst Case** : If the item to be removed is in the beginning. The rest of the items need to be shifted to the left to fill the hole created. **Shifting the items to fill the hole occurs in O(n)**

# Limitations

- In many languages, arrays are static. A definite size must be specified at the time of allocation.

- If the size is not known ahead of time, a large size can be set but might end up wasting memory.

- if a smaller size is set, the array gets filled up quickly and a new larger array is allocated if more items are be to inserted. Items from the old array are also copied into the new array.

- In situations where the number of items to add is unknown or when a lot of items need to be removed, arrays won't perform well.

# Overcoming Limitations

Because arrays have a fixed size, in situations where we dont know how many items we need to add/remove or in situations where we remove a lot items, they dont perform well. Dynamic Arrays can offset this limitation but still with performance and memory issues.

Arrays are however dynamic in some programming languages like python and javascript.

Java has 2 in-built implementations of dynamic arrays:

1. Vector
   - grows by 100% of its size when it gets full size
   - all methods are synchronized (only a single thread can access that method)
2. ArrayList
   - grows by 50% of its size when it gets full size

With Linkedlists, we don't have to know ahead of time how many items we need to add/remove. Linkedlists inherently grow and shrink dynamically. Nevertheless, they have their shortcomings as well.