public class LogMain {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("assert", "logger", "interface", "debug");
        LogTest logTest = new LogTest();
        logTest.run(list);
        // Logger.getGlobal().setLevel(Level.OFF); 语句可以关闭所有日志
        Logger.getGlobal().setLevel(Level.OFF);
        logTest.run(list);
    }
}

class LogTest {

    public void run(List<String> strings) {
        strings.forEach(x -> {
            // 使用全局日志记录器（global logger) 并调用其 warring 方法
            Logger.getGlobal().warning(x);
            // Logger.getGlobal().log(Level.WARNING, x);
        });
        System.out.println("finish function!");
    }

}

/*
 * code run result:
 * 
 * 十一月 29, 2021 11:08:35 上午 core.base.log.LogTest lambda$run$0
 * 警告: assert
 * 十一月 29, 2021 11:08:35 上午 core.base.log.LogTest lambda$run$0
 * 警告: logger
 * 十一月 29, 2021 11:08:35 上午 core.base.log.LogTest lambda$run$0
 * 警告: interface
 * 十一月 29, 2021 11:08:35 上午 core.base.log.LogTest lambda$run$0
 * 警告: debug
 * finish function!
 * finish function!
 */