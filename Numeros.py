entrada = input("Escribe el numero separados por comas:")
#Split corta el texto donde hay comas 
numeros_texto = entrada.split(",")
# Convertimos cada número de texto a float.
numeros = [float(n.strip()) for n in numeros_texto]
suma = sum(numeros)
#len sirve para contar elementos en una lista parecido a lenght en java 
media = suma / len(numeros)
maximo = max(numeros)
duplicados = []

# Recorremos la lista y contamos las apariciones de cada número.
for n in numeros_texto:
    try:
        numeros.append(float(n.strip()))
    except ValueError:
        print(f"⚠️ '{n}' no es un número válido, se omitirá.")

# Si la lista queda vacía, detenemos el programa
if not numeros:
    print("No se ingresaron números válidos.")
else:
    #Calculamos la suma, la media y el máximo
    suma = sum(numeros)
    media = suma / len(numeros)
    maximo = max(numeros)

    #Detectamos duplicados
    duplicados = []
    for n in numeros:
        if numeros.count(n) > 1 and n not in duplicados:
            duplicados.append(n)

    #Mostramos los resultados
    print("\nResultados:")
    print("Lista de números:", numeros)
    print("Suma:", suma)
    print("Media:", media)
    print("Máximo:", maximo)
    if len(duplicados) > 0:
        print("Duplicados:", duplicados)
    else:
        print("No hay duplicados.")