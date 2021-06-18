from random import random               #Para generar numeros aleattorios
import collections                      #Para hacer uso de diccionarios, listas, tuplas, etc

#Para definir la heuristica de linea directa de cada vertice(ciudad) del grafo con respecto a la ciudad de destino

hdlr=[  [0    ,260  ,285  ,219  ,378  ,321  ,369  ,131  ,369  ,406 ],   #Matriz que determina la heuristica de linea recta Hdlr dada una ciudad meta
        [262  ,0    ,10.8 ,107  ,134  ,70.3 ,110  ,130  ,310  ,147 ],   #Fila/Columna orden:
        [288  ,9.6  ,0    ,133  ,138  ,57.5 ,113  ,156  ,314  ,145 ],   #0->Poza Rica               8->Coatzacoalcos
        [219  ,107  ,132  ,0    ,144  ,168  ,136  ,157  ,416  ,253 ],   #1->Veracruz                9->Cosamaloapan
        [385  ,132  ,134  ,144  ,0    ,88.3 ,24.8 ,253  ,328  ,165 ],   #2->Boca del rio
        [324  ,70.4 ,57.3 ,169  ,88.4 ,0    ,66.8 ,176  ,262  ,99.2],   #3->Xalapa
        [365  ,111  ,113  ,136  ,24.6 ,67.4 ,0    ,233  ,307  ,144 ],   #4->Orizaba
        [132  ,129  ,153  ,157  ,260  ,176  ,247  ,0    ,438  ,275 ],   #5->Cotaxtla
        [564  ,310  ,309  ,409  ,328  ,264  ,311  ,432  ,0    ,176 ],   #6->Cordoba
        [399  ,146  ,144  ,244  ,164  ,98.8 ,142  ,263  ,174  ,0   ]]   #7->Vega de alatorre

hdlr_fin=list()    #

def __heuristica_por_ciudad_destino(cod_ciudad):        #Busca en la matriz la lista de heuristicas a usar dada una ciudad de destino
    for i in range(len(hdlr[cod_ciudad])):
        print(hdlr[cod_ciudad][i])
        hdlr_fin.append(hdlr[cod_ciudad][i])

    for x in hdlr_fin:
        print("del copy :",x)    

def __codigo_ciudad(ciudad):                    #Devuelve el valor numerico de la ciudada dado el nombre
    if ciudad== "Poza Rica": 
        return 0
    if ciudad== "Veracruz":
        return 1
    if ciudad== "Boca del rio":
        return 2    
    if ciudad== "Xalapa":
        return 3
    if ciudad== "Orizaba":
        return 4        
    if ciudad== "Cotaxtla":
        return 5
    if ciudad== "Cordoba":
        return 6
    if ciudad== "Vega de alatorre":
        return 7
    if ciudad== "Coatzacoalcos":
        return 8
    if ciudad== "Cosamaloapan":
        return 9

def ciudad(cod):                    #Devuelve el valor numerico de la ciudada dado el nombre
    if cod== 0: 
        return "Poza Rica"
    if cod== 1:
        return "Veracruz"
    if cod== 2:
        return "Boca del rio"    
    if cod== 3:
        return "Xalapa"
    if cod== 4:
        return "Orizaba"        
    if cod== 5:
        return "Cotaxtla"
    if cod== 6:
        return "Cordoba"
    if cod== 7:
        return "Vega de alatorre"
    if cod== 8:
        return "Coatzacoalcos"
    if cod== 9:
        return "Cosamaloapan"

#--------------------------------------------------------------------------------------

class Grafo:
    '''
        Constructor
        Param:
            dic_grafo=diccionario cono los datos del grafo
    '''
    
    def __init__(self, dic_grafo=None):                         
        if dic_grafo is None:
            self.vertices = {}                                  #Lista de vertices = vertices
        else:
            self.vertices = dic_grafo


    def get_grafo(self):
        return self.vertices

    ''' Metodos para el manejo del grafo
        Param:
            cd:ciudad o elemento a agregar al diccionario
        Return:
            False->si ya existe la ciudad
            True->si no existe y se añadio al diccionario(grafo)        
    '''
    def adiciona_vertice(self, cd):                             
        if cd in self.vertices.keys():                          
            print('Ciudad existente!\n' % v)
            return False
        else:
            self.vertices[cd] = []
            print('Ciudad agregada' % cd)
            return True        

    '''
        Conecta dos ciudades existentes
        Param:
            cd1 (str): ciudad 1
            cd2 (str): ciudad 2.
        Return:
            True -> si se realizo la conexion de las ciudades 
            False-> si no existen las ciduades en el grafo       
    '''
    def conecta(self, cd1, cd2):
        if cd1 not in self.vertices.keys():
            print('No existe la ciudad!\n' % cd1)
            return False
        if cd2 not in self.vertices.keys():
            print('No existe la ciudad!\n' % cd2)
            return False
        if cd1 in self.adyacentes(cd2):
            print('La ciudad de %s ya está conectada con la ciudad de %s!\n' % (cd1, cd2))
        else:
            self.vertices[cd1].append(cd2)
            self.vertices[cd2].append(cd1)
            print('Se conecto la ciudad %s con la ciudad %s!\n' % (cd1, cd2))
            return True
    '''
        Devuelve la cantidad de ciudades registradas
        ordem=n_ciudades
    '''
    def n_ciudades(self):
        return len(self.ciudades())

    '''
        Devuelve la lista de ciudades registradas
        vertices=ciudades
    '''
    def ciudades(self):
        return list(self.vertices.keys())

    '''
        Devuelve un conjunto de todas las ciudades conectadas con una determinada ciudad
        Param:
            cd (str): determinado vértice.
        Return:
            False-> No existe la ciudad
            Lista de ciudades    
    '''
    def adyacentes(self, cd):
        if cd not in self.ciudades():
            print('Ciudad %s no registrada!\n' % cd)
            return False
        else:
            return self.vertices[cd]

    '''
        Retorna el numero de ciudades conectadas a una determinada ciudad
        Param:    
            cd (str): ciudad.
        Return:
            False-> ciudad no existe
            nc (int) -> cantidad de ciudades conectadas
    '''
    def n_ciudades_ciudad(self, cd):
        if cd not in self.ciudades():
            print('Ciudad %s no registrada!\n' % cd)
            return False
        else:
            ady = self.adyacentes(cd)
            n = len(ady) + ady.count(cd)
            return n


class Agente_viajero(object):
    """docstring for Agente_viajero"""
    def __init__(self):
        super(Agente_viajero, self).__init__()
        

    '''
    Algoritmo usado para realizar uma busca em um grafo. O algoritmo
    inicia num nó raiz e explora tanto quanto possível cada um de seus
    ramos antes de retroceder (tomando um grafo com estrutura de árvore como exemplo).
    Complexidade O(n+m)/n = número de vértices e m = número de arestas.
    vertice (str): vértice raiz.
    '''
    def bpp(self,mapa,vertice):
        ciudades=mapa.get_grafo()
        if vertice not in ciudades:
            print("Ciudad no registrada!\n")
        else:
            pila = []
            visitados = []
            pila.append(vertice)
            while pila:
                vertice = pila.pop()
                if vertice not in visitados:
                    visitados.append(vertice)
                    for arista in ciudades[vertice]:
                        pila. append(arista)
            return visitados



if __name__ == "__main__":
    g_busca = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': [],
        'F': [],
        'G': [],
        'H': ['J', 'L'],
        'I': [],
        'J': [],
        'L': []
    }
    agente=Agente_viajero()
    g = Grafo(g_busca)
    print(agente.bpp(g,'A'))