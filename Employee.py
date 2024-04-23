class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_dept):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_dept = emp_dept
        
    def calc_emp_salary(self):
        if self.emp_dept = "Engineering":
            return self.emp_salary * 1.1  #10% bonus for engineering department
            
        elif self.emp_dept = "Architecture":
            return self.emp_salary * 1.05  #5% bonus for architecture department
            
        elif self.emp_dept = "Medical":
            return self.emp_salary * 1.15  #15% bonus for medical department
            
        else 
            return self.emp_salary  #No bonus for regular employees

    def emp_assign_dept(self, department):
        self.emp_dept = department
        
    def print_employee_details(self):
        print("Employee ID: ", self.emp_id)  
        print("Employee Name: ", self.emp_name)
        print("Employee Salary: ", self.emp_salary)
        print("Employee Department: ", self.emp_dept)
        
        
#Example usage
emp1 = Employee(4,"Aniket More",10000,"Engineering")
emp1.print_employee_details()
emp1.emp_assign_department("Medical")
emp1.calc_salary()           
