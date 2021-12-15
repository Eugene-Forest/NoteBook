@Configuration
@EnableSwagger
@AllArgsConstructor
public class SwaggerConfiguration {

    /**
     * 引入swagger配置类
     */
    private final SwaggerProperties swaggerProperties;

    /**
     * 引入Knife4j扩展类
     */
    private final OpenApiExtensionResolver openApiExtensionResolver;

    @Bean
    @Profile({ "dev", "test" })
    public Docket testDocket() {
        return docket("module_name", Collections.singletonList("path"));
    }

    /**
     * 模块的基本配置
     *
     * @param groupName    模块名
     * @param basePackages 模块包的根目录
     */
    private Docket docket(String groupName, List<String> basePackages) {
        // ......
    }

    /**
     * swagger 文档主页的基本信息的配置，相关配置可以在项目运行配置文件中修改
     */
    private ApiInfo apiInfo() {
        // ......
    }
}