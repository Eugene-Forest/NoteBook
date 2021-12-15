public class Manager extends Employee {
    private double bonus;

    public Manager(String id, String name, double salary, int year, int month, int day) {
        super(id, name, salary, year, month, day);
        bonus = 0;
    }

    @Override
    public double getSalary() {
        double baseSalary = super.getSalary();
        return baseSalary + bonus;
    }

    public void setBonus(double b) {
        bonus = b;
    }
}