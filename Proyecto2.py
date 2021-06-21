from random import random               #Para generar numeros aleattorios
import collections                      #Para hacer uso de diccionarios, listas, tuplas, etc
import copy


class Hdlr_and_cities(object):
    """docstring for Hdlr_and_cities"""
    def __init__(self):
        super(Hdlr_and_cities, self).__init__()
        self.hdlr= [[0    ,260  ,285  ,219  ,378  ,321  ,369  ,131  ,369  ,406 ],   #Matriz que determina la heuristica de linea recta Hdlr dada una ciudad meta
                    [262  ,0    ,10.8 ,107  ,134  ,70.3 ,110  ,130  ,310  ,147 ],   #Fila/Columna orden:
                    [288  ,9.6  ,0    ,133  ,138  ,57.5 ,113  ,156  ,314  ,145 ],   #0->Poza Rica               8->Coatzacoalcos
                    [219  ,107  ,132  ,0    ,144  ,168  ,136  ,157  ,416  ,253 ],   #1->Veracruz                9->Cosamaloapan
                    [385  ,132  ,134  ,144  ,0    ,88.3 ,24.8 ,253  ,328  ,165 ],   #2->Boca del rio
                    [324  ,70.4 ,57.3 ,169  ,88.4 ,0    ,66.8 ,176  ,262  ,99.2],   #3->Xalapa
                    [365  ,111  ,113  ,136  ,24.6 ,67.4 ,0    ,233  ,307  ,144 ],   #4->Orizaba
                    [132  ,129  ,153  ,157  ,260  ,176  ,247  ,0    ,438  ,275 ],   #5->Cotaxtla
                    [564  ,310  ,309  ,409  ,328  ,264  ,311  ,432  ,0    ,176 ],   #6->Cordoba
                    [399  ,146  ,144  ,244  ,164  ,98.8 ,142  ,263  ,174  ,0   ]]   #7->Vega de alatorre
        self.hdlr_fin=[]

    def get_hdlr_fin(self):
        return self.hdlr_fin
        
    def heuristica_por_ciudad_destino(self,cod_ciudad):        #Busca en la matriz la lista de heuristicas a usar dada una ciudad de destino
        for i in range(len(self.hdlr[cod_ciudad])):
            #print(self.hdlr[cod_ciudad][i])
            self.hdlr_fin.append(self.hdlr[cod_ciudad][i])

        for x in self.hdlr_fin:
            print("del copy :",x)    


    def codigo_ciudad(self,ciudad):                    #Devuelve el valor numerico de la ciudada dado el nombre
        #print("codigo ciudas")
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

    def ciudad(self,cod):                    #Devuelve el valor numerico de la ciudada dado el nombre
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
#--------------------------------------------
'''class Estado(object):
    """docstring for Estado"""
    def __init__(self, ciudad,cod_cd):
        super(Estado, self).__init__()
        self.ciudad = ciudad
        self.hdlr=hdlr_fin[cod_cd]

    def get_estado(self):
        return self.ciudad    
    
    def get_hdlr(self):
        return self.hdlr        '''
#-------------------------------------
#Clase Nodo
class Nodo(object):
    """docstring for Viajero"""
    def __init__(self,estado,padre,hdlr):
        super(Nodo, self).__init__()
        self.estado = estado 
        self.nodo_padre= padre
        self.gn = 0 #camino del estado inicial al nodo
        self.hn = hdlr #num de pasos a lo largo del camino desde el estado inicial

    def calcular_fn(self):      #calcula fn 
        print(self.hn+self.gn)
        fn=self.hn+self.gn
        return  fn

    def aumentar_valor_camino(self,valor_camino):        #aumenta el valor del camino del nodo hacia el nodo inicial
        self.gn +=valor_camino    

    def get_estado(self):
        return self.estado

    def set_estado(self,estado):
        self.estado=estado    

    def get_padre(self):
        return self.padre

    def set_padre(self,padre): 
        self.padre=padre 
            
    def get_hn(self):
        return self.hn

    def set_hn(self,hn):
        self.hn+=hn    

    def set_gn(self,gna):
        self.gn+=gna

    def get_gn(self):
        return self.gn 
