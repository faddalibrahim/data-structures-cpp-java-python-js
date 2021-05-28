package array;

public class DynamicArray {
    private int[] items;
    private int count;

    public DynamicArray(int length) {
        items = new int[length];
    }

    public void print() {
        for (int i = 0; i < count; i++) {
            System.out.println(items[i]);
        }
    }

    public void insert(int item) {
        // if array is full, resize it
        if (count == items.length) {
            // create new array
            int[] newItems = new int[count * 2];

            // copy all existing items
            for (int i = 0; i < count; i++) {
                newItems[i] = items[i];
            }

            // set items to new array
            items = newItems;
        }

        // add the new item at the end
        items[count++] = item;
    }

    public void removeAt(int index) {
        // validate index
        if (index < 0 || index >= count) {
            throw new IllegalArgumentException();
        }

        // Shift items to the left to fill the hole
    }

}