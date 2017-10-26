import normalizar

def  indiceInvertido_cantidad_repeticiones(texto):

    lista_clave = normalizar.texto_raiz(texto).split()
    #elimino repetdos paso a lista a un conjunto
    conjunto_claves = set(lista_clave)

    dic_palabras = {}
    for x in conjunto_claves:
        dic_palabras[x] = normalizar.texto_raiz(texto).count(x)

    return dic_palabras





#en español no funciona bien
texto = "melina mélina.) a por pero nosotros, !casa casas $ Hola Python"
print(normalizar.texto_raiz(texto))
print(indiceInvertido_cantidad_repeticiones(texto))