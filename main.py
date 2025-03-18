
# Employee Management System - OOP

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"--- Employee Details ---\nEmployee ID: {self.employee_id}\nName: {self.name}\nDepartment: {self.department}")


class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


employees = [
    PermanentEmployee("S123", "Sohel Shaikh", "IT", 60000, 5000),
    ContractEmployee("A123", "Mr.ashish", "HR", 50, 160),
    Intern("B123", "Anonymous", "Finance", 1500)
]

for emp in employees:
    emp.display_details()
    print(f"Total Salary: ${emp.calculate_salary():.2f}\n")
