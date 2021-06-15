#A* ciudades- Peralta Luna Karen Lisseth

import copy


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

hdlr_fin=list()




#Clase Nodo
class Nodo(object):
    """docstring for Viajero"""
    def __init__(self,estado,hn):
        super(Nodo, self).__init__()
        self.estado = estado 
        #self.nodo_padre= padre
        self.gn = 0 #camino del estado inicial al nodo
        self.hn = hn #num de pasos a lo largo del camino desde el estado inicial

    def calcular_fn(self):      #calcula fn 
        print(self.hn+self.gn)
        fn=self.hn+self.gn
        return  fn

    def aumentar_valor_camino(self,valor_camino):        #aumenta el valor del camino del nodo hacia el nodo inicial
        self.gn +=valor_camino    


    def get_estado(self):
        return self.estado
    def get_hn(self):
        return self.hn    


##Clases para grafo de ciudades
class Vertex(object):

    def __init__(self, label,hn):

        self.label = Nodo(label,hn)
        self.edges = []
        self.visited = False


class Edge(object):

    def __init__(self, to, weight):

        self.to = to
        self.weight = weight



class GraphAdjacencyList(object):

    def __init__(self):

        self.vertices = []

    def __str__(self):

        hline = ("-" * 44) + "\n"
        leftspace = ("|" + (" " * 16) + "|")
        string = []

        string.append(hline)
        string.append("|    Vertices    |    Edge To     | Weight |\n")
        string.append(hline)

        for vertex in self.vertices:

            string.append("|{0: <16}|".format(vertex.label.get_estado()))

            if len(vertex.edges) > 0:

                for index, edge in enumerate(vertex.edges):

                    if index > 0:
                        string.append(leftspace)

                    string.append("{0: <16}|".format(edge.to))

                    if edge.weight is not None:
                        string.append("{0: 8}|".format(edge.weight))
                    else:
                        string.append((" " * 8) + "|")

                    string.append("\n")

                string.append(hline)

            else:

                string.append((" " * 16) + "|" + (" " * 8) + "|\n")
                string.append(hline)

        return "".join(string)

    def add_vertex(self, label,hn):

        """
        Adds a vertex with the given label to the list.
        Raises ValueError if already exists.
        """

        if self.__find_vertex_index(label) == -1:
            v = Vertex(label,hn)
            self.vertices.append(v)
        else:
            raise ValueError("Vertex with this label already exists")

    def add_edge(self, label1, label2, directed, weight):

        """
        Adds edge between given two vertices with given weight.
        Recursively adds "reverse" edge if directed is False.
        Raises ValueError if edge already exists, or if
        either or both vertices do not exist.
        """

        if self.__edge_exists(label1, label2) is True:
            raise ValueError("Edge already exists")
        else:
            index1 = self.__find_vertex_index(label1)
            index2 = self.__find_vertex_index(label2)

            if index1 == -1 or index2 == -1:
                raise ValueError("One or both vertices not found")

            else:
                e1 = Edge(label2, weight)
                self.vertices[index1].edges.append(e1)

                if directed is False:
                    self.add_edge(label2, label1, True, weight)


    def __find_vertex_index(self, label):

        for index, vertex in enumerate(self.vertices):
            if vertex.label.get_estado() == label:
                return index

        return -1

    def __edge_exists(self, label1, label2):

        vertex_index = self.__find_vertex_index(label1)

        for edge in self.vertices[vertex_index].edges:
            if edge.to == label2:
                return True

        return False                
    def get_vertice(self,label1):
        vertex_index = self.__find_vertex_index(label1)
        print(self.vertices[vertex_index].label.get_estado())
        print(self.vertices[vertex_index].label.get_hn())
        #Recuperar una copia del nodo en un objeto nuevo
        nodo_aux= copy.deepcopy(self.vertices[vertex_index].label)
        return nodo_aux
 

#--------------------------------------

def create_graph():

    g = GraphAdjacencyList()
    print(hdlr_fin[0])
    g.add_vertex("Poza Rica",hdlr_fin[0])
    g.add_vertex("Veracruz",hdlr_fin[1])
    g.add_vertex("Boca del rio",hdlr_fin[2])
    g.add_vertex("Xalapa",hdlr_fin[3])
    g.add_vertex("Orizaba",hdlr_fin[4])
    g.add_vertex("Cotaxtla",hdlr_fin[5])
    g.add_vertex("Cordoba",hdlr_fin[6])
    g.add_vertex("Vega de alatorre",hdlr_fin[7])
    g.add_vertex("Coatzacoalcos",hdlr_fin[8])
    g.add_vertex("Cosamaloapan",hdlr_fin[9])


    g.add_edge("Poza Rica", "Xalapa", directed=False, weight=219)
    g.add_edge("Poza Rica", "Vega de alatorre", directed=False, weight=132)

    g.add_edge("Veracruz", "Boca del rio", directed=False, weight=9.6)
    g.add_edge("Veracruz", "Xalapa", directed=False, weight=107)
    g.add_edge("Veracruz", "Cotaxtla", directed=False, weight=70.4)
    g.add_edge("Veracruz", "Vega de alatorre", directed=False, weight=130)


    g.add_edge("Boca del rio", "Cotaxtla", directed=False, weight=57.3)
    
    g.add_edge("Xalapa", "Cordoba", directed=False, weight=136)

    g.add_edge("Orizaba", "Cordoba", directed=False, weight=24.8)

    g.add_edge("Cotaxtla", "Cordoba", directed=False, weight=67.4)

    g.add_edge("Cotaxtla", "Cosamaloapan", directed=False, weight=98.8)

    g.add_edge("Coatzacoalcos", "Cosamaloapan", directed=False, weight=176)



    return g



