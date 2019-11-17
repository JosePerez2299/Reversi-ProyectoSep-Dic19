#Hola joseito 
import pygame,sys
from pygame.locals import *

def DeseaJugar():
	x=input("Desea Jugar")


	if x=="S" or x=="si":
		A=True

	elif x=="N" or "No":
		A=False

	return A

def inicializarTablero():
	tablero=[[0 for x in range(0,8)] for y in range(0,8)]
	return tablero



def QuienJuega(A:int):
	if A==1:
		A=2
	elif A==2:
		A=1
	return A

	

def QuedanFichas(A:[[int]]):
	cuenta=0

	for i in range(0,8):
		for j in range(0,8):
			if A[i][j]==0:
				cuenta = cuenta +1

	return cuenta

def obtenerJugada():
	x=int(input("Fila: "))
	y=input("Columna: ")
	letras='ABCDEFGH'	

	for i in range(0,8):
		if y==letras[i]:
			y=i
	x=x-1

	return x,y


def reflejarJugada(jugador,A,x,y):
	A[x][y]=jugador



def dibujar(A:[[int]]):
	
	
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
	GRIS=(120,120,120)
	NEGRO=(0,0,0)
	

	#Crear letras
	letras=[
	miFuente.render("A",1,NEGRO),  # 1:Bool, Alisado de las letras
	miFuente.render("B",1,NEGRO),
	miFuente.render("C",1,NEGRO),
	miFuente.render("D",1,NEGRO),
	miFuente.render("E",1,NEGRO),
	miFuente.render("F",1,NEGRO),
	miFuente.render("G",1,NEGRO),
	miFuente.render("H",1,NEGRO)
	]	

	
	#Pintar fondo de ventana
	VENTANA.fill(GRIS)
	

	#Instertar Numeros y letras al tablero
	
	x=100
	for i in range(0,8):

		VENTANA.blit(miFuente.render(str(i+1),1,NEGRO),(55,x))
		VENTANA.blit(miFuente.render(str(i+1),1,NEGRO),(565,x))		

		VENTANA.blit(letras[i],(x,50))
		VENTANA.blit(letras[i],(x,560))
		x+=60
	
	VENTANA.blit(miFuente.render("Fila:",1,NEGRO),(620,50))
	VENTANA.blit(miFuente.render("Columna:",1,NEGRO),(620,80))

	#Insertar imagenes del tablero (Casillas, fichas)

	TableroPosy=80
	
	for y in range(0,8):
		
		TableroPosx=80
		
		for x in range(0,8):
			
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




tablero=inicializarTablero()
jugador=2

while DeseaJugar():
	
	dibujar(tablero)
	
	while QuedanFichas(tablero)>0:
		
		x,y=obtenerJugada()
		jugador=QuienJuega(jugador)
		
		reflejarJugada(jugador,tablero,x,y)
		dibujar(tablero)
		
		
		




