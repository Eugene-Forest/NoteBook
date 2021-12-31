package other.stream;

import java.util.List;
import java.util.Arrays;

public class DStreamSorted {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(3, 2, 2, 3, 7, 3, 5);
        // 获取对应的平方数
        numbers.stream().map(i -> i * i).distinct().sorted().forEach(System.out::println);
    }
}
