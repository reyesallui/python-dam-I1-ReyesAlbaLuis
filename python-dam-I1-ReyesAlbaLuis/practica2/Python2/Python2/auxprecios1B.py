# auxprecios.py

def maximo(precios):
    try:
        resultado = max(precios)
    except ValueError:
        raise ValueError("La lista está vacía, no se puede calcular el máximo.")
    except TypeError:
        raise TypeError("La lista debe contener solo números.")
    else:
        return resultado
    finally:
        print("Se intentó calcular el máximo.")


def minimo(precios):
    try:
        resultado = min(precios)
    except ValueError:
        raise ValueError("La lista está vacía, no se puede calcular el mínimo.")
    except TypeError:
        raise TypeError("La lista debe contener solo números.")
    else:
        return resultado
    finally:
        print("Se intentó calcular el mínimo.")


def promedio(precios):
    try:
        if len(precios) == 0:
            raise ValueError("La lista está vacía, no se puede calcular el promedio.")
        resultado = sum(precios) / len(precios)
    except TypeError:
        raise TypeError("La lista debe contener solo números.")
    else:
        return resultado
    finally:
        print("Se intentó calcular el promedio.")


def rango(precios):
    try:
        resultado = max(precios) - min(precios)
    except ValueError:
        raise ValueError("La lista está vacía, no se puede calcular el rango.")
    except TypeError:
        raise TypeError("La lista debe contener solo números.")
    else:
        return resultado
    finally:
        print("Se intentó calcular el rango.")


def aplicar_descuento(precios, porcentaje):
    try:
        if not isinstance(porcentaje, (int, float)):
            raise TypeError("El porcentaje debe ser un número.")
        factor = 1 - (porcentaje / 100)
        nuevos_precios = [p * factor for p in precios]
    except TypeError:
        raise TypeError("La lista debe contener solo números y el porcentaje debe ser numérico.")
    else:
        return nuevos_precios
    finally:
        print("Se intentó aplicar un descuento.")
