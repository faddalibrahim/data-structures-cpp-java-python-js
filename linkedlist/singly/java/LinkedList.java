/**
 * 
 * singly linkedlist implementation in java
 */

package linkedlist.singly.java;

/**
 * 
 * @author faddalibrahim
 * 
 *         class: LinkedList
 * 
 *         Accessibility Modifier: public
 */
public class LinkedList {
    private Node head;
    private Node tail;

    private class Node {
        private int value;
        private Node next;

        /**
         * Constructor
         * 
         * @param value
         */
        public Node(int value) {
            this.value = value;
        }
    }

    /**
     * Appends an item to the linkedlist
     * 
     * @param newItem the item to be appended
     */
    public void addLast(int newItem) {
        Node node = new Node(newItem);

        if (isEmpty()) {
            head = tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
    }

    /**
     * Prepends an item to the linkedlist
     * 
     * @param newItem the item to be prepended
     */
    public void addFirst(int newItem) {
        Node node = new Node(newItem);

        if (isEmpty()) {
            head = tail = node;
        } else {
            node.next = head;
            head = node;
        }
    }

    /**
     * Method to check if linkedlist is empty
     * 
     * @return either true if head is null, otherwise false
     */
    private boolean isEmpty() {
        return head == null;
    }

    /**
     * Returns the index of an item in the linkedlist
     * 
     * @param item The time whose index we are looking for
     * @return the index of the item. value is -1 if item was not found
     */
    public int indexOf(int item) {
        Node currentNode = head;
        int index = 0;
        while (currentNode != null) {
            if (currentNode.value == item)
                return index;
            currentNode = currentNode.next;
            index++;
        }
        return -1;
    }

    /**
     * Checks if an item exists in the linkedlist
     * 
     * @param item The item to be searched for
     * @return true if item was found, false otherwise
     */
    public boolean contains(int item) {

        return indexOf(item) != -1;
    }
    // deleteFirst
    // deleteLast
    // contains
}