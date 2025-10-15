# temperaturas.py
# Conversor de temperaturas: de grados Celsius a Kelvin o Fahrenheit.

# Pedimos al usuario los datos
grados = float(input("Introduce la temperatura en grados Celsius: "))
#Strip quita los espacios en blanco y Upper convierte a mayúsculas
try:

    opcion = input("¿Convertir a Kelvin(K) o Fahrenheit(F)? ").strip().upper()

    if opcion == "K":
        kelvin = grados + 273.15
        print(f"{grados}°C = {kelvin} K")
    elif opcion == "F":
        fahrenheit = (grados * 9/5) + 32
        print(f"{grados}°C = {fahrenheit}°F")
    else:
        print("Opción no válida. Debes escribir 'K' o 'F'.")
except ValueError:
    print("Tienes que introducir o Kelvin o Fahrenheit.")
