package soundsystem;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class CDPlayerConfig {

  @Bean
  public CompactDisc compactDisc() {
    return new SgtPeppers();
  }

  @Bean
  public CDPlayer cdPlayer(CompactDisc compactDisc) {
    // 实现了依赖注入
    return new CDPlayer(compactDisc); // recommend
    // return new CDPlayer(compactDisc()); //way 2
  }

}
