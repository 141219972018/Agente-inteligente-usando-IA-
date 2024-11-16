import time
import networkx as net
import graph as gph
#.....Lista dos objestos............#
pessoas_list=[]
supervisor_list=[]
visitante_list=[]
operario_list=[]
maquinas_list=[]
armazem_list=[]
empacotamento_list=[]
escritorio_list=[]
corredor_list =['coredor 1','coredor 2','coredor 3','coredor 4']

#.....Lista das Divisoes.............#

zona_list=[]
total_division=[]

#......Variaveis Inicializadas.......#
position=['zona 10']
local_point=[[565,400]]
graph=net.MultiGraph()
speed=245.6

#...........Pega nos objetos e coloca-os em listas.....................#
def get_object(object_list,local):
	
	#Esta é a função principal, a mais importante e é 
	#responsável por pegar os inputs recebidos pelo agente, classifica
	# o objeto observado, podendo ser maquina, supervisor, operario, visitante
	#ou uma zona bem identificada.... Depois de classificar é criado
	#um vínculo do objeto com a sala (cria-se uma aresta entre a sala e 
	#o objeto)
	for obj in object_list:
		#Pega a categoria do objeto
		cathegory=obj.split("_")[0]
		
		#Classifica se o objeto é uma pessoa do sexo Masculino, e se for, 
		#é adicionado a uma lista auxiliar que guarda as duas ultimas 
		#pessoas que o agente encontrou.

		#Para determinar se a pessoa era do sexo Masculino ou não, uma 
		#vez que não tinhamos mais informações sobre a pessoa para além
		# de saber que é operario, supervisor ou visitante e ter um nome,
		#tomamos a liberdade de assumir que, na língua portuguesa, a 
		#a probabilidade de um nome Masculino terminar com uma letra diferente da letra "a"
		#é bem maior do que a de um nome femenino. Deste modo, 
		#verificamos os nomes que terminam com uma letra diferente de "a" e assumimos que são
		#do sexo Masculino.
		if(cathegory =='supervisor' or cathegory=='operário' or cathegory=='visitante'):
			if(len(pessoas_list)>2):
				pessoas_list.remove(pessoas_list[0])
			if((len(pessoas_list)==0) and ((obj[-1])!='a')):
				pessoas_list.append(obj)
			if((len(pessoas_list)!= 0) and ((obj[-1])!='a')):
				if((pessoas_list[-1])!= obj):
					pessoas_list.append(obj)
		
		#No codigo a seguir vamos categorizar o abjeto e adicionar
		#aresta entre o objeto e a sala onde se encontra.			
		if(cathegory=='supervisor'):
			if obj not in supervisor_list:
				supervisor_list.append(obj)
				gph.add_obj_graph(getCurrentPosition(),obj,local,graph)
		
		if(cathegory=='operário'):
			if obj not in operario_list:
				operario_list.append(obj)
				gph.add_obj_graph(getCurrentPosition(),obj,local,graph)
			
		if(cathegory=='visitante'):
			if obj not in visitante_list:
				visitante_list.append(obj)
				gph.add_obj_graph(getCurrentPosition(),obj,local,graph)
		
		if(cathegory=='máquina'):
			if obj not in maquinas_list:
				maquinas_list.append(obj)
				gph.add_obj_graph(getCurrentPosition(),obj,local,graph)
				
		if(cathegory=='armazem'):
			if obj not in armazem_list:
				armazem_list.append(obj)
				gph.add_obj_graph(getCurrentPosition(),obj,local,graph)
				
		elif(cathegory=='zona'):
			if obj not in zona_list:
				zona_list.append(obj)
				gph.add_obj_graph(getCurrentPosition(),obj,local,graph)
				if obj=='zona_empacotamento':
					empacotamento_list.append(obj)
		elif cathegory == 'escritório':
			#Aqui, queremos apenas a categoria do objecto para categprizar 
			#a zona em que está
			if cathegory not in escritorio_list:
				escritorio_list.append(cathegory)
				gph.add_obj_graph(getCurrentPosition(),cathegory,local,graph)
					
