
##es valida
#Flanquear
#obtener jugada

def DeseaJugar():
	#Crear Ventana
	ancho,largo=800,600
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")


	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	MARRON=(128,64,0)
	
	TITULO=pygame.image.load("IMAGENES/TITULO.png")
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	JUGAR=pygame.image.load("IMAGENES/JUGAR.png")
	SALIR=pygame.image.load("IMAGENES/SALIR.png")


	
	VENTANA.blit(FONDO,(0,0))

	VENTANA.blit(TITULO,(120,10))
	JUGAR_V=VENTANA.blit(JUGAR,(280,250))
	SALIR_V=VENTANA.blit(SALIR,(290,350))
	jugar=False
	
	while not(jugar):
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos
				
				if JUGAR_V.collidepoint(x,y):
					jugar=True

				elif SALIR_V.collidepoint(x,y):
					pygame.quit() 
					sys.exit()
		
		pygame.display.update()

	return jugar


def inicializarTablero():
	tablero=[[0 for x in range(0,8)] for y in range(0,8)]
	tablero[3][3]=2
	tablero[4][4]=2
	tablero[3][4]=1
	tablero[4][3]=1

	return tablero


def Jugadores():
	#Crear Ventana
	ancho,largo=800,600
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")


	#Colores
	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	
	TITULO=pygame.image.load("IMAGENES/TITULO.png")
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)


	
	jugadores=["",""]
	casilla_jug0=False
	casilla_jug1=False
	IntroducidoNombre0=False
	IntroducidoNombre1=False
	

	jugador1_V=fuente.render("JUGADOR 1:",1,BLANCO)#TEXTO DE CASILLA1
	jugador2_V=fuente.render("JUGADOR 2:",2,BLANCO)#TEXTO DE CASILLA2

	PosX,PosY=280,250
	ancho,largo=250,100

	casilla_jug0_inactive=pygame.draw.rect(VENTANA,GRIS,(PosX,PosY,ancho,largo),5)#CASILLA INACTIVA JUG1
	casilla_jug1_inactive=pygame.draw.rect(VENTANA,GRIS,(PosX,PosY+105,ancho,largo),5)#CASILLA INACTIVA JUG2
	

	while not(IntroducidoNombre0 and IntroducidoNombre1):

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos
				
				if casilla_jug0_inactive.collidepoint(x,y):
					casilla_jug0=True
					casilla_jug1=False
				
				elif casilla_jug1_inactive.collidepoint(x,y):
					
					casilla_jug1=True
					casilla_jug0=False
				
				else:
					casilla_jug0=False
					casilla_jug1=False

			elif event.type==pygame.KEYDOWN:
				if casilla_jug0 and not(IntroducidoNombre0):
					if event.key == pygame.K_BACKSPACE:
						jugadores[0] = jugadores[0][:-1]
					
					elif event.key==pygame.K_RETURN:
						casilla_jug0=False
						IntroducidoNombre0=True
						casilla_jug1=True
						
					else:
						jugadores[0]+=event.unicode
				
				elif casilla_jug1 and not(IntroducidoNombre1):
					if event.key == pygame.K_BACKSPACE:
						jugadores[1] = jugadores[1][:-1]
					elif event.key==pygame.K_RETURN:
						casilla_jug1=False
						IntroducidoNombre1=True

					else:
						jugadores[1]+=event.unicode

				
		VENTANA.blit(FONDO,(0,0))
		VENTANA.blit(TITULO,(120,10))
	
	
		VENTANA.blit(jugador1_V,(PosX+10,PosY+10))
		VENTANA.blit(jugador2_V,(PosX+10,PosY+115))

		
		VENTANA.blit((fuente.render(jugadores[0],1,VERDE)),(PosX+10,PosY+50))
		VENTANA.blit((fuente.render(jugadores[1],1,VERDE)),(PosX+10,PosY+165))
		


		if casilla_jug0:
			pygame.draw.rect(VENTANA,BLANCO,(PosX,PosY,ancho,largo),5)

		else:
			pygame.draw.rect(VENTANA,GRIS,(PosX,PosY,ancho,largo),5)

		
		if casilla_jug1:
			pygame.draw.rect(VENTANA,BLANCO,(PosX,PosY+105,ancho,largo),5)
			
		
		else:
			
			pygame.draw.rect(VENTANA,GRIS,(PosX,PosY+105,ancho,largo),5)


		if IntroducidoNombre0:
			pygame.draw.rect(VENTANA,VERDE,(PosX,PosY,ancho,largo),5)

		elif IntroducidoNombre1:
			pygame.draw.rect(VENTANA,VERDE,(PosX,PosY+105,ancho,largo),5)
		
		pygame.display.update()


	return jugadores


