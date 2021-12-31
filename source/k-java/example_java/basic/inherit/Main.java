public class Main {
    public static void main(String[] args) {
        Employee eugene = new Employee("1244", "eugene", 2000, 2021, 8, 10);
        Manager forest = new Manager("1244", "eugene forest", 2000, 2021, 8, 10);
        forest.setBonus(5000);
        Staff staff = new Staff("1244", "eugene_forest", 2000, 2021, 8, 10);
        if (forest.equals(eugene) && eugene.equals(forest)) {
            System.out.println("forest and eugene");
        }
        if (staff.equals(eugene) && staff.equals(forest)) {
            System.out.println("equal");
        }
        if (eugene.equals(staff) || forest.equals(staff)) {
            System.out.println("eugene or forest equal staff");
        } else {
            System.out.println("eugene and forest not equal staff");
        }
    }
}

// result code
/*
forest and eugene
equal
eugene and forest not equal staff
*/