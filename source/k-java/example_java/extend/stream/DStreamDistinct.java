package other.stream;

import java.util.Arrays;
import java.util.List;

public class DStreamDistinct {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd", "", "jkl", "bc");

        strings.stream().forEach(System.out::println);
        System.out.println("--");
        strings.stream().distinct().forEach(System.out::println);
        System.out.println("--");
        strings.stream().filter(ele -> !ele.isEmpty()).forEach(System.out::println);
    }
}
