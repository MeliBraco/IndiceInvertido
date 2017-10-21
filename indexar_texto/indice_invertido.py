import normalizar

def  indiceInvertido_cantidad_repeticiones(texto):

    clave_dic = normalizar.lista_palabras_claves(texto)

    dic_palabras = {}
    for x in clave_dic:
        dic_palabras[x] = normalizar.texto_raiz(texto).count(x)

    return dic_palabras





#en español no funciona bien
texto = "melina mélina.) a por pero nosotros, !casa casas $ Hola Python"
print(normalizar.texto_raiz(texto))
print(indiceInvertido_cantidad_repeticiones(texto))