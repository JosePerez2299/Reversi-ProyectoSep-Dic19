
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
	jugador1=input("\nIntroduzca nombre Jugador 1:")
	jugador2=input("Introduzca nombre Jugador 2:")

	return jugador1,jugador2


def QuienJuega(jugador1,jugador2:str,turno:int):
	if turno==1:
		turno+=1
		jugador=jugador2

	elif turno==2:
		turno-=1
		jugador=jugador1

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

 

def obtenerJugada(jugador):
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
			print("\n====Error====\nEl valor de Fila debe ser (1,2,3,4,5,6,7,8). Columna debe ser (A,B,C,D,E,F,G,H)\n===========")	



	for i in range(0,8):
		if y==letras[i]:
			y=i
	x=x-1

	return x,y


def realizarJugada(turno,A,x,y):
	A[x][y]=turno



def dibujar(A:[[int]],jugador1,jugador2,FichasNegras,FichasBlancas):
	
	assert(len(A)==8 and all(len(A[i])==8 for i in range(0,len(A))))

	pygame.init()
	
	TABLERO_POS=[[0 for x in range(0,8)] for y in range(0,8)]
	ancho,largo=800,600
	

	#Cargar Imagenes
	casillaVacia=pygame.image.load("casillas.png")
	fichaNegra=pygame.image.load("negra.png")
	fichaBlanca=pygame.image.load("blanca.png")	
	

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	miFuente=pygame.font.Font(None,40)
	
	#Colores
	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	MARRON=(128,64,0)
	

	#Crear letras
	letras=[
	miFuente.render("A",1,MARRON),  # 1:Bool, Alisado de las letras
	miFuente.render("B",1,MARRON),
	miFuente.render("C",1,MARRON),
	miFuente.render("D",1,MARRON),
	miFuente.render("E",1,MARRON),
	miFuente.render("F",1,MARRON),
	miFuente.render("G",1,MARRON),
	miFuente.render("H",1,MARRON)
	]	

	
	#Pintar fondo de ventana
	VENTANA.fill(GRIS)
	

	#Instertar Numeros, y texto al tablero
	
	x=100
	for i in range(0,8):

		VENTANA.blit(miFuente.render(str(i+1),1,MARRON),(55,x))
		VENTANA.blit(miFuente.render(str(i+1),1,MARRON),(565,x))		

		VENTANA.blit(letras[i],(x,50))
		VENTANA.blit(letras[i],(x,560))
		x+=60
	
	pygame.draw.rect(VENTANA,MARRON,(590,85,200,30),2)
	pygame.draw.rect(VENTANA,MARRON,(590,120,200,90),2)
	VENTANA.blit(miFuente.render("Puntuación",1,NEGRO),(600,90))
	VENTANA.blit(miFuente.render(str(jugador1.lower())+":"+str(FichasNegras),1,NEGRO),(600,130))
	VENTANA.blit(miFuente.render(str(jugador2.lower())+":"+str(FichasBlancas),1,NEGRO),(600,160))

	
	#Insertar imagenes del tablero (Casillas, fichas)

	TableroPosy=80
	
	for x in range(0,8):
		
		TableroPosx=80
		
		for y in range(0,8):
			
			if A[x][y]==0:

				TABLERO_POS[x][y]=VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
				
			
			elif A[x][y]==1:
				TABLERO_POS[x][y]=VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
				

			elif A[x][y]==2:
				TABLERO_POS[x][y]=VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))
				
			
			TableroPosx+=60	
		
		TableroPosy+=60
	
	
	#Eventos:

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit() 
			sys.exit()

	pygame.display.update()



##PROGRAMA PRINCIPAL

tablero=inicializarTablero()
turno=2

while DeseaJugar():
	
	jugador1,jugador2=Jugadores()

	TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
	
	dibujar(tablero,jugador1,jugador2,FichasNegras,FichasBlancas)
	
	
	while TotalFichas>0:
		
		turno,jugador=QuienJuega(jugador1,jugador2,turno)
		
		x,y=obtenerJugada(jugador)
		
		realizarJugada(turno,tablero,x,y)
		
		TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
		
		dibujar(tablero,jugador1,jugador2,FichasNegras,FichasBlancas)
		
		
		




