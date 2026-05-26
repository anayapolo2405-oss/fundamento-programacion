# Matriz del menú
menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 30000],
    ["Ensalada", "Saludable", 18000],
    ["Pasta", "Italiana", 35000],
    ["Sushi", "Japonesa", 45000],
    ["Tacos", "Mexicana", 22000]
]

# Categoría y condición para descuento
categoria_objetivo = "Comida Rapida"
umbral = 20000

# Función para calcular precio final
def calcular_precio_final(categoria, precio):

    if categoria == categoria_objetivo and precio > umbral:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final

# Mostrar menú
print("====== MENU DEL RESTAURANTE ======")

for i in range(len(menu)):
    print(i + 1, ".", menu[i][0], "-", "$", menu[i][2])

# Elegir producto
opcion = int(input("\nSeleccione un producto: "))

# Obtener datos del producto
producto = menu[opcion - 1]

nombre = producto[0]
categoria = producto[1]
precio_base = producto[2]

# Calcular precio final
precio_final = calcular_precio_final(categoria, precio_base)

# Mostrar resultado
print("\n===== FACTURA =====")
print("Producto:", nombre)
print("Categoría:", categoria)
print("Precio Base: $", precio_base)
print("Precio Final: $", precio_final)
