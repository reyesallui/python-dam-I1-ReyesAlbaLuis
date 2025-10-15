# Importamos datetime para trabajar con fechas
import datetime

# Pedimos el nombre
nombre = input("Introduce tu nombre: ")

# Bucle para asegurarnos de que se introduce un año válido (numérico)
while True:
    try:
        # Pedimos el año de nacimiento
        anio_nacimiento = int(input("Introduce tu año de nacimiento (ej. 1990): "))
        
        # Validamos que el año sea razonable
        if anio_nacimiento < 1900 or anio_nacimiento > datetime.datetime.now().year:
            print("Por favor, introduce un año válido (entre 1900 y el actual).")
            continue
        
        # Si es válido, rompemos el bucle
        break
    except ValueError:
        # Captura cuando el usuario no pone un número
        print("Error: Debes introducir un número válido para el año.")

# Obtenemos la fecha actual
hoy = datetime.datetime.now()
anio_actual = hoy.year

# Calculamos la edad
edad = anio_actual - anio_nacimiento

# Clasificamos la edad en tramos
if edad < 18:
    tramo = "Menor de 18 años"
elif 18 <= edad <= 65:
    tramo = "Adulto (18 a 65 años)"
else:
    tramo = "Mayor de 65 años"

# Determinamos el día de la semana en que nació
# Usamos 1 de enero como fecha de nacimiento (solo con el año, porque no sabemos el día/mes exacto)
# Si quieres pedir día y mes exacto, se puede extender fácilmente
while True:
    try:
        mes = int(input("Introduce tu mes de nacimiento (1-12): "))
        dia = int(input("Introduce tu día de nacimiento (1-31): "))
        
        fecha_nacimiento = datetime.datetime(anio_nacimiento, mes, dia)
        # Si no hay error, salimos del bucle
        break
    except ValueError:
        print("Fecha no válida. Intenta de nuevo.")

# Diccionario para traducir el día de la semana
dias_semana = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

# Obtenemos el día de la semana
dia_semana = dias_semana[fecha_nacimiento.weekday()]

# Mostramos resultados
print("\n--- RESULTADOS ---")
print(f"Hola {nombre}, tienes {edad} años.")
print(f"Clasificación por edad: {tramo}")
print(f"Naciste un {dia_semana}.")
