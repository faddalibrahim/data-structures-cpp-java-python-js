# Arrays

Used to store a list of items sequentially in memory

# Runtime of Operations

## LookUp : O(1)  

## Insertion : O(n)

**Best Case** : When the array is not full and so the item is inserted at the next available index  

**Worst Case 1**: When the array is full and we have to create a large array, copying the contents of the previous array into the new one in the process.

**Worst Case 2**: When we have to insert at the beginning. We have to shift the other items to the right to make space for the item to be inserted.

## Removal : O(n)

**Best Case** : If the item is at the end, its memory is cleared
**Worst Case** : If the item to be removed is the beginning. The rest of the items need to be shifted to the left to fill the hole created.


# Limitations

Arrays are static. we need to specify a size at the time of allocation. This size cannot change.

If we dont know the size ahead of time and we set a large size, we might end up wasting memory.
if we set a smaller size, the array gets filled up quickly and we have to create a new larger array if we want to add more items. Additionally we have to transfer the items from the previous array into the new one.

To add another time, we need to resize.
This is done by allocae a larer array and copy all the items of the previous array into the new one. This is very costly.



# Other Options
because array have a fixed size, in situations where we dont know how many items, or we need to add/remove large or remove a lot items,they dont perform well.

In that case we can use dynamic arrays (Vector and ArrayList in Java) or LinkedLists.

Arrays in Java
```java
```
