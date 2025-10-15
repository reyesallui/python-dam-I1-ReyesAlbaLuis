# Pedir al usuario una lista de números separados por comas
entrada = input("Escribe una lista de números separados por comas: ")

# Intentar convertir los valores a números (float)
try:
    numeros = [float(n.strip()) for n in entrada.split(',')]
except ValueError:
    print("❌ Error: asegúrate de escribir solo números separados por comas.")
    exit()

# Calcular los valores básicos
suma_total = sum(numeros)
media = suma_total / len(numeros)
maximo = max(numeros)

# Buscar números duplicados
duplicados = []
for n in numeros:
    if numeros.count(n) > 1 and n not in duplicados:
        duplicados.append(n)

# Mostrar resultados
print(f"\n📊 Resultados:")
print(f"Suma: {suma_total}")
print(f"Media: {media}")
print(f"Máximo: {maximo}")
if duplicados:
    print(f"Números duplicados: {duplicados}")
else:
    print("No hay números duplicados.")