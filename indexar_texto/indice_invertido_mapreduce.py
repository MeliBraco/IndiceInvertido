import functools
import normalizar

class indexar_texto_mapreduce():

    def nose(self):

        #importo los textos
        texto1 = open('C:/Users/Melina/PycharmProjects/indice_invertido/indexar_texto/Textos/texto1.txt',
                      'r').read()
        texto2 = open(
            'C:/Users/Melina/PycharmProjects/indice_invertido/indexar_texto/Textos/texto2.txt',
            'r').read()

        #texto normalizado
        self.t1_raiz = normalizar.texto_raiz(texto1)
        self.t2_raiz = normalizar.texto_raiz(texto2)

        #lista con el total de claves
        self.lista_claves = (self.t1_raiz + " " + self.t2_raiz).split()

        #quito repeticiones
        self.conjunto_claves = set(self.lista_claves)


        lista_intermedia = list(map(self.funcion_map, self.conjunto_claves))

        print(lista_intermedia)

        self.dic = {}
        for x in lista_intermedia:
            lista_interna = x
            for y in lista_interna:
                resultdo = functools.reduce(self.funcion_reduce,y)

        print(resultdo)

    def funcion_map(self, clave):

        lista = []
        if clave in self.t1_raiz:
            lista.append((clave,'1'))
        if clave in self.t2_raiz:
            lista.append((clave, '2'))
        return lista

    def funcion_reduce(self, palabra, id_texto):

        if palabra not in self.dic:
            lista = []
            lista.append(id_texto)
            self.dic[palabra] = lista
        else:
            self.dic[palabra].append(id_texto)
        return self.dic




v = indexar_texto_mapreduce()
print(v.nose())