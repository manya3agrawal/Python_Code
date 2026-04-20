class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__basic_salary = basic_salary

    def calculate_hra(self):
        return 0.20 * self.__basic_salary   

    def calculate_da(self):
        return 0.10 * self.__basic_salary 

    def calculate_tax(self):
        return 0.05 * self.__basic_salary

    def calculate_gross_salary(self):
        return self.__basic_salary + self.calculate_hra() + self.calculate_da()

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()

    def display_salary_details(self):
        print("\n--- Employee Salary Details ---")
        print(f"Employee ID   : {self.__emp_id}")
        print(f"Name          : {self.__name}")
        print(f"Basic Salary  : {self.__basic_salary}")
        print(f"HRA           : {self.calculate_hra()}")
        print(f"DA            : {self.calculate_da()}")
        print(f"Tax Deduction : {self.calculate_tax()}")
        print(f"Gross Salary  : {self.calculate_gross_salary()}")
        print(f"Net Salary    : {self.calculate_net_salary()}")

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

emp = Employee(emp_id, name, basic_salary)
emp.display_salary_details()
