import collections                      #Para hacer uso de diccionarios, listas, tuplas, etc
import copy
from collections import deque

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

        #for x in self.hdlr_fin:
            #print("del copy :",x)    


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

    def ciudad(self,cod):                           #Devuelve el nombre de la ciudad dado el codigo
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



#################################################  NODE CLASS #######################################

class Node:

    # CONSTRUCTOR
    def __init__(self, name, parent):

        self.name = name                       
        self.parent = parent
        self.dist_to_start_node = 0     # Distancia al nodo inicial (gn)
        self.dist_to_goal_node = 0      # Distancia al nodo meta (hn)
        self.total_dist = 0             # Fn


    # Verifica si 2 nodos son iguales
    def __eq__(self, node_to_compare):

        return self.name == node_to_compare.name

    # Ordena con base al costo de cada nodo
    def __lt__(self, node_to_compare):

         return self.total_dist < node_to_compare.total_dist

    #Imprime los valores del nodo
    def __repr__(self):
        return ('({position},{total_dist})'.format(self.position, self.total_dist))

    #Devuelve el estado del nodo    
    def get_estado(self):
        return self.name    




################################################## GRAPH CLASS #############################################


class Graph:

    # CONSTRUCTOR
    def __init__(self, input_dict=None):

        self.input_dict = input_dict or {}                          #Determina el grafo dado un diccionario, o dejandolo vacio 

        for city_1 in list(self.input_dict.keys()):                 #Determina los valores del diccionario (Llaves del diccionario)

            for (city_2, dist) in self.input_dict[city_1].items():  #Por cada llave recorrida asigna los valores de la conexiòn con otras ciudades
                                                                    #y el costo de las aristas
                self.input_dict.setdefault(city_2, {})[city_1] = dist
       


    #Conecta dos ciudades asignando una arista entre dos ciudades y la distancia 
    def add_connection(self, node_a, node_b, distance=1):

        self.input_dict.setdefault(node_a, {})[node_b] = distance
        
        self.input_dict.setdefault(node_b, {})[node_a] = distance

   
    #Devuelve los vecinos de un nodo especifico
    def get(self, node_a, node_b=None):

        connections = self.input_dict.setdefault(node_a, {})

        if node_b is None:

            return connections

        else:

            return connections.get(node_b)

    #Devuelve en una lista el valor de todas las llaves de un diccionario. Lista de las ciudades 
    def display_all_nodes(self):

        citys = set([city for city in self.input_dict.keys()])

        city_distances = set([distances for dist in self.input_dict.values() for distances, dist_2 in dist.items()])

        display_all_nodes = citys.union(city_distances)

        return list(display_all_nodes)



############################################## AGENTE INTELIGENTE ##################################################

#CONSTRUCTOR
class Agente(object):
    def __init__(self):
        super(Agente, self).__init__()
        
    #Devuelve el indice de un dato en una lista dada
    def indx_lista(self,lista,busq):
        indx=0
        for i in range(len(lista)):
            if lista[i]==busq:
                indx=i
                break
        return indx

################ Greedy : Dijkstra #######################################        
    def dijkstra(self,graph,start,goal,hn):
        #print(graph)
        #Crea diccionarios vacios para la distancia mas corta y predecesores
        shortest_distance = {}
        predecessor = {}

        #Agrega en una lista a todas las ciudades contenidas en el grafo
        unseenNodes = graph.display_all_nodes()
        
        #Asigna una cifra auxiliar para los caluculos del algoritmo
        infinity = 9999999

        #Crea una lista para contener la ruta obtenida por el algoritmo
        path = []

        #Recorre la lista de nodos no visitados
        for node in unseenNodes:
            #print(node)
            #Asigna al diccionario la clave obtenida en nodo con el valor auxiliar como dato
            shortest_distance[node] = infinity

        #Indica que para la ciudad inicial el costo sera el menor, al iniciar el algoritmo    
        shortest_distance[start] = 0
        #print(shortest_distance.values())

        #Ciclo  para realizar el algoritmo siempre que haya nodos en la lista de nodos no visitados
        while unseenNodes:

            #Asignamos una variable para almacenar el nodo con menor costo
            minNode = None
            #Recorre la lista de nodos no visitados
            for node in unseenNodes:
                #print(node)
                #Verificamos si aun no hay nodo minimo asignado, para asignar al nodo actual como minimo
                if minNode is None:
                    minNode = node
                    #print("for 1st if:",minNode)
                #Verificamos si la distancia del nodo actual es menor a la del nodo minimo, de ser asi, se asigna como minimo al nodo actual    
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
                    #print("for 1st if:",minNode)

            #Almacenamos en un diccionario auxiliar a los vecinos del nodo con costo minimo        
            dict_aux=graph.get(minNode)        
            #print(dict_aux)

            #Recorremos cada vecino almacenando la ciudad que representa y la distancia con la ciudad actual        
            for childNode, weight in dict_aux.items():

                #Se verifica si la distancia del nodo minimo, mas la distancia entre ciudades, es menor a la distancia de su nodo vecino
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:

                    #De ser asi se asigna al nodo vecino el costo del nodo munimo
                    shortest_distance[childNode] = weight + shortest_distance[minNode]

                    #Y se que el predecesor, sea igual al nodo minimo
                    predecessor[childNode] = minNode
            #print("min node ..:",minNode)
            #print(hn.codigo_ciudad(minNode))
            #print(unseenNodes)

            #Obtenemos el codigo numerico de la ciudad con costo minimo
            idx=self.indx_lista(unseenNodes,minNode)

            #Quitamos esa ciudad de la lista de nodos no visitados        
            unseenNodes.pop(idx)
 
        #Se indica que la ciudad actual sera igual a la ciudad meta
        currentNode = goal

        #Ciclo que durara siempre que la ciudad aactual sea distinta a la inicial
        while currentNode != start:
            try:
                #Se agrega la ciudad actual a la lista que almacena la ruta
                path.insert(0,currentNode)

                #Se hace nodo actual al nodo padre de este
                currentNode = predecessor[currentNode]
            except KeyError:
                print("Ruta no encontrada")
                break

        path.insert(0,start)

        #Se imprime la ruta y el costo de la misma
        if shortest_distance[goal] != infinity:
            print("KM recorridos: " + str(shortest_distance[goal]))
            print("Ruta: " + str(path)+ "\n\n")