#.......Actualiza a posicao do agente de acordo a sua localizacao.......'''
def current_location(pos):
	#Atualiza a posicao do agente com o clock do work, a posicao
	#determinada pelas paredes das salas ou zonas que a definidas
	
	local_point.clear()
	local_point.append(pos)
	x =pos[0]
	y =pos[1]
	#pontos que definem os limites de cada zona da fabrica
	if(x>=30 and x<=135 and y>=165 and y<=355):
		position='corredor 1'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=180 and x<=485 and y>=165 and y<=185):
		position='corredor 2'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=30 and x<=485 and y>=380 and y<=450):
		position='corredor 3'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=530 and x<=635 and y>=230 and y<=435):
		position='corredor 4'
		getPosition(position)
		add_to_division_list(position)
	
	
	elif(x>=30 and x<=135 and y>=30 and y<=135):
		position='zona 5'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=180 and x<=285 and y>=30 and y<=135):
		position='zona 6'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=330 and x<=485 and y>=30 and y<=135):
		position='zona 7'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=530 and x<=770 and y>=30 and y<=185):
		position='zona 8'
		getPosition(position)
		add_to_division_list(position)	
	elif(x>=655 and x<=770 and y>=230 and y<=285):
		position='zona 9'
		getPosition(position)
		add_to_division_list(position)	
	elif(x>=660 and x<=770 and y>=330 and y<=385):
		position='zona 10'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=530 and x<=770 and y>=450 and y<=570):
		position='zona 11'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=330 and x<=485 and y>=445 and y<=570):
		position='zona 12'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=180 and x<=285 and y>=440 and y<=570):
		position='zona 13'
		getPosition(position)
		add_to_division_list(position)
	elif(x>=30 and x<=135 and y>=435 and y<=570):
		position='zona 14'
		getPosition(position)
		add_to_division_list(position)	
#////////////////////////////////////////////////////////////////////
#..........Atualizar....................
def getPosition(pos):
	#O Clock do work atualiza a posição do agente e guarda ela numa lista
	if(pos!=position[-1]):
		#position.remove(position[0])
		position.append(pos)
#.......................................
#.........Pega na posicao actual...........................#		
def getCurrentPosition():
	#Pega na ultima coordenada do agente e retorna para ser usada no agente.py
	return position
#..........................................................


#............Adicionar ao total da divisao..............
def add_to_division_list(pos):
	#Esta função se encarrega de ir adicionando na lista 'total_division'
	#todas as divisões por onde o agente passa, sem repetir
	if(pos not in total_division):
		total_division.append(pos)
#..........................................................



#.........Adiciona divisao ou objecto ao grafo............#	
def refresh_graph(posicao):
	
	gph.search_room_in_graph(getCurrentPosition(),posicao,graph)
#..........................................................

 	 
#...........Mostrar arestas no grafo........................
def show_edges():
	#Mostra na linha de comando todas as arestas já adicionadas ao grafo
	gph.show_edges(graph)
#..........................................................


#.................PERGUNTA 1 ...............................#
#........Diga o nome da penultima pessoa do sexo Masculino vista.........

#Esta função encarrega-se de verificar na lista de pessoas do sexo 
#Masculino observadas pelo agente e dizer qual foi a penultima pessoa vista
def get_penultima_pessoa_masculino():
	if(pessoas_list==[]):
		return 'O agente ainda nao encotrou nenhuma pessoa do sexo 	Masculino'
	elif(len(pessoas_list)>=2):
		return 'Penultima pessoa do sexo Masculino:'+ pessoas_list[-2] + '!'
	else:
		return 'Apenas uma pessoa do sexo Masculino encontrada!'+'\nPessoa:'+ pessoas_list[0]
	
#.................PERGUNTA 2.................................#
#Esta função simplesmente verifica na lista "position" e paga o último
#registo de posição que lá estiver. A função "current_location" e a "get_Position"
#encarregam-se de atualizar a posição do agente na lista "position".
#..........Em que zona estas agora.......................
def find_current_location():
	zona=[]
	escritorio=[]
	for node in graph.edges(position[-1]):
		cathegory=node[1].split("_")[0]
		place_name=[1]
		if(cathegory=='zona'):
			zona.append(node[1])
		elif(cathegory=='escritório'):
			escritorio.append(node[1])
	if(len(zona)>=1):
		return('Estou na ' + zona[-1])
	elif(len(escritorio)>=1):
		return ('Estou no ' + escritorio[-1])
	else:
		return (position[-1])
#.......................................................................