#Algorithm-
 #The implementation of A* Algorithm involves maintaining two lists- OPEN and CLOSED.
  #  OPEN contains those nodes that have been evaluated by the heuristic function but have not been expanded into successors yet.
   # CLOSED contains those nodes that have already been visited.
#The algorithm is as follows-
#Step-01:
 #   Define a list OPEN.
#  Initially, OPEN consists solely of a single node, the start node S.
OPEN_list = list()
CLOSED_list=list()
 

  

def fn_menor():         #Determina el nodo con menor valor para fn
    menor = 0           #determina fn menor igual a 0 en un inicio
    nodo_aux = Nodo('',0)
    fn_actual = 0       #para determinar el calculo actual
    for x in OPEN_list:
        print(x.estado)                           #Toma el valor de una lista
        x.calcular_fn()     #Determina a fn actual con el calculo de fn del nodo aux actual
        if menor == 0:
            menor=fn_actual
            nodo_aux=x
        else:
            if fn_actual < menor:
                menor=fn_actual
                nodo_aux=x

    return nodo_aux            

            
class Agente(object):
    """docstring for Agente"""
    def __init__(self,ciudad_org,ciudad_dest):
        super(Agente, self).__init__()
        self.ciudad_org=ciudad_org
        self.ciudad_dest=ciudad_dest

    def es_estado_meta(self,ciudad_act):
        if ciudad_act == self.ciudad_dest:
            return True
        return False
    
    def lista_vacia(self,list):            #Verifica si una lista esta vacia
        if len(list)==0:
            return True
        return False  

    #Step-02:

    def A_estrella(self):
        if (self.lista_vacia(OPEN_list)):      #If the list is empty, return failure and exit.
            print("Error")
            return  False  
    #Step-03:
    #   Remove node n with the smallest value of f(n) from OPEN and move it to list CLOSED.
    #  If node n is a goal state, return success and exit.
        menor=fn_menor()
        aux_estado=menor.get_estado()
        CLOSED_list.append(menor)
        OPEN_list.remove(menor)
        if self.es_estado_meta(aux_estado):
            print("Llego al estado meta")
            return True

        #print(OPEN_list)  
        print("Toca expandir")

    
    #Step-04:

#Expand node n.

 
#Step-05:

 

 #   If any successor to n is the goal node, return success and the solution by tracing the path from goal node to S.
  #  Otherwise, go to Step-06.

 
#Step-06:

 

#For each successor node,

#    Apply the evaluation function f to the node.
#    If the node has not been in either list, add it to OPEN.

 
#Step-07:

#Go back to Step-02.

def add_to_OPENLIST(ciudad):
    OPEN_list.append(ciudad)
    print(OPEN_list[0].get_estado())
    print(OPEN_list[0].get_hn())


def __heuristica_por_ciudad_destino(cod_ciudad):        #Busca en la matriz la lista de heuristicas a usar dada una ciudad de destino
    #hdlr_finn=list()
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


def main():
    #Indicamos la ciudad de origen y de destino
    ciudad_ori=str(input("Indique la ciudad de origen:"))
    ciudad_dest=str(input("Indique la ciudad destino:"))

    Agentee=Agente(ciudad_ori,ciudad_dest)

    codigo_ciudad=__codigo_ciudad(ciudad_dest)      #determinamos el codigo de la coidad de destino
    print(codigo_ciudad)                    

    __heuristica_por_ciudad_destino(codigo_ciudad)  #Buscamos la lista de los valores de las heuristicas de cada ciudad
                                                     # con respecto a la ciudad de destino           
    #print(ciudad_ori)
    #print(ciudad_dest)

    #Creamos el grafo representativo de las ciudades
    gr = create_graph()

    print(gr)

    cd_hn=gr.get_vertice(ciudad_ori)        #Buscamos el nodo de la ciudad de origen ,para comenzar
    
    add_to_OPENLIST(cd_hn)      #Agregamos el nodo a la OPENLIST
    #-------- A*
    Agentee.A_estrella()


main()         
