package other.stream;

import java.util.Arrays;
import java.util.List;

public class DoubleColon {
    public static void main(String[] args) {
        String[] names = { "eugene", "forest", "jackson" };
        List<String> nameList = Arrays.asList(names);
        nameList.forEach(ele -> DoubleColon.showPersonInfo(ele)); // 输出一
        nameList.forEach(DoubleColon::showPersonInfo); // 输出二
    }

    public static void showPersonInfo(String info) {
        System.out.print(info);
    }
}
