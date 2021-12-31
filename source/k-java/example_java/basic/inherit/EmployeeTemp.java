public class Employee {

    private String id;
    private String name;
    private double salary;
    private LocalDate hireDay;

    /* ... */

    @Override
    public boolean equals(Object o) {
        // 快速判断；因为当两个对象有相同引用时必定是相等的
        if (this == o) {
            return true;
        }
        // 比较对象不为空且比较的对象属于同一个类时才成立
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        // 属性值比较
        Employee employee = (Employee) o;
        return Objects.equals(id, employee.id);
        /*
         * 当然不排除有特殊需求；例如子类对象比较父类对象，
         * 只要父对象拥有的属性部分相同即可判定两个对象相同, 如
        if (o instanceof Employee) {
            // 属性值比较
            Employee employee = (Employee) o;
            return Objects.equals(id, employee.id);
        } else {
            return false;
        }
         */
    }
}
