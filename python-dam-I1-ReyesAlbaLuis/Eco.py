# eco_io.py
# Programa que pide tres números, muestra la suma, la media y el mayor.
# Además, guarda un resumen con el "prompt", la explicación y una adaptación libre en un archivo.

# Pedimos 3 números al usuario
try:
    n1 = float(input("Introduce el primer número: "))
    n2 = float(input("Introduce el segundo número: "))
    n3 = float(input("Introduce el tercer número: "))

    # Cálculos
    suma = n1 + n2 + n3
    media = suma / 3
    mayor = max(n1, n2, n3)

    # Mostramos los resultados
    print(f"\nResultados:")
    print(f"Suma: {suma}")
    print(f"Media: {round(media, 2)}")
    print(f"Mayor: {mayor}")

    # Adaptación libre: mostrar si todos son iguales o diferentes
    if n1 == n2 == n3:
        adaptacion = "Todos los números son iguales."
    else:
        adaptacion = "Los números son diferentes."

    # Guardar en archivo S3_prompts.txt
    with open("S3_prompts.txt", "w", encoding="utf-8") as f:
        f.write("=== ECO_IO ===\n")
        f.write("Prompt: Pedir 3 números y mostrar suma, media y mayor.\n")
        f.write("Explicación: Se leen tres valores, se calcula suma, media y el mayor usando max().\n")
        f.write(f"Adaptación libre: {adaptacion}\n")

    print("\n✅ Resultados guardados en 'S3_prompts.txt'")

except ValueError:
    print("❌ Error: Debes introducir solo números.")