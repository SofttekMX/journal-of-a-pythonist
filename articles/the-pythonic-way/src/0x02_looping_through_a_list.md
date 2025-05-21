# The Pythonic Way

"the good python code is like business logic" - Raymond Hettinger

Escribir código que sea claro y comprensible, no solo como buena práctica sino como estilo de trabajo, es clave para cualquier proyecto (y su trascendencia). En este "post", mezcla de experiencia, algunas lecturas y práctica, me di a la tarea de consolidar algunos ejemplos de lo que en el mundo Python, se conoce como "The Pythonic Way".

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
