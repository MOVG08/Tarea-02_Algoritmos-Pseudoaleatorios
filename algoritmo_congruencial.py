import pandas as pd

def generador_congruencial_lineal_mixto(seed, a, c, m, n):
    """
    Generador de números pseudoaleatorios usando el algoritmo congruencial lineal mixto.

    Parámetros:
    - seed: semilla inicial (X0), debe ser mayor que 0.
    - a: multiplicador, debe ser mayor que 0.
    - c: constante aditiva, debe ser mayor que 0.
    - m: módulo, debe ser mayor que X0, a, y c.
    - n: cantidad de números pseudoaleatorios a generar.

    Retorna:
    - Una lista con los números generados.
    """
    resultados = []
    x = seed  # Semilla inicial
    
    for _ in range(n):
        # Calcular el siguiente número usando la fórmula del generador congruencial
        x = (a * x + c) % m
        resultados.append(x)
    
    return resultados

# Parametros
seed = 5
a = 7  # Multiplicador
c = 9  # Constante aditiva
m = 11  # Módulo (usando 2^32, que es común en generadores de números aleatorios)
n = 20  # Cantidad de números aleatorios a generar

# Generar números pseudoaleatorios
aleatorios = generador_congruencial_lineal_mixto(seed, a, c, m, n)

# Crear una tabla con pandas para mostrar los resultados
df = pd.DataFrame(aleatorios, columns=["Número Aleatorio"])

# Mostrar la tabla
print("Secuencia de números aleatorios generados:")
print(df)
