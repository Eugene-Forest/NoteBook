public class TestMain {

    /**
     * 自定义的日志记录器，一般情况下初始记录等级与全局logger相同
     * 除非配置文件中有同名的自定义记录器配置
     */
    public static final Logger customizeLogger= Logger.getLogger("core.base.log");

    public static void main(String[] args) {
        List<String> list= Arrays.asList("12443039","eugene-forest");
        //测试全局记录器
        Logger.getGlobal().info("---global--");
        run(list,Logger.getGlobal());
        //测试自定义记录器
        customizeLogger.info("---custom--");
        run(list,customizeLogger);
    }

    public static void run(List<String> strings,Logger logger){
        strings.stream().map(x->x+"@qq.com").collect(Collectors.toList()).forEach(logger::config);
        logger.fine("fine logger");
        logger.info("finish function!");
    }

    /**
     * run code result without config :
     *
     * 十一月 29, 2021 4:52:10 下午 core.base.log.TestMain main
     * 信息: ---global--
     * 十一月 29, 2021 4:52:10 下午 core.base.log.TestMain run
     * 信息: finish function!
     * 十一月 29, 2021 4:52:10 下午 core.base.log.TestMain main
     * 信息: ---custom--
     * 十一月 29, 2021 4:52:10 下午 core.base.log.TestMain run
     * 信息: finish function!
     */

    /**
     * run code result with customize config : java -Djava.util.logging.config.file=path MyApp
     *
     * 十一月 29, 2021 4:54:30 下午 core.base.log.TestMain main
     * 信息: ---global--
     * 十一月 29, 2021 4:54:30 下午 java.util.ArrayList forEach
     * 配置: 12443039@qq.com
     * 十一月 29, 2021 4:54:30 下午 java.util.ArrayList forEach
     * 配置: eugene-forest@qq.com
     * 十一月 29, 2021 4:54:30 下午 core.base.log.TestMain run
     * 信息: finish function!
     * 十一月 29, 2021 4:54:30 下午 core.base.log.TestMain main
     * 信息: ---custom--
     * 十一月 29, 2021 4:54:30 下午 java.util.ArrayList forEach
     * 配置: 12443039@qq.com
     * 十一月 29, 2021 4:54:30 下午 java.util.ArrayList forEach
     * 配置: eugene-forest@qq.com
     * 十一月 29, 2021 4:54:30 下午 core.base.log.TestMain run
     * 详细: fine logger
     * 十一月 29, 2021 4:54:30 下午 core.base.log.TestMain run
     * 信息: finish function!
     */
}
