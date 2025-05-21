# The Pythonic Way

"the good python code is like business logic" - Raymond Hettinger

Escribir código que sea claro y comprensible, no solo como buena práctica sino como estilo de trabajo, es clave para cualquier proyecto (y su trascendencia). En este "post", mezcla de experiencia, algunas lecturas y práctica, me di a la tarea de consolidar algunos ejemplos de lo que en el mundo Python, se conoce como "The Pythonic Way".

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

## Next Steps

¿Te resultó interesante?, el post completo en el canal Python (Teams) y el código en GitLab. 

No he visto publicaciones recientes, así que estaré colocando extractos del post completo en este canal.

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

The Pythonic Way
https://gitlab.com/andresaquino/the-pythonic-way

--- 