def CambiarTurno(turno:int):

	assert(0<turno<=2)
	
	if turno==1:
		turno+=1	

	elif turno==2:
		turno-=1

	assert(0<turno<=2)

	return turno


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


def TraducirJugada(x,y):
	
	
	letras='abcdefgh'	
	
	
	for i in range(0,8):
		if y==letras[i]:
			y=i
	
	x=x=int(x)-1
	return x,y


def realizarJugada(turno:int,A:[[int]],x:int,y:int):
	A[x][y]=turno


def TableroYPuntuacion(A:[[int]],jugadores:[str],FichasNegras:int,FichasBlancas:int,Validez:bool):

	assert(len(A)==8 and all(len(A[i])==8 for i in range(0,8)))
	
	ancho,largo=800,600
	

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	PUNTUACION=pygame.image.load("IMAGENES/PUNTUACION.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")
	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	

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
	#Texto jugada no valida

	VALIDEZ=fuente.render("Jugada Invalida",1,VERDE)
	
	#Pintar fondo de ventana
	VENTANA.blit(FONDO,(0,0))
	siguiente=False
	
	while not(siguiente):

		#Insertar imagenes del tablero (Casillas, fichas)
		TableroPosy=60

		for x in range(0,8):
			
			TableroPosx=60
			
			for y in range(0,8):
				
				if A[x][y]==0:

					VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
					
				
				elif A[x][y]==1:
					VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
					

				elif A[x][y]==2:
					VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))
					
				
				TableroPosx+=60	
			
			TableroPosy+=60

		#Instertar Numeros, y texto al tablero

		PosLetrasNumeros=80
		for i in range(0,8):

			VENTANA.blit(fuente.render(str(i+1),1,GRIS),(35,PosLetrasNumeros))
			VENTANA.blit(fuente.render(str(i+1),1,GRIS),(545,PosLetrasNumeros))		

			VENTANA.blit(letras[i],(PosLetrasNumeros,30))
			VENTANA.blit(letras[i],(PosLetrasNumeros,540))
			PosLetrasNumeros+=60

		#Tablero de puntuacion
		pygame.draw.rect(VENTANA,GRIS,(590,120,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,160,200,90),4)
		VENTANA.blit(PUNTUACION,(600,115))
		VENTANA.blit(fuente.render(str(jugadores[0])+": "+str(FichasNegras),1,VERDE),(600,170))
		VENTANA.blit(fuente.render(str(jugadores[1])+": "+str(FichasBlancas),1,VERDE),(600,210))

		SIGUIENTE_V=VENTANA.blit(SIGUIENTE,(580,400))

		#Error
		if not(Validez):
			VENTANA.blit(VALIDEZ,(580,350))



		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type==MOUSEBUTTONDOWN:
				x,y=event.pos
				if SIGUIENTE_V.collidepoint(x,y):
					siguiente=True
	
		pygame.display.update()

