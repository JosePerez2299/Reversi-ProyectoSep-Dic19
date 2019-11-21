
import pygame,sys
from pygame.locals import *



def inicializarTablero():
	tablero=[[0 for x in range(0,8)] for y in range(0,8)]
	tablero[3][3]=2
	tablero[4][4]=2
	tablero[3][4]=1
	tablero[4][3]=1

	return tablero

def DeseaJugar():
	x=input("Bienvenido.\n¿Desea Jugar?\nS o N: ")

	x=x.lower()
	if x=="s" or x=="si":
		A=True

	elif x=="n" or x=="no":
		A=False

	return A

def Jugadores():
	while True:
		try:
			jugador1=input("\nIntroduzca nombre Jugador 1:")
			assert(len(jugador1)>0)
			jugador2=input("Introduzca nombre Jugador 2:")
			assert(len(jugador2)>0)
			break
		except:
			print("\n====Error=====\nIntroduzca como minimo un digito para su nombre\n============")

	return jugador1,jugador2


def CambiarTurno(jugador1:str,jugador2:str,turno:int):

	assert(0<turno<=2)
	
	if turno==1:
		turno+=1
		jugador=jugador2

	elif turno==2:
		turno-=1
		jugador=jugador1

	assert(0<turno<=2)

	return turno,jugador


def QuedanFichas(tablero:[[int]]):

	
	negras=0
	blancas=0
	for i in range(0,8):
		for j in range(0,8):
			if tablero[i][j]==1:
				negras += 1
			elif tablero[i][j]==2:
				blancas+=1

	total=64-(negras+blancas)
	
	return total,negras,blancas

 

def obtenerJugada(jugador:str):
	print("\nEs el turno de "+str(jugador)+":\nRealice su jugada:")
		
	letras='abcdefgh'	
	while True:
		try:
			x=int(input("Fila: "))
			assert(1<=x<=8)
			y=input("Columna : ").lower()

			assert(any(y==letras[i] for i in range(0,8)))
			break
		except:
			print("\n====Error====\nEl valor de Fila debe ser (1,2,3,4,5,6,7,8). Columna debe ser (A,B,C,D,E,F,G,H)\n==========")	


	for i in range(0,8):
		if y==letras[i]:
			y=i
	x=x-1

	return x,y


def realizarJugada(turno:int,A:[[int]],x:int,y:int):
	A[x][y]=turno



def dibujar(A:[[int]],jugador1:str,jugador2:str,FichasNegras:int,FichasBlancas:int):
	assert(len(A)==8 and all(len(A[i])==8 for i in range(0,8)))

	
	
	#Inicializar arreglo para almacenar casillas
	TABLERO_POS=[[0 for x in range(0,8)] for y in range(0,8)]
	ancho,largo=800,600
	

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	PUNTUACION=pygame.image.load("IMAGENES/PUNTUACION.png")

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)
	
	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	

	#Crear letras
	letras=[
	fuente.render("A",1,GRIS),  # 1:Bool, Alisado de las letras
	fuente.render("B",1,GRIS),
	fuente.render("C",1,GRIS),
	fuente.render("D",1,GRIS),
	fuente.render("E",1,GRIS),
	fuente.render("F",1,GRIS),
	fuente.render("G",1,GRIS),
	fuente.render("H",1,GRIS)
	]	

	
	#Pintar fondo de ventana
	VENTANA.blit(FONDO,(0,0))
	

	#Insertar imagenes del tablero (Casillas, fichas)
	TableroPosy=60
	
	for x in range(0,8):
		
		TableroPosx=60
		
		for y in range(0,8):
			
			if A[x][y]==0:

				TABLERO_POS[x][y]=VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
				
			
			elif A[x][y]==1:
				TABLERO_POS[x][y]=VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
				

			elif A[x][y]==2:
				TABLERO_POS[x][y]=VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))
				
			
			TableroPosx+=60	
		
		TableroPosy+=60
	
	#Instertar Numeros, y texto al tablero
	
	x=80
	for i in range(0,8):

		VENTANA.blit(fuente.render(str(i+1),1,GRIS),(35,x))
		VENTANA.blit(fuente.render(str(i+1),1,GRIS),(545,x))		

		VENTANA.blit(letras[i],(x,30))
		VENTANA.blit(letras[i],(x,540))
		x+=60
	
	#Tablero de puntuacion
	pygame.draw.rect(VENTANA,GRIS,(590,80,200,40),4)
	pygame.draw.rect(VENTANA,GRIS,(590,120,200,90),4)
	VENTANA.blit(PUNTUACION,(600,75))
	VENTANA.blit(fuente.render(str(jugador1)+": "+str(FichasNegras),1,VERDE),(600,130))
	VENTANA.blit(fuente.render(str(jugador2)+": "+str(FichasBlancas),1,VERDE),(600,170))

	
	

	
	
	
	#Eventos:

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit() 
			sys.exit()

	pygame.display.update()

	



##PROGRAMA PRINCIPAL
pygame.init()
tablero=inicializarTablero()
turno=2

while DeseaJugar():
	
	jugador1,jugador2=Jugadores()

	TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
	
	dibujar(tablero,jugador1,jugador2,FichasNegras,FichasBlancas)
	
	
	while TotalFichas>0:
		
		turno,jugador=CambiarTurno(jugador1,jugador2,turno)
		
		x,y=obtenerJugada(jugador)
		
		realizarJugada(turno,tablero,x,y)
		
		TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
		
		dibujar(tablero,jugador1,jugador2,FichasNegras,FichasBlancas)

		
		
		




