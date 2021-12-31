package other.stream;

import java.util.Arrays;
import java.util.List;

public class DStreamFilter {
    public static void main(String[] args) {

        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd", "", "jkl");
        // 获取空字符串的数量
        long count = strings.stream().filter(string -> string.isEmpty()).count();
        // (stream.) count() : Returns the count of elements in this stream.
        // (stream.) filter() : Returns a stream consisting of the elements of this
        // stream that match the given predicate.
        System.out.println("**" + count);

    }
}
