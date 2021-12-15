public class Staff {
    private String id;
    private String name;
    private double salary;
    private LocalDate hireDay;

    public Staff(String id, String name, double salary, int year, int month, int day) {
        this.id = id;
        this.name = name;
        this.salary = salary;
        hireDay = LocalDate.of(year, month, day);
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public LocalDate getHireDay() {
        return hireDay;
    }

    public void raiseSalary(double byPercent) {
        double raise = salary * byPercent / 100;
        salary += raise;
    }

    @Override
    public boolean equals(Object o) {
        // 快速判断；因为当两个对象有相同引用时必定是相等的
        if (this == o) {
            return true;
        }
        if (o == null) {
            return false;
        }
        // 特殊需求；只要 id 相同即可判定两个对象相同
        if (o instanceof Employee) {
            // 属性值比较
            Employee employee = (Employee) o;
            return Objects.equals(id, employee.getId());
        } else {
            return false;
        }
    }
}
