"""Looping through a list"""

# Annual Bonus (as percent value)
BONUS_PERFORMANCE: float = 1.12

# our employees list
employees = [
    {"ssn": 506891, "salary": 11235.78},
    {"ssn": 524970, "salary": 14235.34},
    {"ssn": 469559, "salary": 10534.56},
    {"ssn": 202851, "salary": 10262.19},
    {"ssn": 323940, "salary": 19253.28},
    {"ssn": 164539, "salary": 12544.37},
]

# Dont's
for i in range(len(employees)):
    employees[i]["bonus"] = round(employees[i]["salary"] * BONUS_PERFORMANCE, 2)
print(f"[x] Employees with bonus {employees}")

# Do's
for employee in employees:
    employee["bonus"] = round(employee["salary"] * BONUS_PERFORMANCE, 2)
print(f"[√] Employees with bonus {employees}")

# Better!
[employee.update({"bonus": round(employee["salary"] * BONUS_PERFORMANCE, 2)}) for employee in employees]
print(f"[•]Employees with bonus {employees}")

# /eof
