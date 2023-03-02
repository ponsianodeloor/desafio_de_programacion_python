def calcular_factorial(numero):
    factorial = 1
    for i in range(2, numero + 1):
        factorial = factorial * i
    return factorial

    return True


print(calcular_factorial(0))
print(calcular_factorial(3))
print(calcular_factorial(4))
print(calcular_factorial(5))


def calcular_factorial_recursivo(numero):

    if numero == 0 or numero == 1:
        return 1

    return numero * calcular_factorial_recursivo(numero - 1)


print(calcular_factorial_recursivo(0))
print(calcular_factorial_recursivo(3))
print(calcular_factorial_recursivo(4))
print(calcular_factorial_recursivo(5))