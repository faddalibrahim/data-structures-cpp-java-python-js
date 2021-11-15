package queue.java;

public class ArrayQueue {
    private int[] items;
    private int count;

    private int front;
    private int rear;

    public ArrayQueue(int capacity) {
        items = new int[capacity];
    }

    public static void main(String[] args) {

    }
    
    public void enqueue(int item) {
        if (count == items.length) {
            throw new IllegalStateException();
        }
        items[rear] = item;
        rear = (rear + 1) % items.length;
        count++;
    }

    public int dequeue() {
        if (count == 0) {
            throw new IllegalStateException();
        }
        var item = items[front];
        items[front] = 0;
        front = (front + 1) % items.length;
        count--;

        return item;
    }

    public int peek() {
        if (count == 0) {
            throw new IllegalStateException();
        }
        return items[rear];
    }

    public boolean isEmpty() {
        return items.length == 0;
    }
}