#------------------------------------
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
    def bpp(self,mapa,vertice,origen):
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
                        pila. append(arista.get_destino())
            return visitados

    def configurar_nodo(self,nodo_inicial,costo_camino):
        nodo_inicial.set_gn(costo_camino)

    def asignar_padre(self,nodo_actual,nodo_padre):
        nodo_actual.set_padre(nodo_padre)


    def extraer_nodo_menor(self,lista):
        #print("ext nod men 1:",lista)            
        menor_fn=lista[0].calcular_fn()
        indx=0
        for x in range(len(lista)):
            if lista[x].calcular_fn()<menor_fn:
                print("if menor")
                menor_fn=lista[x]
                indx=x
        print("menor:",lista[indx].get_estado())        
        print("print menor fn:",menor_fn)        
        return indx        
                   
    def obtener_sucesores(self,ciudad_ori,g):
        return g[ciudad_ori]

    def contiene(self,lista,b):
        boole = False
        for x in lista:
            if x == b:
                boole=True    
                break    
        return boole

    def buscar_arista(self,ciudad_dest,lista):
        distancia=0
        for i in range(len(lista)):
            if lista[i].destino==ciudad_dest:
                distancia= lista[i].get_distancia()
                break
        return distancia        
                    
    def costo(self,ciudad_ori,ciudad_dest,g):
        list_aux=g[ciudad_ori]
        print("lista aux1:",list_aux)
        costo=self.buscar_arista(ciudad_dest,list_aux)
        print("costoo:",costo)
        return costo

    def indx_lista(self,lista,busq):
        indx=0
        for i in range(len(lista)):
            if lista[i].get_estado==busq:
                indx=i
                break
        return indx
    #A-Estrella (G, nodo-Inicial, nodo-Final) {Precondición Q1: G = (V, E) ∧ nodo-Inicial, nodo-Final ∈V)         
    def A_estrella(self,G,ciudad_inicial,ciudad_final,hdlr_list):
        if G == False:
            print("No existe mapa registrado")
            return False

        cod_cd1=hdlr_list.codigo_ciudad(ciudad_inicial)
        cod_cd2=hdlr_list.codigo_ciudad(ciudad_final)
        
        hn=hdlr_list.get_hdlr_fin()

        nodo_final = Nodo(ciudad_final,"",hn[cod_cd2])
        OPEN_list=list()
        CLOSED_list=list()
        nodo_actual=Nodo(ciudad_inicial,"",hn[cod_cd1])
        OPEN_list.append(nodo_actual)
        print(OPEN_list[0].get_estado())

        while len(OPEN_list) != 0:
            print("hi1")
            indx_m=self.extraer_nodo_menor(OPEN_list)
            nodo_actual=OPEN_list[indx_m]
            OPEN_list.remove(nodo_actual)
            CLOSED_list.append(nodo_actual)
            print("OPEN_list")
            for i in range(len(OPEN_list)):
                print(OPEN_list[i].get_estado())
            print("CLOSED_list")
            for i in range(len(CLOSED_list)):
                print(CLOSED_list[i].get_estado())
            print("")    
            if nodo_actual.get_estado() == nodo_final.get_estado():
                OPEN_list.clear()
            else:
                sucesores=self.obtener_sucesores(nodo_actual.get_estado(),mapa)
                print("sucesores_list")
                for i in range(len(sucesores)):
                    print(sucesores[i].get_destino())
                print("")  
                num_sucesores=len(sucesores)
                for i in range(num_sucesores):
                    print(" for range")
                    if self.contiene(CLOSED_list,sucesores[i].get_destino()) == False :
                        print("if no contiene")
                        cod_c=hdlr_list.codigo_ciudad(sucesores[i].get_destino())
                        print("cod ciudad sucesor:",cod_c,sucesores[i].get_destino())
                        sucesor_actual=Nodo(sucesores[i].get_destino(),nodo_actual,hn[cod_c])
                        print(sucesor_actual.get_estado())
                        sucesor_actual.set_gn(nodo_actual.get_gn()+self.buscar_arista(sucesores[i].get_destino(),sucesores))
                        print(sucesor_actual.get_gn())

                        if self.contiene(OPEN_list,sucesor_actual.get_estado())== False:
                            print("no esta en OPEN_list")
                            OPEN_list.append(sucesor_actual)
                        else:
                            if OPEN_list[i].get_gn() > sucesor_actual.get_gn():
                                print("OPEN_list[i}>gn:")
                                OPEN_list[i]=sucesor_actual
                            #end if
                        #end if
                    # end if
                #end if
            #loop
        
        if nodo_actual.get_estado() == nodo_final.get_estado():
            print("Ciudades recorridas para llegar a %s:",nodo_final.get_estado(),len(CLOSED_list))
            print("Ciudades:")
            for i in range(len(CLOSED_list)):
                print(CLOSED_list[i].get_estado())
            return True    
        else:
            print("NO existe camino entre las ciudades")
            return False
                        


