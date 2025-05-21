"""Using operators like in"""

# employees
employees = [
    {"name": "Margarita Amaya", "plate": "914ZEC", "team": "Infrastructure"},
    {"name": "Barbara Santillán", "plate": "LEE-5005", "team": "Security"},
    {"name": "Timoteo Carreón", "plate": "9-2592H", "team": "Human Resources"},
    {"name": "Patricia Verduzco", "plate": "1PC1672", "team": "Infrastructure"},
    {"name": "Omar Peres", "plate": "806-519", "team": "Software Development"},
    {"name": "Virginia Burgos", "plate": "843 WXM", "team": "Security"},
    {"name": "Marcos Baeza", "plate": "093 FKI", "team": "Human Resources"},
    {"name": "Eugenia Robles", "plate": "LGF 560", "team": "Infrastructure"},
    {"name": "Leticia Barragán", "plate": "9YY 183", "team": "Software Development"},
    {"name": "Arcelia Olmos", "plate": "696 7651", "team": "Human Resources"},
    {"name": "Guillermo Luna", "plate": "690-BTG", "team": "Infrastructure"},
    {"name": "Virginia Pulido", "plate": "30-O345", "team": "Architecture"},
    {"name": "Hilda Rodríquez", "plate": "315-IJE", "team": "Software Development"},
    {"name": "Perla Narváez", "plate": "70XL5", "team": "Business Development"},
    {"name": "Mauro Bétancourt", "plate": "ZRY 336", "team": "Business Development"},
    {"name": "Felipe Ochoa", "plate": "278 SGI", "team": "Software Development"},
    {"name": "Ramiro Urbina", "plate": "HPM-8680", "team": "Software Development"},
    {"name": "Gloria Tafoya", "plate": "MFQ0418", "team": "Software Development"},
    {"name": "Jacinto Olivo", "plate": "04-8646G", "team": "Software Development"},
    {"name": "Alberto Mora", "plate": "N68 6JT", "team": "Infrastructure"},
]

#
# Time to assign

# Dont's
print("Parking Zone")
for id in range(len(employees)):
    if employees[id]["team"] == "Human Resources" or employees[id]["team"] == "Business Development":
        print(f"[x] {employees[id]['name']} of {employees[id]['team']}, parking zone: premium")
    else:
        print(f"[x] {employees[id]['name']} of {employees[id]['team']}, parking zone: regular")

# Do's
print("Parking Zone")
for employee in employees:
    if employee["team"] in ("Human Resources", "Business Development"):
        print(f"[√] {employee['name']} of {employee['team']}, parking zone: premium")
    else:
        print(f"[√] {employee['name']} of {employee['team']}, parking zone: regular")

# Better!
print("Parking Zone")
for employee in employees:
    parking_zone = "premium" if employee["team"] in ("Human Resources", "Business Development") else "regular"
    print(f"[√] {employee['name']} of {employee['team']}, parking zone: {parking_zone}")


# Alternative
def require_parking(team: str) -> bool:
    """
    The name of individual of team that requieres the parking space

    Parameters
    ----------
    team: str
        Team or individual name that requieres the parkins space

    Returns
    -------
    bool
        Requiere el espacio o no
    """
    return team in ("Human Resources", "Business Development")


print("Parking Zone")
template: str = "[√] {0} of {1}, parking zone: {2}"
for employee in employees:
    parking_zone = "premium" if require_parking(employee["team"]) else "regular"
    print(template.format(employee["name"], employee["team"], parking_zone))

# /eof
