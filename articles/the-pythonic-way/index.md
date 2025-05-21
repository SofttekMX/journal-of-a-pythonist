# The Pythonic Way

"the good python code is like business logic" - Raymond Hettinger

Mi historia como desarrollador no difiere de la de muchos otros, que comenzaron con C/C++, que navegaron entre Pascal y Basic (pasando por esas ediciones "Turbo"), y que con el devenir de los años; aprendieron otros lenguajes como Java, Lisp o Prolog. En todos ellos, la estructura siempre resultaba importante; los proyectos universitarios resultaban ser un reto al momento de  revisar y comprender lo que nuestros compañeros habían codificado, independientemente del lenguaje usado.

La historia laboral no se aleja de este escenario.

Python, al igual que otros lenguajes, cuenta con documentación oficial relacionada a nuevas implementaciones, cambios, recomendaciones y buenas prácticas de desarrollo, conocidas como PEP (Python Enhancement Proposal). La PEP8 es la referencia que contiene las normas o convenciones para escribir código que sea claro y conciso; y que a través de los años, la comunidad de Python ha adoptado y mejorado, resultando en lo que se considera el estilo "pitónico" (The Pythonic way).

Así que escribir código que sea claro y comprensible, no solo como buena práctica sino como estilo de trabajo, es clave para cualquier proyecto (y su trascendencia). En este "post", mezcla de experiencia, algunas lecturas y práctica, me di a la tarea de consolidar algunos ejemplos de lo que en el mundo Python, se conoce como "The Pythonic Way".

Pero antes, entremos en el mood requerido, dale play ["The Wolf You Feed - Nita Strauss"](https://www.youtube.com/watch?v=YYQ02OP5h00)

## Snake-Case 

Considera la importancia de apegarse a la convención de nombres: "snake_case".
Por otro lado, recuerda que nunca habrá mejor oportunidad para comenzar a practicar el idioma inglés, arriésgate.

```python
# Dont's
nombreReporte = "Estado de Cuenta"

# Do's 
name_report = "Estado de Cuenta"

# Better!
name_report: str = "Estado de Cuenta"

```

## Looping through a list

Recorrer una lista puede ser más sencillo de lo que parece, operando sobre cada uno de los elementos que le componen sin conocer la longitud de la misma.

```python 
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
print(f"[•] Employees with bonus {employees}")

```

## Looping through a list (using an index)

En ocasiones es necesario recorrer esa lista y tomar un índice, podría ser tentador generar el rango y recorrerla; o podrías usar *enumerate*.

```python
# Our shopping_list
shopping_list = [
    "1 litro de leche",
    "1 paquete de Pan integral",
    "1 litro de Aceite de oliva",
    "6 Tomates frescos",
    "1 paquete de Queso rallado",
    "1 pechuga de pollo",
    "8 papas",
    "1 rollo de espinacas frescas",
    "12 de huevos",
    "1 paquete de mantequilla",
    "1 ajo fresco",
    "1 kilo de limón",
    "3 litros de agua embotellada",
    "1 bote de helado de vainilla ",
]


# simulate existence of a product
def exists_at_store(id_product: int) -> bool:
    return id_product % 2


#
# Let's go shopping!

# Dont's
shopping_cart = []
for id in range(len(shopping_list)):
    if exists_at_store(id):
        shopping_cart = [*shopping_cart, shopping_list[id]]
print(f"[x] Products in our shopping cart {shopping_cart}")

# Do's
shopping_cart = []
for id, product in enumerate(shopping_list):
    if exists_at_store(id):
        shopping_cart.append(product)
print(f"[√] Products in our shopping cart {shopping_cart}")

# Better!
shopping_cart = [product for id, product in enumerate(shopping_list) if exists_at_store(id)]
print(f"[•] Products in our shopping cart {shopping_cart}")

```

## Looping a list in backward mode

Para esas ocasiones donde es necesario recorrer esa lista, pero en modo inverso: *reversed*.
Que por cierto, también podrías hacerlo usando lambdas, incluyo el ejemplo como una alternativa.

```python
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

```

## Iterating over multiple lists

Cuando es necesario recorrer dos o más listas y hacer una asignación simultanea: *zip*.

```python
# license plates
license_plates = [
    "LWO 756",
    "28C 382",
    "9LU 094",
    "ZSG 951",
    "727 37O",
    "36Q 759",
    "365 IHN",
    "PCA 515",
    "113 244",
    "037 FKO",
    "TCY 180",
    "791 BOX",
    "376 922",
    "XFH 488",
    "217 WJW",
    "3A3 786",
    "G73 0DT",
    "017 OYJ",
    "KCO 301",
    "2Y9 904",
]

subjects = [
    "Rosa Mena",
    "Raquel Segovia",
    "Israel Zedillo",
    "Marcela Solorio",
    "Catalina Cardenas",
    "Bruno Bétancourt",
    "Salma Perales",
    "Débora Serrato",
    "Claudia Griego",
    "Patricia Ruelas",
    "Jesús Lovato",
    "Mauro Estrada",
]

#
# Time to assign

# Dont's
to_authorize = min(len(subjects), len(license_plates))
for application in range(to_authorize):
    print(f"[x] {subjects[application]}, license plate {license_plates[application]}")

# Do's
for subject, plate in zip(subjects, license_plates):
    print(f"[√] {subject}, license plate {plate}")

```

## Using operator like "in"

En este escenario, usando el operador "in" para no hacer multiples comparaciones.

```python 
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
def require_parking(name_team: str) -> bool:
    return name_team in ("Human Resources", "Business Development")


print("Parking Zone")
template: str = "[√] {0} of {1}, parking zone: {2}"
for employee in employees:
    parking_zone = "premium" if require_parking(employee["team"]) else "regular"
    print(template.format(employee["name"], employee["team"], parking_zone))

```

## Next Steps

¿Te resultó interesante?, aún hay material por desarrollar, te leo.
 
El código fuente lo pueden encontrar en la siguiente URL: https://gitlab.com/andresaquino/the-pythonic-way

## URLs 

The Pythonic Way
https://blog.junglacode.org/memorias/tutoriales/the-pythonic-way/

Camel Case vs. Snake Case vs. Pascal Case — Naming Conventions
https://khalilstemmler.com/blogs/camel-case-snake-case-pascal-case/#Snake-case

Writing Phytonic Code
https://inventwithpython.com/beyond/chapter6.html

PEP8 
https://realpython.com/ref/glossary/pep-8/

How to Write Beautiful Python Code With PEP 8
https://realpython.com/python-pep8/#how-to-choose-names

--- 
