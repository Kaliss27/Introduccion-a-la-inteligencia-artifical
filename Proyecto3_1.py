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



#################################################  NODE CLASS #######################################

class Node:

    # CONSTRUCTOR
    def __init__(self, name:str, parent:str):

        self.name = name
        self.parent = parent
        self.dist_to_start_node = 0 # Distance to start node
        self.dist_to_goal_node = 0 # Distance to goal node
        self.total_dist = 0 # Total cost

    # Built in Object Comparision Function (__eq__)
    # Check if two nodes are identical
    def __eq__(self, node_to_compare):

        return self.name == node_to_compare.name

    # Built in Object Sorting (__lt__)
    # Sort Nodes Based on Total Cost
    def __lt__(self, node_to_compare):

         return self.total_dist < node_to_compare.total_dist

    # Built in Object toString Java like function
    # Print Node
    def __repr__(self):
        return ('({position},{total_dist})'.format(self.position, self.total_dist))
    def get_estado(self):
        return self.name    




################################################## GRAPH CLASS #############################################


class Graph:

    # CONSTRUCTOR
    def __init__(self, input_dict=None):

        self.input_dict = input_dict or {}

        for city_1 in list(self.input_dict.keys()):

            for (city_2, dist) in self.input_dict[city_1].items():

                self.input_dict.setdefault(city_2, {})[city_1] = dist
       


    # Add conection / edge between nodes/verices
    def add_connection(self, node_a, node_b, distance=1):

        self.input_dict.setdefault(node_a, {})[node_b] = distance
        
        self.input_dict.setdefault(node_b, {})[node_a] = distance

    # get neighbours of the current node/vertex
    def get(self, node_a, node_b=None):

        connections = self.input_dict.setdefault(node_a, {})

        if node_b is None:

            return connections

        else:

            return connections.get(node_b)

    # Get all nodes in the graph
    def display_all_nodes(self):

        citys = set([city for city in self.input_dict.keys()])

        city_distances = set([distances for dist in self.input_dict.values() for distances, dist_2 in dist.items()])

        display_all_nodes = citys.union(city_distances)

        return list(display_all_nodes)



##############################################  A STAR SEARCH ##################################################

class Agente(object):
    """docstring for Agente"""
    def __init__(self):
        super(Agente, self).__init__()
        

    def BPP(self,grafo, elementoInicial, elementosRecorridos = []):

        elementosRecorridos.append(elementoInicial)

        vecinos = grafo.get(elementoInicial)

        # Loop over neighbours
        for key, value in vecinos.items():

            vecino = Node(key, elementoInicial)

        # Check if the neighbor is in the expanded list
            if(vecino.name in elementosRecorridos):
                continue

            self.BPP(grafo, vecino, elementosRecorridos)    


################ Greedy : Dijkstra #######################################
#----------- Metodos auxiliares--------------------
    def indx_lista(self,lista,busq):
        indx=0
        for i in range(len(lista)):
            if lista[i]==busq:
                indx=i
                break
        return indx
    def dijkstra(self,graph,start,goal,hn):
        #print(graph)
        shortest_distance = {}
        predecessor = {}
        unseenNodes = graph.display_all_nodes()
        infinity = 9999999
        path = []
        for node in unseenNodes:
            #print(node)
            shortest_distance[node] = infinity
        shortest_distance[start] = 0
        
        #print(shortest_distance.values())

        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                #print(node)
                if minNode is None:
                    minNode = node
                    #print("for 1st if:",minNode)
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
                    #print("for 1st if:",minNode)
            dict_aux=graph.get(minNode)        
            #print(dict_aux)        
            for childNode, weight in dict_aux.items():
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]
                    predecessor[childNode] = minNode
            #print("min node ..:",minNode)
            #print(hn.codigo_ciudad(minNode))
            #print(unseenNodes)
            idx=self.indx_lista(unseenNodes,minNode)        
            unseenNodes.pop(idx)
 
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print("Path not reachable")
                break
        path.insert(0,start)
        if shortest_distance[goal] != infinity:
            print("KM recorridos: " + str(shortest_distance[goal]))
            print("Ruta: " + str(path)+ "\n\n")

################@@#######----- A* ------#############################################
    def a_star_search(self,graph, heuristics, start, end):
        #print(graph)
###########################  Shortest Path Algorithm ################################
   
        not_expanded = [] # Not Expanded
        expanded = [] # expanded

   
        start_node = Node(start, None)
        goal_node = Node(end, None)

    # Add the start node to not_expanded list
        not_expanded.append(start_node)
    
    # Loop until all nodes in not_expanded are expanded
        while len(not_expanded) > 0:

        # Sort The List
            not_expanded.sort()

        # Get the node with the lowest cost
            current_node = not_expanded.pop(0)

        # Add the current node to the expanded list
            expanded.append(current_node)
        
        # Check if we have reached the goal if reached start backtrack , else continue
            if current_node == goal_node:

                print("KM recorridos: ",current_node.dist_to_start_node)
            # List to Store Shrtest Path
                path = []
            
            # Backtrack back to the start node 
                while current_node != start_node:

                
                    path.append(current_node.name)
                    current_node = current_node.parent

                    
                
                path.append(start_node.name)

                
                
                return path[::-1]



        # Get neighbours
            neighbors = graph.get(current_node.name)

        # Loop over neighbours
            for key, value in neighbors.items():

                neighbor = Node(key, current_node)

            # Check if the neighbor is in the expanded list
                if(neighbor in expanded):
                    continue

############################ A_Star_Search_Algorithm #######################################

            # Calculate full path cost
                neighbor.dist_to_start_node = current_node.dist_to_start_node + graph.get(current_node.name, neighbor.name)

                neighbor.dist_to_goal_node = heuristics.get(neighbor.name)

                neighbor.total_dist = neighbor.dist_to_start_node + neighbor.dist_to_goal_node

            # Check if this Node Path's f(x) A* Value is > or not           
                for node in not_expanded:

                    if (neighbor == node and neighbor.total_dist > node.total_dist):

                        continue

          
                not_expanded.append(neighbor)

    
        return None



################################################# MAIN  ##############################################################


def main():

    # Create graph instance
    graph = Graph()

        # add edges/connections between nodes/cities
        # City A , City B , Distance Between
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
         


    print("Ciudades")
    print(graph.display_all_nodes())
  
    ciudad_ori = str(input("Ingrese la ciudad de origen : "))
    ciudad_dest = str(input("Ingrese la ciudad de destino : "))

    hdlr_u=Hdlr_and_cities()

    codigo_ciudad=hdlr_u.codigo_ciudad(ciudad_dest)
    hdlr_u.heuristica_por_ciudad_destino(codigo_ciudad)
    hn=hdlr_u.get_hdlr_fin()

    # Create a dictionary for heuristics : dict{'city_name' : 'distance_to_goal}

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
    agente_ia=Agente()
    print("Ruta con A*")
    path = agente_ia.a_star_search(graph, heuristics, ciudad_ori, ciudad_dest)
    print("Ruta:",path)
    print()
    print("Ruta con dijkstra")
    agente_ia.dijkstra(graph,ciudad_ori,ciudad_dest,hdlr_u)
    #agente_ia.BPP(graph,ciudad_dest)
    
    #anchoPrimero(grafo, buenosAires, imprimir)


if __name__ == "__main__": 
    main()