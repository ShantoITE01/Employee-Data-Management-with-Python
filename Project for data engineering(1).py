# 1. Storing employee data - each employee’s data is in a tuple, stored within a list
employees = [
    ("Alice", "IT", 3),  # each tuple contains (name, department, years of experience)
    ("Bob", "Finance", 5),
    ("Charlie", "IT", 1),
    ("David", "HR", 4),
]

# 2. Using a set to show unique departments from the employee list
departments = {emp[1] for emp in employees}
print("Departments:", departments)

# 3. Counting the number of employees in each department using a dictionary
employee_count_by_dept = {}
for emp in employees:
    department = emp[1]
    if department in employee_count_by_dept:
        employee_count_by_dept[department] += 1
    else:
        employee_count_by_dept[department] = 1

print("Employee Count by Department:", employee_count_by_dept)

# 4. Adding a new employee to the employee list
new_employee = ("Emma", "Marketing", 2)
employees.append(new_employee)
print("Updated Employee List:", employees)

# 5. Finding employees based on years of experience (e.g., employees with 3 years of experience)
target_years = 3
filtered_employees = [emp for emp in employees if emp[2] == target_years]
print(f"Employees with {target_years} years of experience:", filtered_employees)
