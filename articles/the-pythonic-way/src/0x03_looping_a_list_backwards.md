# The Pythonic Way

"the good python code is like business logic" - Raymond Hettinger

Escribir código que sea claro y comprensible, no solo como buena práctica sino como estilo de trabajo, es clave para cualquier proyecto (y su trascendencia). En este "post", mezcla de experiencia, algunas lecturas y práctica, me di a la tarea de consolidar algunos ejemplos de lo que en el mundo Python, se conoce como "The Pythonic Way".

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

The Pythonic Way
https://gitlab.com/andresaquino/the-pythonic-way

--- 
