"""Looping through a list"""

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
    """
    Validar la existencia de una tienda

    :parameter id_product int
    :return bool
    """
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


# /eof
