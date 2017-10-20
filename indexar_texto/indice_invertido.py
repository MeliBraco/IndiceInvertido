import normalizar

def  value_cantidad_repeticiones(texto):

    clave_dic = normalizar.quitar_palabras_claves_dic(texto)

    dic_palabras = {}
    for x in clave_dic:
        dic_palabras[x] = normalizar.stemming(texto).count(x)

    return dic_palabras





#en español no funciona bien
texto = "melina mélina.) a por pero nosotros casa casas"
print(value_cantidad_repeticiones(texto))