#----------------------------------------------

class Arista(object):
    """docstring for Arista"""
    def __init__(self, destino,distancia):
        super(Arista, self).__init__()
        self.destino = destino
        self.distancia=distancia
    def get_distancia(self):
        return self.distancia
    def get_destino(self):
        return self.destino
        

#---------------------------------------------
if __name__ == "__main__":

    #Indicamos la ciudad de origen y de destino
    ciudad_ori=str(input("Indique la ciudad de origen:"))
    ciudad_dest=str(input("Indique la ciudad destino:"))

    hdlr_u=Hdlr_and_cities()

    codigo_ciudad=hdlr_u.codigo_ciudad(ciudad_dest)
    #codigo_ciudad=codigo_ciudad(ciudad_dest)      #determinamos el codigo de la coidad de destino
    print(codigo_ciudad)
                   
    codigo_ciudad2=hdlr_u.codigo_ciudad(ciudad_ori)
    #codigo_ciudad=codigo_ciudad(ciudad_dest)      #determinamos el codigo de la coidad de destino
    print(codigo_ciudad2)

    hdlr_u.heuristica_por_ciudad_destino(codigo_ciudad)  #Buscamos la lista de los valores de las heuristicas de cada ciudad
                                                     # con respecto a la ciudad de destino 
        
    #hn_oficial=hdlr_u.get_hdlr_fin()
    
    #print(hn_oficial)

    mapa ={
        "Poza Rica":[Arista("Xalapa", 219),Arista("Vega de alatorre",132)],
        "Veracruz":[Arista("Boca del rio",9.6),Arista("Xalapa",107),Arista("Cotaxtla",70.4),Arista("Vega de alatorre",130)],
        "Boca del rio":[Arista("Veracruz",9.6),Arista("Cotaxtla",57.3)],
        "Xalapa":[Arista("Poza Rica", 219),Arista("Cordoba",136),Arista("Veracruz",107)],
        "Orizaba":[Arista("Cordoba",24.8)],
        "Cotaxtla":[Arista("Cordoba",67.4),Arista("Veracruz",70.4),Arista("Boca del rio",57.3),Arista("Cosamaloapan",98.8)],
        "Cordoba":[Arista("Orizaba",24.8),Arista("Xalapa",136),Arista("Cotaxtla",67.4)],
        "Vega de alatorre":[Arista("Poza Rica",132),Arista("Veracruz",130)],
        "Coatzacoalcos":[Arista("Cosamaloapan",176)],
        "Cosamaloapan":[Arista("Coatzacoalcos",176),Arista("Cotaxtla",98.8)] 
        }                         

    agente=Agente_viajero()
    g = Grafo(mapa)
    print(agente.bpp(g,ciudad_dest,ciudad_ori))
    agente.A_estrella(mapa,ciudad_ori,ciudad_dest,hdlr_u)
    '''                                                    
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
    }'''