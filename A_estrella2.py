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



##Clases para grafo de ciudades
class Vertice:
    def __init__(self,nodo):
        self.nodo = nodo 
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())        



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
    nodo = Nodo('',0)
    nodo=fn_menor();
    print("",nodo.estado)


main()    