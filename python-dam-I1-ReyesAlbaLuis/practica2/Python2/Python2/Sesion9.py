import datetime  # Para trabajar con fecha y hora

# Diccionario donde se guardan los registros de fichajes
registros = {}

# ----------------- FUNCIONES -----------------

def registrar_entrada(nombre):
    """Registra la hora de entrada de un empleado."""
    if not nombre:  # Control de error: nombre vacío
        return "Error: el nombre no puede estar vacío."
    try:
        hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registros[nombre] = {"entrada": hora_actual, "salida": None}
        return f"Entrada registrada para {nombre} a las {hora_actual}"
    except Exception as e:  # Captura errores inesperados
        return f"Error al registrar entrada: {e}"

def registrar_salida(nombre):
    """Registra la hora de salida de un empleado."""
    if not nombre:
        return "Error: el nombre no puede estar vacío."
    try:
        if nombre not in registros:
            raise KeyError("El empleado no tiene una entrada registrada.") #Genera un error tipo KeyError si no existe el empleado
        hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        registros[nombre]["salida"] = hora_actual
        return f"Salida registrada para {nombre} a las {hora_actual}"
    except KeyError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error al registrar salida: {e}"


def mostrar_registros():
    """Muestra todos los fichajes realizados."""
    try:
        if not registros:
            return "No hay registros aún."
        resultado = "\n--- REGISTROS DE FICHAJE ---\n"
        for nombre, datos in registros.items():
            resultado += f"{nombre} → Entrada: {datos['entrada']} | Salida: {datos['salida']}\n"
        return resultado
    except Exception as e:
        return f"Error al mostrar registros: {e}"

# ----------------- PROGRAMA PRINCIPAL -----------------

while True:
    print("\n--- SISTEMA DE FICHAJES ---")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Mostrar registros")
    print("4. Salir")

    try:
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            nombre = input("Nombre del empleado: ").strip()
            print(registrar_entrada(nombre))
        elif opcion == 2:
            nombre = input("Nombre del empleado: ").strip()
            print(registrar_salida(nombre))
        elif opcion == 3:
            print(mostrar_registros())
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo (1-4).")
    except ValueError:
        print("Error: introduce un número válido (1-4).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
