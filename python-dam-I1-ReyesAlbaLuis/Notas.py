# analisis_notas.py
# Programa que analiza una lista de calificaciones y muestra un resumen estadístico.

# Pedimos al usuario una lista de notas separadas por comas
entrada = input("Introduce las calificaciones separadas por comas (ej: 6.5, 8, 5, 4, 9, 10, 7, 3): ")

try:
    # Convertimos la cadena en una lista de números (floats)
    notas = [float(n.strip()) for n in entrada.split(",")]

    # --- Cálculos principales ---
    total = len(notas)
    media = round(sum(notas) / total, 2)
    minima = min(notas)
    maxima = max(notas)

    # --- Porcentajes ---
    aprobados = sum(1 for n in notas if n >= 5)
    sobresalientes = sum(1 for n in notas if n >= 9)
    porc_aprobados = round((aprobados / total) * 100, 2)
    porc_sobresalientes = round((sobresalientes / total) * 100, 2)

    # --- Cálculo de la(s) nota(s) más repetida(s) (moda) ---
    frecuencias = {}
    for n in notas:
        frecuencias[n] = frecuencias.get(n, 0) + 1

    max_freq = max(frecuencias.values())
    modas = [str(n) for n, f in frecuencias.items() if f == max_freq]

    # --- Mensaje final según la media ---
    if media >= 8:
        nivel = "Nivel excelente"
    elif media >= 5:
        nivel = "Nivel medio"
    else:
        nivel = "Necesita refuerzo"

    # --- Resultados ---
    print("\n📊 RESUMEN ESTADÍSTICO 📊")
    print(f"Número total de notas: {total}")
    print(f"Media: {media}")
    print(f"Nota mínima: {minima}")
    print(f"Nota máxima: {maxima}")
    print(f"Porcentaje de aprobados: {porc_aprobados}%")
    print(f"Porcentaje de sobresalientes: {porc_sobresalientes}%")
    print(f"Nota(s) más repetida(s): {', '.join(modas)}")
    print(f"\n🟢 {nivel}")

except ValueError:
    # Si el usuario introduce algo que no sea número
    print("❌ Error: asegúrate de introducir solo números separados por comas.")
