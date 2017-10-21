import functools
import normalizar

class indexar_texto_mapreduce():

    def nose(self):

        texto1 = open('C:/Users/Melina/PycharmProjects/indice_invertido/indexar_texto/Textos/El inspector.txt' , 'r').read()
        texto2 = open('C:/Users/Melina/PycharmProjects/indice_invertido/indexar_texto/Textos/El perrito que no podia caminar.txt','r').read()

        self.t1_raiz = normalizar.texto_raiz(texto1)
        self.t2_raiz = normalizar.texto_raiz(texto2)

        total_clave = normalizar.texto_raiz(texto1+texto2).split()

        lista_intermedia = map(self.funcion_map, total_clave)
        resultado = functools.reduce(self.funcion_reduce() ,lista_intermedia)


        return lista_intermedia

    def funcion_map(self,x):

        lista = []
        if x in self.t1_raiz:
            lista.append((x,'1'))
        if x in self.t2_raiz:
            lista.append((x,'2'))

        print (lista)

    def funcion_reduce(self,x):

        dic ={}



v = indexar_texto_mapreduce()
print(v.nose())