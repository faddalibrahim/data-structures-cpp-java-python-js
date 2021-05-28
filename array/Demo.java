package array;

public class Demo {
    public static void main(String[] args) {
        DynamicArray da = new DynamicArray(3);
        da.insert(5);
        da.insert(10);
        da.insert(1);
        da.print();
    }
}
