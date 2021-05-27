# Arrays

Used to store a list of items. These items get stored sequentially in memory.

# Runtime of Operations

LookUp : O(1)

# Limitations
Arrays are static. we need to specify a size at the time of allocation. This size cannot change.

what if we dont know?
if we set a large size we end up wasting memory
if we set a smaller size, the array gets filled up quickly

To add another time, we need to resize.
This is done by allocae a larer array and copy all the items of the previous array into the new one. This is very costly.

Insertion at this pont will be O(1)
best case will be when our array is not full, so we just put an item at the next available index.
worst case scenario: when array is full, we have to create a new array and copy the items of the old array into the new one.Ano

removing an item
best case scenario : look it up by its index and clear its memory O(1)
worst case scenario : removing from the beginig. after clearing the item, we neeed to shift items to the left to fill in the hole. this takes O(n)

because array have a fixed size, in situations where we dont know how many items, or we need to add/remove large or remove a lot items,they dont perform well.

In that case we can use dynamic arrays (Vector and ArrayList in Java) or LinkedLists.

Arrays in Java
```java
```
