package other.stream;

import java.util.Random;

public class DStream {

    public static void main(String[] args) {
        Random random = new Random();
        random.ints().limit(10).forEach(System.out::println);
        // ints() : 返回一个有效的无限流的伪 int值。
        // (stream.)limit(int maxSize) : 返回由该流的元素组成的流，截断后的长度不超过maxSize。
    }

}
