"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
E11304, Mbalu Lukaya Júnior
53233, Marcus Ramos

"""
import time
import main 
import graph

power=[]
print('Neste momento, o agente não sabe de nada sobre o ambiente em que foi inserido')
def work(posicao, bateria, objetos):
	# Função que serve para armazenar informação recolhida pelo agente
	if(objetos!=[]):
		main.get_object(objetos,posicao)
	#Aqui chamamos uma função que auxilia na atualização da posição do agente
	main.current_location(posicao)
	#Funcao que auxilia na atualização do grafo
	main.refresh_graph(posicao)
	#Encarrega-se de atualizar o agente sobre o seu estado de bateria atual
	if(objetos!=[]):
		main.get_object(objetos,posicao)
	if(power==[]):
		power.append(bateria)
	else:
		power.clear()
		power.append(bateria)
def resp1():
	#Qual foi a penultima pessoa do sexo masculino que viste?
	print(main.get_penultima_pessoa_masculino())


def resp2():
	#Em que tipo de zona estas agora?
	print(main.find_current_location())


def resp3():
	#Qual e o caminho para zona de empacotamento?
	path=main.show_path_empacotamento()
	if(path=='Nenhum empacotamento encotrado ate o momento'):
		print(path)
	else:
		print('Distancia:',round(path[0][0],2),'\nTime:',round(path[0][1],2),'\nPath:',path[0][2])
  

def resp4():
	#Qual a distância até ao laboratório?
	main.find_distance_laboratorio()
  

def resp5():
	#Quanto tempo achas que demoras a ir de onde estás até ao escritório?
	main.find_time_to_escritorio()
    

def resp6():

	#Quanto tempo achas que falta até ficares sem bateria?
	#Para responder a esta questão foram feitos varios testes com a bateria,
	#primeiro testamos quanto tempo a bateria dura com o agente parado (4.35min)
	#observámos mais ou menos
	#e o tempo quando esta em movimento o que deu 3.22 minutos.Dividir por cem (sendo cem a percentagem total de bateria) e
	#multiplicar pelo tempo que ele aguenta em movimento. Logo, obtemos o va-
	#restante do equipamento sempre em movimento, da mesma forma con-
	#seguimos obter o valor, com o equipamento em repouso.

	#parado =(power[0]/100)*4.35
	parado=(power[0]/100)*(4.35)
	#movimento =(power[0]/100)*3.22
	movimento=(power[0]/100)*(3.22)
	#o estado da bateria atual
	print('Bateria Atual',power[0])
	print('Se eu continuar a me mover, restaram me:', round(movimento,2),'minutos','\nSe eu  ficar parado, restara me',round(parado,2))
  

def resp7():
	
	#Responsavel por calcular a probabilidade de encotrar um supervisor
	#Chamando a funcão probabilidade7 Responsavel por calcular a probabilidade
	print(main.Probabilidades7())


def resp8():
	#Chamando a funcão probabilidade2
	#Responsavel por calcular a probabilidade pretendida
	print(main.Probabilidades2())

