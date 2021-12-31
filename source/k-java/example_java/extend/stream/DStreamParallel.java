package other.stream;

import java.util.Arrays;
import java.util.List;

public class DStreamParallel {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(3, 2, 2, 3, 7, 3, 5);
        // 获取对应的平方数
        numbers.parallelStream().map(i -> i * i).distinct().sorted().forEach(System.out::println);
        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd", "", "jkl");
        // 获取空字符串的数量
        long count = strings.parallelStream().filter(string -> string.isEmpty()).count();
        System.out.println("空字符串的数量:" + count);
    }
}
