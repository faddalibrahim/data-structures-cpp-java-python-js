# LinkedLists

- Used to store a list of items in sequence. Unlike arrays, LinkedLists grow and shrink automatically.
- Consist of a group of nodes in sequence. Each node holds two pieces of data -- value and address of the next node in the list.
- First node : Head
- Last node : Tail
- CS Applications: implement stack, queue, deque, adjacency list representation of graphs, dynamic memory allocation
- SWE Applications: Image Viewers, Music Playlist, Previous and Next Pages in browsers

# Runtime of Operations

## LookUp

- **By value (Search)**: The linkedlist must be traversed while simultaneously comparing with the value at each node till the value being searched for is matched. **O(n)**

- **By index (Access)** : Unlike arrays, linked lists nodes may not be together in memory. Thats why each node keeps a reference to the next node. Accessing an item by its index is **O(n)** since the traversal has to be done.

## Insertion

- **At the end** : Create a new node and have the tail point to it and set the tail to reference this new node **O(1)**

- **At the beginning**: Create a new node, link it to the head and change the head to point to this new node : **O(1)**

- **In the middle** (say after the 10th node) : we have to traverse to the 10th node and update the links **O(n)**

## Deletion

- **From the beginning**: Set the head to point to the second node, remove the link from the previous head so that it doesn't reference the second node (now the head) anymore **O(1)**
- **From the end** : Traverse the list all the way to the penultimate item, then unlink it from the tail and finally have the tail point to the penultimate node. **O(n)**
- **From the middle** : Traverse to the node as well as get its preceeding node. Link the preceding node to the node after our target node. Then remove the links surrounding the target node. **O(n)**

# Limitations

extra memory to store next node

# Overcoming Limitations

.

### Todo

| Operations       | Array | LinkedList                  | Dynamic Array |
| ---------------- | ----- | --------------------------- | ------------- |
| Lookup By Index  | O(1)  | O(n)                        | O(1)          |
| Lookup By value  | O(n)  | O(n)                        | O(n)          |
| Insert(begining) | O(n)  | O(1)                        | O(n)          |
| Insert (middle)  | O(n)  | O(n)                        | O(n)          |
| Insert(end)      | O(n)  | O(1)                        | O(n)          |
| Delete(begining) | O(n)  | O(1)                        | O(n)          |
| Delete(middle)   | O(n)  | O(n)                        | O(n)          |
| Delete(end)      | O(1)  | O(n) , O(1) if doublylinked | O(n)          |

With doubly-linkedlists, deleting an item from the end would be O(1). Since the last item has reference to the penultimate, there is no need to traverse sequentially to find the penultimate item.

This comes with the cost of an extra memory to hold the address of the previous node. This can be negligible for the performance gain when removing an item from the end

> the linked list class in java is an implementation of doubly linked list
