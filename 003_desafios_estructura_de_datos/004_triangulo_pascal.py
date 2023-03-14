def triangulo_pascal(cantidad_filas):
    triangulo = []
    for n_fila in range(cantidad_filas):
        fila = []
        for posicion in range(n_fila+1):
            if posicion == 0 or posicion == n_fila:
                fila.append(1)
            else:
                valor = triangulo[n_fila-1][posicion-1] + triangulo[n_fila-1][posicion]
                fila.append(valor)
        triangulo.append(fila)
    return triangulo

print(triangulo_pascal(4))
