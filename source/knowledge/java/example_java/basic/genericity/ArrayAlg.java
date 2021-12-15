package genericity;

public class ArrayAlg {

    public static <T> T getMidParam(T... a) {
        return a[a.length / 2];
    }

    public static <T extends Comparable> T min(T[] a) {
        if (a == null || a.length == 0) {
            return null;
        }
        T smallest = a[0];
        for (int i = 1; i < a.length; i++) {
            if (smallest.compareTo(a[i]) > 0) {
                smallest = a[i];
            }
        }
        return smallest;
    }

    public static void main(String[] args) {
        System.out.println(ArrayAlg.<Integer>getMidParam(1, 2, 3, 4));
        System.out.println(getMidParam("a", "b", "c"));

        Integer[] num = { 1, 2, 3, 4 };
        System.out.println(min(num));

        String[] strings = { "json", "parse", "java" };
        System.out.println(min(strings));
    }
}
