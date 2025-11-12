# auxprecios.py

def maximo(precios):
    """Devuelve el precio máximo de la lista."""
    return max(precios)

def minimo(precios):
    """Devuelve el precio mínimo de la lista."""
    return min(precios)

def promedio(precios):
    """Devuelve el promedio de los precios."""
    return sum(precios) / len(precios)

def rango(precios):
    """Devuelve la diferencia entre el precio máximo y el mínimo."""
    return maximo(precios) - minimo(precios)

def aplicar_descuento(precios, porcentaje):
    """Aplica un descuento a todos los precios y devuelve una nueva lista."""
    factor = 1 - (porcentaje / 100)
    return [p * factor for p in precios]
