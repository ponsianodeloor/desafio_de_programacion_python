def es_numero_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


print(es_numero_primo(3))
print(es_numero_primo(12))
print(es_numero_primo(43))
