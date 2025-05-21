"""looping a list backwards"""

# our employees list
employees = [
    {"ssn": 506891, "gender": "male", "age": 35, "salary": 11235.78},
    {"ssn": 524970, "gender": "female", "age": 43, "salary": 14235.34},
    {"ssn": 469559, "gender": "female", "age": 25, "salary": 10534.56},
    {"ssn": 202851, "gender": "male", "age": 32, "salary": 10262.19},
    {"ssn": 323940, "gender": "female", "age": 52, "salary": 19253.28},
    {"ssn": 164539, "gender": "male", "age": 53, "salary": 12544.37},
]

# Dont's
print("reversed using range function")
for i in range(len(employees) - 1, -1, -1):
    print(f"[x] ssn {employees[i]['ssn']}, age {employees[i]['age']}, gender {employees[i]['gender']}")

# Do's
print("Reversed using reversed function")
for employee in reversed(employees):
    print(f"[√] ssn {employee['ssn']}, age {employee['age']}, gender {employee['gender']}")

# Alternative
print("Sorted using a lamda function (by age)")
for employee in sorted(employees, key=lambda x: x["age"], reverse=True):
    print(f"[√] ssn {employee['ssn']}, age {employee['age']}, gender {employee['gender']}")


# /eof
