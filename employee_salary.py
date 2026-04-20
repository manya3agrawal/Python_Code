class Employee {
    // Encapsulation (private variables)
    private int id;
    private String name;
    private double basicSalary;

    // Constructor
    public Employee(int id, String name, double basicSalary) {
        this.id = id;
        this.name = name;
        this.basicSalary = basicSalary;
    }

    // Methods to calculate salary components
    public double calculateHRA() {
        return 0.20 * basicSalary; // 20%
    }

    public double calculateDA() {
        return 0.10 * basicSalary; // 10%
    }

    public double calculateTax() {
        return 0.05 * basicSalary; // 5%
    }

    public double calculateGrossSalary() {
        return basicSalary + calculateHRA() + calculateDA();
    }

    public double calculateNetSalary() {
        return calculateGrossSalary() - calculateTax();
    }

    // Display method
    public void displaySalary() {
        System.out.println("Employee ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Basic Salary: " + basicSalary);
        System.out.println("HRA: " + calculateHRA());
        System.out.println("DA: " + calculateDA());
        System.out.println("Tax: " + calculateTax());
        System.out.println("Gross Salary: " + calculateGrossSalary());
        System.out.println("Net Salary: " + calculateNetSalary());
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        Employee emp = new Employee(101, "Manya", 50000);
        emp.displaySalary();
    }
}
