def primera_letra_repetida(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    lista_letras = []
    for letra in texto_sin_espacios:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)

    return texto_minuscula


print(primera_letra_repetida("Hola mundo"))
