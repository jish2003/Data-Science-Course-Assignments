employee_data = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 32, 'department': 'Engineering', 'salary': 80000},
    103: {'name': 'Priya', 'age': 29, 'department': 'Marketing', 'salary': 60000},
    104: {'name': 'Rohan', 'age': 26, 'department': 'Finance', 'salary': 55000},
    105: {'name': 'Meena', 'age': 35, 'department': 'Sales', 'salary': 70000},
    106: {'name': 'Kiran', 'age': 30, 'department': 'HR', 'salary': 52000},
    107: {'name': 'Rajeev', 'age': 28, 'department': 'Engineering', 'salary': 82000},
    108: {'name': 'Sneha', 'age': 31, 'department': 'Marketing', 'salary': 61000},
    109: {'name': 'Arjun', 'age': 34, 'department': 'Finance', 'salary': 58000},
    110: {'name': 'Divya', 'age': 25, 'department': 'Sales', 'salary': 67000},
    111: {'name': 'Vikram', 'age': 33, 'department': 'Engineering', 'salary': 85000},
    112: {'name': 'Tanya', 'age': 27, 'department': 'HR', 'salary': 51000},
    113: {'name': 'Neha', 'age': 29, 'department': 'Marketing', 'salary': 62000},
    114: {'name': 'Manoj', 'age': 36, 'department': 'Finance', 'salary': 59000},
    115: {'name': 'Pooja', 'age': 30, 'department': 'Sales', 'salary': 72000},
    116: {'name': 'Ravi', 'age': 28, 'department': 'Engineering', 'salary': 81000},
    117: {'name': 'Anjali', 'age': 32, 'department': 'HR', 'salary': 53000},
    118: {'name': 'Kunal', 'age': 26, 'department': 'Marketing', 'salary': 60000},
    119: {'name': 'Shruti', 'age': 31, 'department': 'Finance', 'salary': 57000},
    120: {'name': 'Deepak', 'age': 35, 'department': 'Sales', 'salary': 74000}

}


def Add_Employee():
    emp_id = int(input("Enter the Employee ID: "))
    if(emp_id not in employee_data):
        employee_info = {}
        
        employee_info['name'] = str(input("Enter the name of the employee - "))
        employee_info['age'] = int(input("Enter the age of the Employee - "))
        employee_info['department'] = str(input("Enter the department of the Employee - "))
        employee_info['salary'] = int(input("Enter the salary of the Employee - "))


    elif(emp_id in employee_data):
        print("Employee already exists in the database.") 
        return

    employee_data[emp_id] = employee_info 
    print("Employee added successfully")



def view_employee_data():
    if(len(employee_data) == 0):
        return(print("\n\nNO EMPLOYEES AVAILABLE."))
    
    print(f"\n\n{'ID':<5} {'Name':<10} {'Age':<10} {'Department':<15} {'Salary':<10}")
    print("-"*50)

    for emps, details in employee_data.items():
        Name = details['name']
        Age = details['age']
        Department = details['department']
        Salary = details['salary']

        print(f"{emps:<5} {Name:<10} {Age:<10} {Department:<15} {Salary:<10}")
    
    print("\n")




def Search_Employee(emp_id):
    if(emp_id in employee_data.keys()):
        print(f"{'Name - ':<10} {employee_data[emp_id]['name']:<6} {' ':<5} {'Age - ':<7} {employee_data[emp_id]['age']:<7} {' ':<5} {'Department - ':<15} {employee_data[emp_id]['department']:<10} {' ':<5} {'Salary - ':<10} {employee_data[emp_id]['salary']:<10} {' ':<5}")

    else:
        return(print("EMPLOYEE NOT FOUND"))



ans = 1
while(ans != 4):

    print("\n")
    print("="*50)
    print("1. Add Employee\n2. View All Employees\n3. Search for Employee\n4. Exit")
    ans = int(input("Choose any one option from above: "))


    if(ans == 1):
        Add_Employee()
       

    elif(ans == 2):
        view_employee_data()


    elif(ans == 3):
        emp_id = int(input("Enter the Employee ID that you want to search: "))
        Search_Employee(emp_id)


    elif(ans == 4):
        print("\nTHANK YOU!\n")
        continue


    else:
        print("Please choose valid option!")

        
    