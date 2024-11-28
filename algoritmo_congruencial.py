import pandas as pd

def metodo_congruencial_lineal(x0, a, c, m, n):
    """
    Generador de números pseudoaleatorios usando el algoritmo congruencial lineal mixto.

    Retorna:
    - Una lista con los números generados.
    """
    resultados = []
    x = x0
    
    for _ in range(n):
        # Calcular el siguiente número usando la fórmula del generador congruencial
        x = (a * x + c) % m
        resultados.append(x)
    
    return resultados

# Parametros
x0 = 5   # Semilla
a = 7  # Multiplicador
c = 9  # Constante aditiva
m = 11  # Módulo
n = 15  # Cantidad de números a generar

# Generar números pseudoaleatorios
aleatorios = metodo_congruencial_lineal(x0, a, c, m, n)

# Crear una tabla con pandas para mostrar los resultados
df = pd.DataFrame(aleatorios, columns=["Número Aleatorio"])

# Mostrar la tabla
print("Secuencia de números aleatorios generados:")
print(df)
