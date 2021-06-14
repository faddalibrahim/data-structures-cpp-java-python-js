package linkedlist.singly.java;

public class LinkedList {
    private Node head;
    private Node tail;

    private class Node {
        private int value;
        private Node next;

        public Node(int value) {
            this.value = value;
        }
    }

    public void addLast(int newItem) {
        Node node = new Node(newItem);

        if (head == null) {
            head = tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
    }
    // addFirst
    // addLast
    // deleteFirst
    // deleteLast
    // contains
    // indexOf
}