def obtenerJugada1(A:[[int]],jugadores:[str],turno):

	import time
	
	ancho,largo=800,600
	

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	TURNO=pygame.image.load("IMAGENES/TURNO.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")

	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	

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
	jugada=["",""]
	FILA=fuente.render("FILA ",1,GRIS)
	COLUMNA=fuente.render("Columna",1,BLANCO)

	
	while jugada[0]=="" or jugada[1]=="":
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type==pygame.KEYDOWN:
				if  jugada[0]=="":
					
					if event.key == pygame.K_BACKSPACE:
						pass
					
					elif event.key==pygame.K_RETURN:
						pass
						
					else:
						jugada[0]+=event.unicode

				else:
					if event.key == pygame.K_BACKSPACE:
						
						pass
					elif event.key==pygame.K_RETURN:
						pass
						
					else:
						jugada[1]+=event.unicode

		#Insertar imagenes del tablero (Casillas, fichas)
		TableroPosy=60

		for x in range(0,8):
			
			TableroPosx=60
			
			for y in range(0,8):
				
				if A[x][y]==0:

					VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
					
				
				elif A[x][y]==1:
					VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
					

				elif A[x][y]==2:
					VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))
					
				
				TableroPosx+=60	
			
			TableroPosy+=60

		#Instertar Numeros, y texto al tablero

		PosLetrasNumeros=80
		for i in range(0,8):

			VENTANA.blit(fuente.render(str(i+1),1,GRIS),(35,PosLetrasNumeros))
			VENTANA.blit(fuente.render(str(i+1),1,GRIS),(545,PosLetrasNumeros))		

			VENTANA.blit(letras[i],(PosLetrasNumeros,30))
			VENTANA.blit(letras[i],(PosLetrasNumeros,540))
			PosLetrasNumeros+=60

		#Tablero de Turno
		
		#Casilla turno
		pygame.draw.rect(VENTANA,GRIS,(590,120,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,160,200,90),4)
		VENTANA.blit(TURNO,(630,115))


		#Casilla Fila 
		FILA_V=pygame.draw.rect(VENTANA,GRIS,(590,300,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,300,150,40),4)
		VENTANA.blit(FILA,(600,310))
		VENTANA.blit(fuente.render(jugada[0],1,VERDE),(760,310))
		
		#Casilla columna
		COLUMNA_V=pygame.draw.rect(VENTANA,GRIS,(590,340,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,340,150,40),4)
		VENTANA.blit(fuente.render(jugada[1],1,VERDE),(760,350))

		if turno==1:
			VENTANA.blit(fuente.render(str(jugadores[0]),1,VERDE),(600,180))
		else:
			VENTANA.blit(fuente.render(str(jugadores[1]),1,VERDE),(600,180))

		pygame.display.update()

	time.sleep(0.3)

	return jugada[0],jugada[1]

def obtenerJugada2(A:[[int]],jugadores:[str],turno):
	
	#Inicializar arreglo para almacenar casillas
	TABLERO_POS=[[0 for x in range(0,8)] for y in range(0,8)]
	ancho,largo=800,600
	

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	TURNO=pygame.image.load("IMAGENES/TURNO.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")

	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	

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
	jugada=False
	
	while not(jugada):

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

		PosLetrasNumeros=80
		for i in range(0,8):

			VENTANA.blit(fuente.render(str(i+1),1,GRIS),(35,PosLetrasNumeros))
			VENTANA.blit(fuente.render(str(i+1),1,GRIS),(545,PosLetrasNumeros))		

			VENTANA.blit(letras[i],(PosLetrasNumeros,30))
			VENTANA.blit(letras[i],(PosLetrasNumeros,540))
			PosLetrasNumeros+=60

		#Tablero de puntuacion
		pygame.draw.rect(VENTANA,GRIS,(590,120,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,160,200,90),4)
		VENTANA.blit(TURNO,(630,115))

		if turno==1:
			VENTANA.blit(fuente.render(str(jugadores[0]),1,VERDE),(600,180))
		else:
			VENTANA.blit(fuente.render(str(jugadores[1]),1,VERDE),(600,180))


		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type==MOUSEBUTTONDOWN:
				x,y=event.pos
				for i in range(0,8):
					for j in range(0,8):
						if TABLERO_POS[i][j].collidepoint(x,y) and A[i][j]==0:
							jugada=True
							x,y=i,j
	
		pygame.display.update()

	return x,y




##PROGRAMA PRINCIPAL


import pygame,sys
from pygame.locals import *

pygame.init()


while DeseaJugar():
		
		tablero=inicializarTablero()
		turno=1
		jugadores=Jugadores()
		TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)		

		while TotalFichas>0:
			
			x,y=obtenerJugada1(tablero,jugadores,turno)
			x,y=TraducirJugada(x,y)	####FUNCION AUXILIAR, MIENTRAS NO TENGAMOS LA DE ES VALIDA
			 
			validez=True			###LLAMADA A LA FUNCION ES VALIDA
			
			if validez:				##SI LA JUGADA ES VALIDA, REALIZA JUGADA, CONSUME FICHA, CAMBIA TURNO
				realizarJugada(turno,tablero,x,y)
				TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
				###		FALTA FLANQUEO
				turno=CambiarTurno(turno)
			
			TableroYPuntuacion(tablero,jugadores,FichasNegras,FichasBlancas,validez)

		
		
		




