package genericity;

public class ExtendsTest {

    public static void main(String[] args) {
        Manager manager1 = new Manager("name", 11, "nan", "office");
        Manager manager2 = new Manager("eugene", 22, "gender", "ffa");
        Pair<Manager> mPair = new Pair<Manager>(manager1, manager2);
        printStaffInfo(mPair);
        /*
         * printStaffInfo(mPair); 出错如下： The method printStaffInfo(Pair<Staff>) in the
         * type ExtendsTest is not applicable for the arguments (Pair<Manager>)
         */
        printInfo(mPair);
        printPairInfo(mPair);
    }

    private static void printStaffInfo(Pair<Staff> staffs) {
        System.out.println(staffs.getFirst().getName());
        System.out.println(staffs.getSecond().getName());
    }

    private static <T extends Staff> void printInfo(Pair<T> staffs) {
        System.out.println(staffs.getFirst().getName());
        System.out.println(staffs.getSecond().getName());
    }

    private static void printPairInfo(Pair<? extends Staff> staffs) {
        System.out.println(staffs.getFirst().getName());
        System.out.println(staffs.getSecond().getName());
    }
}
