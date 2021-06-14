#A* ciudades- Peralta Luna Karen Lisseth

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


def create_graph(hn):

    g = GraphAdjacencyList()

    g.add_vertex("Poza Rica",hn)
    g.add_vertex("Veracruz",hn)
    g.add_vertex("Boca del rio",hn)
    g.add_vertex("Xalapa",hn)
    g.add_vertex("Orizaba",hn)
    g.add_vertex("Cotaxtla",hn)
    g.add_vertex("Cordoba",hn)
    g.add_vertex("Vega de alatorre",hn)
    g.add_vertex("Coatzacoalcos",hn)
    g.add_vertex("Cosamaloapan",hn)


    g.add_edge("Poza Rica", "Xalapa", directed=False, weight=219)
    g.add_edge("Poza Rica", "Vega de alatorre", directed=False, weight=132)

    g.add_edge("Veracruz", "Boca del rio", directed=False, weight=9.6)
    g.add_edge("Veracruz", "Xalapa", directed=False, weight=107)
    g.add_edge("Veracruz", "Cotaxtla", directed=False, weight=70.4)
    g.add_edge("Veracruz", "Vega de alatorre", directed=False, weight=130)

    #g.add_edge("Boca del rio", "Veracruz", directed=False, weight=9.6)
    g.add_edge("Boca del rio", "Cotaxtla", directed=False, weight=57.3)
    
    #g.add_edge("Xalapa", "Poza Rica", directed=False, weight=219)
    g.add_edge("Xalapa", "Cordoba", directed=False, weight=136)
    #g.add_edge("Xalapa", "Veracruz", directed=False, weight=107)

    g.add_edge("Orizaba", "Cordoba", directed=False, weight=24.8)

    g.add_edge("Cotaxtla", "Cordoba", directed=False, weight=67.4)
    #g.add_edge("Cotaxtla", "Veracruz", directed=False, weight=70.4)
    #g.add_edge("Cotaxtla", "Boca del rio", directed=False, weight=57.3)
    g.add_edge("Cotaxtla", "Cosamaloapan", directed=False, weight=98.8)

    #g.add_edge("Cordoba", "Orizaba", directed=False, weight=24.8)
    #g.add_edge("Cordoba", "Xalapa", directed=False, weight=136)
    #g.add_edge("Cordoba", "Cotaxtla", directed=False, weight=67.4)

    #g.add_edge("Vega de alatorre", "Poza Rica", directed=False, weight=132)
    #g.add_edge("Vega de alatorre", "Veracruz", directed=False, weight=130)

    g.add_edge("Coatzacoalcos", "Cosamaloapan", directed=False, weight=176)

    #g.add_edge("Cosamaloapan", "Coatzacoalcos", directed=False, weight=176)
    #g.add_edge("Cosamaloapan", "Cotaxtla", directed=False, weight=98.8)



    return g



#Algorithm-
 #The implementation of A* Algorithm involves maintaining two lists- OPEN and CLOSED.
  #  OPEN contains those nodes that have been evaluated by the heuristic function but have not been expanded into successors yet.
   # CLOSED contains those nodes that have already been visited.
#The algorithm is as follows-
#Step-01:
 #   Define a list OPEN.
#  Initially, OPEN consists solely of a single node, the start node S.
OPEN_list = [Nodo('Veracruz',46)]
 

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

            


#Step-02:

def A_estrella():
    if (OPEN_list==Null):      #If the list is empty, return failure and exit.
        print("Error")
        return
#Step-03:
 #   Remove node n with the smallest value of f(n) from OPEN and move it to list CLOSED.
  #  If node n is a goal state, return success and exit.

 
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

def main():
    g = create_graph(0)

    print(g)
    

    nodo = Nodo('',0)
    nodo=fn_menor();
    print("",nodo.estado)


main()    
