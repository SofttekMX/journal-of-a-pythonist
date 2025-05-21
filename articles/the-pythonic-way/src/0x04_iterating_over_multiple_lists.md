# The Pythonic Way

"the good python code is like business logic" - Raymond Hettinger

Escribir código que sea claro y comprensible, no solo como buena práctica sino como estilo de trabajo, es clave para cualquier proyecto (y su trascendencia). En este "post", mezcla de experiencia, algunas lecturas y práctica, me di a la tarea de consolidar algunos ejemplos de lo que en el mundo Python, se conoce como "The Pythonic Way".

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
