# ---------- ESTRUCTURA INVERSA ----------
gastos_inverso = {
    "descripcion": [],
    "categoria": [],
    "monto": []
}


# ---------- AÑADIR GASTO ----------
def añadir_gasto_inverso(descripcion, categoria, monto):
    if not descripcion or not categoria:
        print("Error: la descripción y la categoría no pueden estar vacías.")
        return

    if not isinstance(monto, (int, float)):
        print("Error: el monto debe ser un número.")
        return

    # Comprobamos duplicado
    if descripcion in gastos_inverso["descripcion"]:
        print("Error: ya existe un gasto con esa descripción.")
        return

    # Añadimos a cada lista correspondiente
    gastos_inverso["descripcion"].append(descripcion)
    gastos_inverso["categoria"].append(categoria)
    gastos_inverso["monto"].append(monto)
    print("✅ Gasto añadido correctamente (estructura inversa).")


# ---------- BUSCAR GASTO ----------
def buscar_gasto_inverso(descripcion):
    if descripcion not in gastos_inverso["descripcion"]:
        print("No se encontró ningún gasto con esa descripción.")
        return None

    # Buscamos el índice donde aparece
    i = gastos_inverso["descripcion"].index(descripcion)
    gasto = {
        "descripcion": gastos_inverso["descripcion"][i],
        "categoria": gastos_inverso["categoria"][i],
        "monto": gastos_inverso["monto"][i]
    }
    return gasto


# ---------- CALCULAR MEDIA ----------
def calcular_media_inverso():
    if len(gastos_inverso["monto"]) == 0:
        print("No hay gastos registrados.")
        return None

    return sum(gastos_inverso["monto"]) / len(gastos_inverso["monto"])


# ---------- EJEMPLO DE USO ----------
if __name__ == "__main__":
    añadir_gasto_inverso("Café", "Comida", 2.5)
    añadir_gasto_inverso("Bus", "Transporte", 1.4)
    añadir_gasto_inverso("Cine", "Ocio", 8)

    print("\n📘 Resultado de la búsqueda (inversa):")
    print(buscar_gasto_inverso("Cine"))

    print("\n💰 Media de los gastos (inversa):", calcular_media_inverso())