#.................PERGUNTA 3 ...............................#
#..........Qual e o caminho para zona de empacotamento....
def show_path_empacotamento():

	#Procura o melhor caminho até a zona empacotamento mais próxima caso 
	#existam mais de uma.
	empacotamento=[]

	#Verificamos todas as zonas empacotamento identificadas pelo agente e nos
	#certificamos de pegar a mais próxima
	if(len(empacotamento_list)>=1):
		for node in empacotamento_list:
			path=gph.make_graph_distance_two_nodes(position,local_point,node,graph)
			if(empacotamento==[]):
				empacotamento.append(path)
			else:
				if(empacotamento[-1][0] > path[0]):
					empacotamento.clear()
					empacotamento.append(path)
		return empacotamento
	else:
		return 'Nenhuma zona de empacotamento encotrado ate ao momento '
		
#...................PERGUNTA 4.................................#
#........Qual e a distancia ate ao laboratorio.........#
def find_distance_laboratorio():

		#Calcula a distância até ao laboratorio, partindo do ponto em que está

	if('zona_laboratório' in graph.nodes()):
		path=gph.make_graph_distance_two_nodes(position,local_point,'zona_laboratório',graph)
		print('A distancia ate ao laboratorio e de', round(path[0],2))
	else:
		print('Nenhum laboratorio foi encotrado ate ao momento')

#.......................................................................


		
#...................PERGUNTA 5.................................#
#......Quanto tempo achas que demora a ir de onde estas ate escritorio.........#
def find_time_to_escritorio():

	#Calcula o tempo que leva para chegar até ao escritorio, partindo do 
	#ponto em que está
	if('zona_escritório' in graph.nodes()):
		path=gph.make_graph_distance_two_nodes(position,local_point,'zona_escritório',graph)
		print('Tempo estimado ate o escritorio',round(path[1],2))
	else:
		print('Nenhum escritório encotrado ate o momento')

#.................PERGUNTA 7 ..................................#
def Probabilidades7():
	
	#Qual é a probabilidade da próxima pessoa a encontrares ser um supervisor?
	T_operario=len(operario_list)
	T_supervisor=len(supervisor_list)
	T_visitante=len(visitante_list)

	if(T_operario != 0 or T_supervisor != 0 or T_visitante!=0 ):
		probabilidade = T_supervisor/(T_supervisor+T_operario+T_visitante)
		probabilidade *= 100
	else:
		probabilidade = 0
	#Imprime a resposta
	print("%.2f"%probabilidade, end = '% \n')
   
#.................PERGUNTA 8 ..................................#
#..Qual é a probabilidade de encontrar um operário numa zona se estiver lá uma
# máquina mas não estiver lá um supervisor?
def Probabilidades2():

	#Nesta questão, assumimos que a maquina e o supervisor são independentes
	
	#Para responder a esta questão usando a probabilidade condicional pela
	#definição ou pela regra de bayes, é necessário termos o total de divisões
	#encontradas pelo agente até ao momento.
	total_zonas=len(total_division)

	#Pegamos na quantidade de maquina e supervisor observados pelo agente
	#ate aquele momento e com isso podemos calcular a percentagem de chance
	# de encontrar estes objetos
	total_operario=len(operario_list)
	total_supervisor=len(supervisor_list)
	total_maquina=len(maquinas_list)

	#Agora vamos calcular a probabilidade condicionada, usando a formula de bayes e pela definiçao
	#A probabilidade vai ser dada por: P(o|ma,-sup)=(P(ma|o,-sup)*P(o|-sup))/ P(Ma|-sup)
	if(total_zonas!=0 and total_maquina!=0 and total_operario!=0):
		PMa=(total_maquina/total_zonas)*100
		#para P(-Sup)
		PnotSup=(1-(total_supervisor/total_zonas))*100
		#para P(o)
		Po=(total_operario/total_zonas)*100
		#para P(Ma|-sup)
		PManotsup=((PMa*PnotSup)/PnotSup)*100
		#Para P(o|-sup)
		Ponotsup=((Po*PnotSup)/PnotSup)*100
		#Para a resposta final P(o|ma,-Sup)
		resposta=((0.2*Ponotsup)/PManotsup)*100
		return 'Ate o momento a probabilidade e de ', round(resposta),'%'
	else:
		return 'A probabilidade e 0'
		
		
