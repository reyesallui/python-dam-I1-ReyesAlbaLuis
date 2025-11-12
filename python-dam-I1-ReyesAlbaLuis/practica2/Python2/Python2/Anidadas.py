# Lista principal donde se guardarán los registros
gastos = []

# Función para añadir un nuevo gasto
def añadir_gasto(descripcion, categoria, monto):
    # Comprobamos que los campos no estén vacíos
    if not descripcion or not categoria:
        print("Error: la descripción y la categoría no pueden estar vacías.")
        return

    # Comprobamos que el monto sea un número
    if not isinstance(monto, (int, float)):
        print("Error: el monto debe ser un número.")
        return

    # Comprobamos si ya existe un registro igual (por descripción)
    for gasto in gastos:
        if gasto["descripcion"] == descripcion:
            print("Error: ya existe un gasto con esa descripción.")
            return

    # Creamos el diccionario del nuevo gasto
    nuevo_gasto = {
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto
    }

    # Lo añadimos a la lista
    gastos.append(nuevo_gasto)
    print("Gasto añadido correctamente.")


# Función para buscar un gasto por descripción
def buscar_gasto(descripcion):
    for gasto in gastos:
        if gasto["descripcion"] == descripcion:
            return gasto
    print("No se encontró ningún gasto con esa descripción.")
    return None


# Función para calcular la media de todos los montos
def calcular_media():
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return None

    total = 0
    for gasto in gastos:
        total += gasto["monto"]

    media = total / len(gastos)
    return media

# Ejemplos de uso
añadir_gasto("Café", "Comida", 2.5)
añadir_gasto("Bus", "Transporte", 1.4)
añadir_gasto("Cine", "Ocio", 8)

print(buscar_gasto("Cine"))
print("La media de los gastos es:", calcular_media())