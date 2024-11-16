import time
import math
import networkx as net

#Neste ficheiro temos as funcoes necessaria para manipulacao de grafos
#procuramos o melhor caminho entre dois nodos e o tempo para percorer
#Aqui adicionamos nodos ao grafo, adicionamos arestas entre dois nodos

#.........Adicionar nodo..............
def add_nodes(node1,node2,points,graph):
	#Adicionar uma aresta entre o nodo1 e o nodo2
	graph.add_edge(node1,node2,limits=points[:],weight=0)
	
#.........Adicionar objectos no grafo........
def add_obj_graph(localList,obj,weight,graph):
	#Adiciona uma aresta entre um obj e a posição atual do agente
	if not graph.has_edge(localList[-1],obj):
		add_nodes(localList[-1],obj,weight,graph)
		
#.............Mostrar Aresta...............
def show_edge(graph):
	#Mostra na linha de comando todas as arestas já adicionadas ao grafo
	for node in graph.nodes():
		print('|----',node,'-----|')
		for edge in graph[node]:
			print('Edge:',edge,graph[node][edge])
#................................................
#........ Verificar conexoes...............
def search_room_in_graph(localList,weight,graph):
	#Verifica se o nodo em que o agente esta ja esta conectado
	#com outro nodo atraves de uma aresta dentro do grafo
	if len(localList)>1:
		if not graph.has_edge(localList[-1],localList[-2]):
			add_nodes(localList[-1],localList[-2],weight,graph)
#...............O melhor Caminho..................
def make_graph_distance_two_nodes(position,local_points,local,graph):
	#Esta função ajuda a encontrar o menor ou melhor caminho entre dois 
	#nodos e para isso é criado um multigrafo (permite fazer dois nodos 
	#conectarem-se mais de uma vez) e com ele é criado arestas que 
	#representam a distancia entre dois nodos

	
	#Primeira Parte:
	#Aqui não são criadas arestas auxiliares pois o nodo manipulado aqui
	#é o nodo onde o agente está, em outras palavrasm só é dado a distancia
	#entre o agente até as saidas do nodo
	graph2=graph.copy()
	for node in graph2[position[-1]]:
		point1=graph2[position[-1]][node][0]['limits']
		point2=local_points[0]
		cost=distance_two_points(point1,point2)
		graph2[position[-1]][node][0]['weight']=cost
	#segunda parte..............
	#Nesta parte são feitas arestas auxiliares em todos os nodos e 
	#suas saidas
	for node in graph2.nodes():
		if node != position[-1]:
			for edge1 in graph2[node]:
				point1=graph2[node][edge1][0]['limits']
				if(len(graph2[node])>1):
					for edge2 in graph2[node]:
						if(edge2 != edge1 and edge1 != position[-1]):
							point2=graph2[node][edge2][0]['limits']
							cost=distance_two_points(point1,point2)
							graph2.add_edge(node,edge2,limit=point2,weight=cost,going=edge1)
							graph2[node][edge2][0]['weight']=cost
							graph2[node][edge2][0]['going']=edge1
	#Depois de ser criado o multigrafo já com todas as arestas auxiliares, é
	#enviado para 'show_path_two_nodes' que se vai encarregar de mostrar
	# o menor ou melhor caminho
	return best_path_two_nodes(graph2,local_points,position,local)

#..........Procurar o melhor caminho entre dois nodos..........
def best_path_two_nodes(graph,local_points,position,local):
	#Nesta função, podiamos criar uma que se limitasse a achar e mostrar 
	#o caminho entre dois nodos, mas, assumindo que o ambiente pode mudar,
	#achamos melhor criar uma função que pudesse encontrar o menor ou o melhor
	#caminho entre dois nodos.
	#Para tal, usamos a função 'all_pairs_dijkstra_path' da biblioteca
	#networkX, que tem a funcionalidade de aplicar o teorema de Dijktra.
	for node in graph[position[-1]]:
		point1=graph[position[-1]][node][0]['limits']
		point2=local_points[0]
		cost=distance_two_points(point1,point2)
		graph[position[-1]][node][0]['weight']=cost
		graph[position[-1]][node][0]['going']='local'
	sp=dict(net.all_pairs_dijkstra_path(graph))
	path=sp[position[-1]][local]
	#Depois de o caminho ser achado, é enviado para 'distance_two_nodes'
	#que se vai encarregar de somar a distancia entre este path e o tempo que o 
	#agente levará para percorrer (o tempo é uma medida da velocidade por segundos)
	return distance_two_nodes(graph,path)						
							
#........Distancia entre dois nodos .........
def distance_two_nodes(graph,path):
	#Esta função ajudará na soma dos 'weight' ou peso de cada aresta do 
	#path ou caminho dado na função.
	distance=0
	for pos in range(len(path)):
		if(pos+1 < len(path)):
			if(pos==0):
				distance=distance+graph[path[pos]][path[pos+1]][0]['weight']
				if(len(path)==3):
					for keys in graph[path[pos]][path[pos+1]]:
						if(graph[path[pos]][path[pos+1]][keys]['going']==path[pos+2]):
							distance=distance+graph[path[pos]][path[pos+1]][keys]['weight']
							break
					return [distance,distance/245.6,path]
			if(pos+2<len(path)):
				for keys in graph[path[pos]][path[pos+1]]:
					if(graph[path[pos]][path[pos+1]][keys]['going']==path[pos+2]):
						distance=distance+graph[path[pos]][path[pos+1]][keys]['weight']
						break
	return [distance,distance/245.6,path]
#................Distancia entre dois pontos............
def distance_two_points(point1,point2):
	#Nesta função aplicamos o teorema de pitagoras (a distancia entre 
	#dois pontos é uma linha reta: X^2 + Y^2 = Z^2), recebe dois pontos
	#e calcula sua hipotenusa entre esses dois pontos.
	#O resultado dessa função é colocada nos 'weight' dos nodos nas funções
	#make_graph_distance_two_nodes e best_path_two_nodes.
	x1=0
	y1=0
	x2=0
	y2=0
	if(point1[0]<point2[0]):
		x1=point1[0]
		x2=point2[0]
	else:
		x2=point1[0]
		x1=point1[0]
	if(point1[1]<point2[1]):
		y1=point1[1]
		y2=point2[1]
	else:
		y2=point1[1]
		y2=point2[1]
	cost=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	return cost
 
