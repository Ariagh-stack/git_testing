class Employee:
    def __init__(self, name, salary, hrs_work=30):
        self.name = name
        self.salary = salary
        self.hrs_work = hrs_work

    def increase_salary(self):
        if self.hrs_work > 40:
            self.salary += 40000
        return self.salary

    def get_emp_info(self):
        print("_" * 40)
        print(f"Name of the employee: {self.name}\nSalary: {Employee.increase_salary(self)}")
        print("_" * 40)


def main():
    emp1 = Employee("John", 56000, 47)
    emp2 = Employee("Jane", 46500)

    emp1.get_emp_info()
    emp2.get_emp_info()


if __name__ == "__main__":
    main()
