package genericity;

import java.util.Date;

public class Manager extends Staff {

    private String office;

    public Manager(String name, int age, String gender, String office) {
        super(name, age, gender);
        this.office = office;
    }

    public String getOffice() {
        return office;
    }

    public void setOffice(String office) {
        this.office = office;
    }

}
