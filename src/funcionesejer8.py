def cifrar_mensaje(mensaje, desplazamiento):
    nuevo = []
    for letra in mensaje:
        if letra == "Z" or letra.isalpha() == False:
            nuevo.append(letra)
        else:
            caracter = chr(ord(letra) + desplazamiento)
            nuevo.append(caracter)
    return "".join(nuevo)

def descifrar_mensaje(nuevo, desplazamiento):
    descifrado = []
    for letra in nuevo:
        if letra == "Z" or letra.isalpha() == False:
            descifrado.append(letra)
        else:
            caracter = chr(ord(letra) - desplazamiento)
            descifrado.append(caracter)
    return "".join(descifrado)