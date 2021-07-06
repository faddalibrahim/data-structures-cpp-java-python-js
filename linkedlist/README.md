# LinkedLists

- Used to store a list of items in sequence. Unlike arrays, LinkedLists can grow and shrink automatically.  
- Consist of a group of nodes in sequence. Each node holds two pieces of data -- value and address of the next node in the list.
- First node : Head  
- Last node : Tail


# Runtime of Operations

## LookUp : O(n)

- **By value**: The linkedlist must be traversed while simultaneously comparing with the value at each node till the value being searched for is matched.

- **By index** : Unlike arrays, linked lists nodes may not be together in memory. Thats why each node keeps a reference to the next node. Looking up an item by its index is still O(n) since the traversal has to take place.

## Insertion : O(1) / O(n)

- **At the end** : Create a new node and have the tail point to it and set the tail to reference this new node **O(1)**

- **At the beginning**: Create a new node, link it to the head and change the head to point to this new node : **O(1)**

- **In the middle** (say after the 10th node) : we have to traverse to the 10th node and update the links **O(n)**

## Removal/Deletion : O(1) / O(n)

- **From the beginning**: Set the head to point to the second node, remove the link from the previous head so that it doesn't reference the second node (now the head) anymore **O(1)**
- **From the end** : Traverse the list all the way to the penultimate item, then unlink it from the tail and finally have the tail point to the penultimate node. **O(n)**
- **From the middle** : Traverse to the node as well as get its preceeding node. Link the preceding node to the node after our target node. Then remove the links surrounding the target node. **O(n)**



# Limitations
extra memory to store next node



# Overcoming Limitations

.

### Todo



Operations | Arrays | LinkedLists |
| --- | --- | --- |
| Lookup By Index | O(1) | O(n)  
| Lookup By value | O(n) | O(n)  
| Insert(begining/end) | O(n) | O(1)
| Insert (middle) | O(n) | O(n)
| Delete(begining) | O(n) | O(1)
| Delete(middle) | O(n) | O(n)
| Delete(end) | O(n) | O(n)