##############################################  A ESTRELLA ##################################################
    def a_star_search(self,graph, heuristics, start, end):
        #print(graph)
        not_expanded = []                   #Nodos por expandir
        expanded = []                       #Nodos expandidos

        #Se crean los dos nodos, el de la ciudad de origen (star) y la ciudad destino (goal), no se les asigna padre
        start_node = Node(start, None)
        goal_node = Node(end, None)

        # Agrega el nodo inicio a la lista de nodos por expandir
        not_expanded.append(start_node)
    
        # Ciclo para realizar el algortimo mientras que la lista de nodos no expandidos contenga elementos
        while len(not_expanded) > 0:

            #Ordena los nodos en la lista de nodos no expandidos
            not_expanded.sort()

            # Toma de la lista de nodos no expandidos, el primer elemento, el cual debera ser el que contenga menor Fn
            current_node = not_expanded.pop(0)

            #Agrega el nodo actual a la lista de nodos expandidos
            expanded.append(current_node)
        
            # Verifica si se ha llegado al estado meta, y si es asi regresa atras para almacenar la ruta obtenida
            if current_node == goal_node:

                #Imprime el costo del camino obtenido para alcanzar la ciudad meta
                print("KM recorridos: ",current_node.dist_to_start_node)
            # List to Store Shrtest Path
                path = []
            
            # Ciclo para retroceder hasta el nodo inicial
                while current_node != start_node:

                    #Se agrega a la ista del camino, el nodo actual
                    path.append(current_node.name)
                    #Se asigna como nodo actual al nodo padre del actual
                    current_node = current_node.parent

                #Se agrega el nodo inicial a la lista del camino
                path.append(start_node.name)
                
                #Se regresa la lista del camino
                return path[::-1]

            #Se obtiene en una lista a los vecinos del nodo actual
            neighbors = graph.get(current_node.name)

            #Recorremos la lista de vecino tomando de cada elemento, la clave y el valor de la distancia entre ciudades
            for key, value in neighbors.items():

                #Creamos nuevos nodos por cada vecino de la lista, asignando como padre de estos, al nodo actual
                neighbor = Node(key, current_node)

                #Verificamos si el nodo vecino se encuentra en la lista de nodos expandidos
                if(neighbor in expanded):
                    continue

                # Calcula el costo total de la ruta

                neighbor.dist_to_start_node = current_node.dist_to_start_node + graph.get(current_node.name, neighbor.name)

                neighbor.dist_to_goal_node = heuristics.get(neighbor.name)

                neighbor.total_dist = neighbor.dist_to_start_node + neighbor.dist_to_goal_node

                #Verifica recorriendo la lista de nodos no expandidos, si el costo de Fn para esta ruta es el mayor o no           
                for node in not_expanded:

                    if (neighbor == node and neighbor.total_dist > node.total_dist):

                        continue

                #Agrega al vecino a la lista de nodos expandidos 
                not_expanded.append(neighbor)
    
        return None

