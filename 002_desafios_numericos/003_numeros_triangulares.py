"""
*   = 1
**  = 2
*** = 3
"""

def calcular_numero_triangular(fila):

    triangular = 0
    for i in range(1, fila + 1):
        triangular += i
    return triangular


print(calcular_numero_triangular(2))
print(calcular_numero_triangular(4))
print(calcular_numero_triangular(6))