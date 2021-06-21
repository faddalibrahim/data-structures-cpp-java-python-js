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
     * appends an item to the linkedlist
     * 
     * @param newItem
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
     * prepends an item to the linkedlist
     * 
     * @param newItem
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
     * helper function to check if linkedlist is empty
     * 
     * @return either true or false depending on if the head is null
     */
    private boolean isEmpty() {
        return head == null;
    }

    public int indexOf(int item) {

    }
    // addFirst
    // addLast
    // deleteFirst
    // deleteLast
    // contains
    // indexOf
}