#Devuelve el indice de un dato en una lista dada
    def elems_lista(self,lista):
        n=0
        for i in range(len(lista)):
            n+=1    
        return n


    def BPA(self,tam_list,vecinos,ciudad_dest,path,idx):
        print("BPA")
        #listt=list(vecinos.keys())
        print(vecinos)
        if idx >= tam_list:
            return
        if ciudad_dest == vecinos[idx]:
            path.append(vecinos[idx])
            print("encontrada")
            return True
        path.append(vecinos[idx])
        print(path)
        idx+=1
        self.BPA(tam_list,vecinos,ciudad_dest,path,idx)

            
    def busq_primero_prof(self,ciudad_ori,ciudad_dest,graph):
        #1.Crear una  lista  con  un  solo  elemento  consistente  en  una trayectoria o camino de longitud cero:el nodo raíz 
        path = []
        expanded = []
        bnd = False
        path.append(ciudad_ori)

        nodes=graph.display_all_nodes()
        print(nodes)
        print(path)
        #2.Hasta que el primer camino de la lista llegue al nodo objetivo o se llegue a la lista vacía hacer 
            #a. Extraer el primer camino de la lista
        neighbors_init=list(graph.get(ciudad_ori))

        n_li=self.elems_lista(neighbors_init)
        print(neighbors_init)
        print("n:",n_li)
        bnd=self.BPA(n_li,neighbors_init,ciudad_dest,path,0)
        print(bnd)
        idx=0    
        while bnd == None:
            if idx>=n_li:
                break
            neighbors=list(graph.get(neighbors_init[idx]))
            n_l=self.elems_lista(neighbors)
            print(neighbors)
            print("n:",n_l)
            bnd=self.BPA(n_l,neighbors,ciudad_dest,path,0)
            print(bnd)
            idx+=1
        return path
            #b. Expandir el nodo final de este camino a todos los vecinos del nodoterminal.
            #c. Eliminar los ciclos de los caminos expandidos.
            #d. Insertar estos nuevos caminos al Final de la lista.
        #3.FIN Hasta
        #4.Si se halla el nodo meta notifique el éxito, si no el fracaso
    
################################################# MAIN  ##############################################################


def main():

    #Crea una instancia de la clase que representa el Grafo
    graph = Graph()

    # Conecta dos ciudades dados:
    # Ciudad A , Ciudad B , Distancia

    graph.add_connection("Poza Rica","Xalapa", 219)
    graph.add_connection("Poza Rica","Vega de alatorre",132)
    graph.add_connection("Veracruz","Boca del rio",9.6)
    graph.add_connection("Veracruz","Xalapa",107)
    graph.add_connection("Veracruz","Cotaxtla",70.4)
    graph.add_connection("Veracruz","Vega de alatorre",130)
    graph.add_connection("Boca del rio","Cotaxtla",57.3)
    graph.add_connection("Xalapa","Cordoba",136)
    graph.add_connection("Orizaba","Cordoba",24.8)
    graph.add_connection("Cotaxtla","Cordoba",67.4)
    graph.add_connection("Cotaxtla","Cosamaloapan",98.8)
    graph.add_connection("Coatzacoalcos","Cosamaloapan",176)
         

    #Muestra todas las ciudades
    print("Ciudades")
    print(graph.display_all_nodes())
  
    #Lee la ciudad de origen y la de destino
    ciudad_ori = str(input("Ingrese la ciudad de origen : "))
    ciudad_dest = str(input("Ingrese la ciudad de destino : "))

    #Crea una instancia de la clase que nos proporciona la Heuristica de linea recta de las ciudades
    hdlr_u=Hdlr_and_cities()

    #Genera un codigo numerico dado el nombre de la ciudad de destino
    # y genera una lista con los valores de la heuristica para cada ciudad dada la ciudad destino
    codigo_ciudad=hdlr_u.codigo_ciudad(ciudad_dest)
    hdlr_u.heuristica_por_ciudad_destino(codigo_ciudad)
    hn=hdlr_u.get_hdlr_fin()

    #Crea un diccionario para las heuristicas Hdlr 
    # {'Nombre de la ciudad' : Hdlr}

    heuristics = {}
    heuristics['Poza Rica']        =hn[0]
    heuristics['Veracruz']         =hn[1]
    heuristics['Boca del rio']     =hn[2]
    heuristics['Xalapa']           =hn[3]
    heuristics['Orizaba']          =hn[4]
    heuristics['Cotaxtla']         =hn[5]
    heuristics['Cordoba']          =hn[6]
    heuristics['Vega de alatorre'] =hn[7]
    heuristics['Coatzacoalcos']    =hn[8]
    heuristics['Cosamaloapan']     =hn[9]
    
    print()

    #Crea una instancia para el manejo del agente
    agente_ia=Agente()

    #Indica al agente que se ejecuta el algoritmo A* e imprime la ruta 
    print("Ruta con A*")
    path = agente_ia.a_star_search(graph, heuristics, ciudad_ori, ciudad_dest)
    print("Ruta:",path)
    print()

    #Indica al agente que se ejecuta el Dijkstra e imprime la ruta 
    print("Ruta con dijkstra")
    agente_ia.dijkstra(graph,ciudad_ori,ciudad_dest,hdlr_u)
    print()

    #Indica al agente que se ejecuta el BPP
    print("Ruta con BPP")
    pathh=agente_ia.busq_primero_prof(ciudad_ori,ciudad_dest,graph)
    print(pathh)

if __name__ == "__main__": 
    main()