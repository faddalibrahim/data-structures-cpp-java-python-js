/**
 * 
 * singly linkedlist implementation in java
 */

package linkedlist.singly.java;

import java.util.NoSuchElementException;

/**
 * 
 * @author faddalibrahim
 * @version 1.0
 * @since 1.0 class: LinkedList
 */
public class LinkedList {
    /**
     * Represents the head of the linkedlist
     */
    private Node head;

    /**
     * Returns the tail of the linkedlist
     */
    private Node tail;

    private int size;

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

        size++;
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

        size++;
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

    public void removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        if (head == tail) {
            head = tail = null;
            size = 0;
            return;
        }

        Node second = head.next;
        head.next = null;
        head = second;

        size--;
    }

    public void removeLast() {

        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        // if there is only one item
        if (head == tail) {
            head = tail = null;
            size = 0;
            return;
        }

        Node previous = getPrevious(tail);
        tail = previous;
        tail.next = null;

        size--;
    }

    private Node getPrevious(Node node) {
        Node currentNode = head;
        while (currentNode.next != null) {
            if (currentNode.next == node)
                return currentNode;
            currentNode = currentNode.next;
        }
        return null;
    }

    public int size() {
        return size;
    }

    public int[] toArray() {
        int[] array = new int[size];
        Node currentNode = head;
        int index = 0;
        while (currentNode != null) {
            array[index++] = currentNode.value;
            currentNode = currentNode.next;
        }
        return array;
    }
    // deleteFirst
    // deleteLast
    // contains
}