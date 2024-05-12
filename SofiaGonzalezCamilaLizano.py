import random
import sys
import time
from time import sleep
import pygame
from pygame import *

pygame.init() #Iniciando la libreria

sizeScreen= (950, 700) #Definiendo tamaño de ventana
tipografia = font.SysFont("Helvetica", 30, bold=True) #Tipografía
volumenGlobal = 1.0 #Volumen Global Inicial

# ----------------------------------- Iniciando la Ventana de Información -----------------------------------
def screenInformacion():
    tipografia = font.SysFont("Helvetica", 20, bold=True) #Tipografía
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaInformacion = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaInformacion = pygame.image.load("Imagenes//fondoinfcs.png") #Agregando fondo de pantalla de Información
    ventanaInformacion.blit(fondoVentanaInformacion, (0,0)) #Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45))  #Ajustando el tamaño
    ventanaInformacion.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
    # ---- Imágen de las autoras ----
    imagenCami = pygame.image.load("Imagenes//cami.png") #Agregando imagen Camila
    imagenCami = pygame.transform.scale(imagenCami, (200, 180))  #Ajustando el tamaño
    ventanaInformacion.blit(imagenCami, (250,70)) #Visualizar la imagen con su posición
    imagenSofi = pygame.image.load("Imagenes//Sofi.png") #Agregando imagen Sofía
    imagenSofi = pygame.transform.scale(imagenSofi, (200, 180))  #Ajustando el tamaño
    ventanaInformacion.blit(imagenSofi, (500,70)) #Visualizar la imagen con su posición
    # ---- Creando Textos ----
    # ---- CAMILA ----
    nombre1 = tipografia.render("Camila Lizano Brenes", True, ("#000000")) #Indicando mi nombre
    ventanaInformacion.blit(nombre1, (265, 250)) #Reflejando el texto
    cedula1 = tipografia.render("Cédula: 119390227", True, ("#000000")) #Indicando mi cédula
    ventanaInformacion.blit(cedula1, (275, 270)) #Reflejando el texto
    carnet1 = tipografia.render("Carné: 2024255324", True, ("#000000")) #Indicando mi carnet
    ventanaInformacion.blit(carnet1, (273, 290)) #Reflejando el texto
    # ---- SOFÍA ----
    nombre2 = tipografia.render("Sofía González Rubí", True, ("#000000")) #Indicando mi nombre
    ventanaInformacion.blit(nombre2, (520, 250)) #Reflejando el texto
    cedula2 = tipografia.render("Cédula: 119700990", True, ("#000000")) #Indicando mi cédula
    ventanaInformacion.blit(cedula2, (525, 270)) #Reflejando el texto
    carnet2 = tipografia.render("Carné: 2024211034", True, ("#000000")) #Indicando mi carnet
    ventanaInformacion.blit(carnet2, (525, 290)) #Reflejando el texto
    # ---- GENERAL ----
    profesor = tipografia.render("Nombre de Profesor: Luis Barboza", True, ("#000000")) #Indicando el nombre del profesor
    ventanaInformacion.blit(profesor, (340, 325)) #Reflejando el texto
    carrera = tipografia.render("Carrera: Ingeniería en Computadores", True, ("#000000")) #Indicando mi carrera
    ventanaInformacion.blit(carrera, (330, 345)) #Reflejando el texto
    asignatura = tipografia.render("Curso: Fundamentos Computacionales", True, ("#000000")) #Indicando la asignatura
    ventanaInformacion.blit(asignatura, (320, 365)) #Reflejando el texto
    institucion = tipografia.render("Tecnológico de Costa Rica, campus Central", True, ("#000000")) #Indicando la institución
    ventanaInformacion.blit(institucion, (300, 385)) #Reflejando el texto
    pais = tipografia.render("Costa Rica", True, ("#000000")) #Indicando el país
    ventanaInformacion.blit(pais, (205, 420)) #Reflejando el texto
    version = tipografia.render("Python 3.12.2", True, ("#000000")) #Indicando la versión de python
    ventanaInformacion.blit(version, (640, 420)) #Reflejando el texto
    # ---- ACERCA DEL JUEGO ----
    titulo = tipografia.render("Acerca del Juego", True, ("#000000")) #Indicando el título de acerca del juego
    ventanaInformacion.blit(titulo, (410, 465)) #Reflejando el texto
    # ---- Bucle de la ventana de Información ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                return #Cerrar juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                    if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                        screenPrincipal(volumenGlobal) #Ir a ventana principal
        pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Información ---------------------------------

# ----------------------------------- Iniciando la Ventana de Configuración -----------------------------------
equipoSeleccionado = None
enSeleccionEquipo = False
equipo = 1
def screenConfiguracion():
    global equipo
    global equipoSeleccionado #Globalizando mi variable para el equipo del personaje
    global enSeleccionEquipo #Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaConfiguracion = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaConfiguracion = pygame.image.load("Imagenes//fondoconf.png") #Agregando fondo de pantalla de Configuración
    ventanaConfiguracion.blit(fondoVentanaConfiguracion, (0,0)) #Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
    ventanaConfiguracion.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
    # ---- Imágen de los Equipos ----
    imagenArgentina = pygame.image.load("Imagenes//Argentina.png") #Agregando imagen Argentina
    imagenArgentina = pygame.transform.scale(imagenArgentina, (250, 260)) #Ajustando el tamaño
    ventanaConfiguracion.blit(imagenArgentina, (100,200)) #Visualizar la imagen con su posición
    imagenBarcelona = pygame.image.load("Imagenes//Barcelona.png") #Agregando imagen Barcelona
    imagenBarcelona = pygame.transform.scale(imagenBarcelona, (250, 260)) #Ajustando el tamaño
    ventanaConfiguracion.blit(imagenBarcelona, (350,200)) #Visualizar la imagen con su posición
    imagenBayern = pygame.image.load("Imagenes//Bayern.png") #Agregando imagen Bayern
    imagenBayern = pygame.transform.scale(imagenBayern, (250, 260)) #Ajustando el tamaño
    ventanaConfiguracion.blit(imagenBayern, (600,200)) #Visualizar la imagen con su posición
    
    # ---- Creando Botones para la Selección del Equipo ----
    # ---- Cargando las imágenes de los botones ----
    # ---- Imágenes Seleccionadas ----
    equipo = 1
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//Seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaConfiguracion.blit(imagenSeleccionadaOpcion1, (190,470)) #Visualizar la imagen con su posición
    equipo = 2
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//Seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaConfiguracion.blit(imagenSeleccionadaOpcion2, (440,470)) #Visualizar la imagen con su posición
    equipo = 3
    imagenSeleccionadaOpcion3 = pygame.image.load("Imagenes//Seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion3 = pygame.transform.scale(imagenSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaConfiguracion.blit(imagenSeleccionadaOpcion3, (690,470)) #Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenNoSeleccionadaOpcion1 = pygame.image.load("Imagenes//SinSeleccionar.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion1 = pygame.transform.scale(imagenNoSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaConfiguracion.blit(imagenNoSeleccionadaOpcion1, (190,470)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion2 = pygame.image.load("Imagenes//SinSeleccionar.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion2 = pygame.transform.scale(imagenNoSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaConfiguracion.blit(imagenNoSeleccionadaOpcion2, (440,470)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion3 = pygame.image.load("Imagenes//SinSeleccionar.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion3 = pygame.transform.scale(imagenNoSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaConfiguracion.blit(imagenNoSeleccionadaOpcion3, (690,470)) #Visualizar la imagen con su posición
    # ---- Imágenes de Botón de Confirmación ----
    imagenConfirmar = pygame.image.load("Imagenes//Confirmar.png") #Agregando Imagen representativa del botón no seleccionado
    imagenConfirmar = pygame.transform.scale(imagenConfirmar, (180, 140)) #Ajustando el tamaño
    botonConfirmar = ventanaConfiguracion.blit(imagenConfirmar, (390,525)) #Visualizar la imagen con su posición
    # ---- Estableciendo el estado inicial de selección donde todas están apagadas (no seleccionadas) ----
    opcion1Seleccionada = False
    opcion2Seleccionada = False
    opcion3Seleccionada = False
    # ---- Bucle de la ventana de Configuración ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                return #Cerrar juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                    if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                        screenPrincipal(volumenGlobal) #Ir a ventana principal
                    elif (posicionOpcion1.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 1
                        opcion1Seleccionada = True #Encendido
                        opcion2Seleccionada = False #Apagado
                        opcion3Seleccionada = False #Apagado
                        equipoSeleccionado = 1 #Guardando la skin seleccionada
                    elif (posicionOpcion2.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 2
                        opcion1Seleccionada = False #Apagado
                        opcion2Seleccionada = True #Encendido
                        opcion3Seleccionada = False #Apagado
                        equipoSeleccionado = 2 #Guardando la skin seleccionada
                    elif (posicionOpcion3.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1Seleccionada = False #Apagado
                        opcion2Seleccionada = False #Apagado
                        opcion3Seleccionada = True #Encendido
                        equipoSeleccionado = 3 #Guardando la skin seleccionada
                    elif (botonConfirmar.collidepoint(event.pos)): # Verificar si se presionó el botón de confirmar
                        if (equipoSeleccionado == 1):
                            enSeleccionEquipo = True
                            screenSeleccion1()
                        elif (equipoSeleccionado == 2):
                            enSeleccionEquipo = True
                            screenSeleccion2()
                        elif (equipoSeleccionado == 3):
                            enSeleccionEquipo = True
                            screenSeleccion3()
                        else:
                            screenConfiguracion() #Si no se ha seleccionado ningún equipo, simplemente permanece en la ventana de configuración
        # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
        if not enSeleccionEquipo:
            ventanaConfiguracion.blit(imagenSeleccionadaOpcion1 if opcion1Seleccionada else imagenNoSeleccionadaOpcion1, posicionOpcion1)
            ventanaConfiguracion.blit(imagenSeleccionadaOpcion2 if opcion2Seleccionada else imagenNoSeleccionadaOpcion2, posicionOpcion2)
            ventanaConfiguracion.blit(imagenSeleccionadaOpcion3 if opcion3Seleccionada else imagenNoSeleccionadaOpcion3, posicionOpcion3)
        pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Configuración ---------------------------------

# ----------------------------------- Iniciando la Ventana de Selección 1 -----------------------------------
jugadores = 1
porteros = 1
def screenSeleccion1():
        global enSeleccionEquipo #Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
        global jugadores, porteros
        pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
        ventanaSeleccion1 = pygame.display.set_mode(sizeScreen) #Creación de Ventana
        fondoVentanaSeleccion2 = pygame.image.load("Imagenes//fondoSeleccion.png") #Agregando fondo de pantalla de Selección 1
        ventanaSeleccion1.blit(fondoVentanaSeleccion2, (0,0)) #Visualizar el fondo
        # ---- Botón de Regreso ----
        botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
        botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
        ventanaSeleccion1.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
        # ---- Imágen de los jugadores ----
        imagenDiMaria = pygame.image.load("Imagenes//Di María.png") #Agregando imagen de Di María
        imagenDiMaria = pygame.transform.scale(imagenDiMaria, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenDiMaria, (100,130)) #Visualizar la imagen con su posición
        imagenMessi = pygame.image.load("Imagenes//messi.png") #Agregando imagen de Messi
        imagenMessi = pygame.transform.scale(imagenMessi, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMessi, (360,130)) #Visualizar la imagen con su posición
        imagenMusiala = pygame.image.load("Imagenes//dybala.png") #Agregando imagen de Dybala
        imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMusiala, (615,130)) #Visualizar la imagen con su posición
        # ---- Imágen de los botones de selección jugadores----
        # ---- Imágenes Seleccionadas ----
        jugadores = 1
        imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
        posicionOpcion1 = ventanaSeleccion1.blit(imagenSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
        jugadores = 2
        imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
        posicionOpcion2 = ventanaSeleccion1.blit(imagenSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
        jugadores = 3
        imagenSeleccionadaOpcion3 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionadaOpcion3 = pygame.transform.scale(imagenSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
        posicionOpcion3 = ventanaSeleccion1.blit(imagenSeleccionadaOpcion3, (800,180)) #Visualizar la imagen con su posición
        # ---- Imágenes No Seleccionadas ----
        imagenNoSeleccionadaOpcion1 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
        imagenNoSeleccionadaOpcion1 = pygame.transform.scale(imagenNoSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
        posicionOpcion1 = ventanaSeleccion1.blit(imagenNoSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
        imagenNoSeleccionadaOpcion2 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
        imagenNoSeleccionadaOpcion2 = pygame.transform.scale(imagenNoSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
        posicionOpcion2 = ventanaSeleccion1.blit(imagenNoSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
        imagenNoSeleccionadaOpcion3 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
        imagenNoSeleccionadaOpcion3 = pygame.transform.scale(imagenNoSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
        posicionOpcion3 = ventanaSeleccion1.blit(imagenNoSeleccionadaOpcion3, (800,180)) #Visualizar la imagen con su posición
        # ---- Imágen de los porteros ----
        imagenKane = pygame.image.load("Imagenes//Emiliano Martínez.png") #Agregando imagen de Martínez
        imagenKane = pygame.transform.scale(imagenKane, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenKane, (100,432)) #Visualizar la imagen con su posición
        imagenMuller = pygame.image.load("Imagenes//Gerónimo Rulli.png") #Agregando imagen de Rulli
        imagenMuller = pygame.transform.scale(imagenMuller, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMuller, (360,432)) #Visualizar la imagen con su posición
        imagenMusiala = pygame.image.load("Imagenes//Franco Armani.png") #Agregando imagen de Armani
        imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMusiala, (615,432)) #Visualizar la imagen con su posición
        # ---- Imágen de los botones de selección porteros----
        # ---- Imágenes Seleccionadas ----
        porteros = 1
        imagenSeleccionada1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
        posicionOpcion1Por = ventanaSeleccion1.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
        porteros = 2
        imagenSeleccionada2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
        posicionOpcion2Por = ventanaSeleccion1.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
        porteros = 3
        imagenSeleccionada3 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70)) #Ajustando el tamaño
        posicionOpcion3Por = ventanaSeleccion1.blit(imagenSeleccionada3, (800,482)) #Visualizar la imagen con su posición
        # ---- Imágenes No Seleccionadas ----
        imagenSeleccionada1 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
        posicionOpcion1Por = ventanaSeleccion1.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
        imagenSeleccionada2 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
        posicionOpcion2Por = ventanaSeleccion1.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
        imagenSeleccionada3 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70)) #Ajustando el tamaño
        posicionOpcion3Por = ventanaSeleccion1.blit(imagenSeleccionada3, (800,482)) #Visualizar la imagen con su posición
        # ---- Estableciendo el estado inicial de selección donde todas están apagadas (no seleccionadas) ----
        opcion1SeleccionadaJugadores = False
        opcion2SeleccionadaJugadores = False
        opcion3SeleccionadaJugadores = False
        opcion1SeleccionadaPorteros = False
        opcion2SeleccionadaPorteros = False
        opcion3SeleccionadaPorteros = False
        # ---- Bucle de la ventana de Selección 3 ----
        while True:
            for event in pygame.event.get(): #Iterando sobre eventos
                if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                    return #Cerrar juego
                elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                    if (event.button == 1): #Verificar si fue clic izquierdo
                        x, y = event.pos #Guardando en variables donde se hizo clic
                        # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                        if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                            enSeleccionEquipo = False
                            screenConfiguracion() #Ir a ventana principal
                        elif (posicionOpcion1.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 1
                            opcion1SeleccionadaJugadores = True #Encendido
                            opcion2SeleccionadaJugadores = False #Apagado
                            opcion3SeleccionadaJugadores = False #Apagado
                        elif (posicionOpcion2.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 2
                            opcion1SeleccionadaJugadores = False #Apagado
                            opcion2SeleccionadaJugadores = True #Encendido
                            opcion3SeleccionadaJugadores = False #Apagado
                        elif (posicionOpcion3.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaJugadores = False #Apagado
                            opcion2SeleccionadaJugadores = False #Apagado
                            opcion3SeleccionadaJugadores = True #Encendido
                        elif (posicionOpcion1Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaPorteros = True #Encendido
                            opcion2SeleccionadaPorteros = False #Apagado
                            opcion3SeleccionadaPorteros = False #Apagado
                        elif (posicionOpcion2Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaPorteros = False #Apagado
                            opcion2SeleccionadaPorteros = True #Encendido
                            opcion3SeleccionadaPorteros = False #Apagado
                        elif (posicionOpcion3Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaPorteros = False #Apagado
                            opcion2SeleccionadaPorteros = False #Apagado
                            opcion3SeleccionadaPorteros = True #Encendido
                # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadores else imagenNoSeleccionadaOpcion1, posicionOpcion1)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadores else imagenNoSeleccionadaOpcion2, posicionOpcion2)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadores else imagenNoSeleccionadaOpcion3, posicionOpcion3)
                # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorteros else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorteros else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorteros else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
            pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Selección 1 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Selección 2 -----------------------------------
def screenSeleccion2():
    global enSeleccionEquipo  # Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
    global jugadores,porteros
    pygame.mixer.music.set_volume(volumenGlobal)  # Manteniendo el volumen
    ventanaSeleccion2 = pygame.display.set_mode(sizeScreen)  # Creación de Ventana
    fondoVentanaSeleccion2 = pygame.image.load("Imagenes//fondoSeleccion.png")  # Agregando fondo de pantalla de Selección 1
    ventanaSeleccion2.blit(fondoVentanaSeleccion2, (0, 0))  # Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png")  # Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45))  # Ajustando el tamaño
    ventanaSeleccion2.blit(botonRegreso, (10, 10))  # Visualizar la imagen con su posición
    # ---- Imágen de los jugadores ----
    imagenKane = pygame.image.load("Imagenes//Raphinha.png")  # Agregando imagen de Raphinha
    imagenKane = pygame.transform.scale(imagenKane, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenKane, (100, 130))  # Visualizar la imagen con su posición
    imagenMuller = pygame.image.load("Imagenes//RobertLewandowski.png")  # Agregando imagen de Lewandowski
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMuller, (360, 130))  # Visualizar la imagen con su posición
    imagenMusiala = pygame.image.load("Imagenes//FerranTorres.png")  # Agregando imagen de Torres
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMusiala, (615, 130))  # Visualizar la imagen con su posición
    # ---- Imágen de los botones de selección jugadores----
    # ---- Imágenes Seleccionadas ----
    jugadores = 4
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//encendido.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70))  # Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion2.blit(imagenSeleccionadaOpcion1, (280, 180))  # Visualizar la imagen con su posición
    jugadores = 5
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//encendido.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70))  # Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion2.blit(imagenSeleccionadaOpcion2, (540, 180))  # Visualizar la imagen con su posición
    jugadores = 6
    imagenSeleccionadaOpcion3 = pygame.image.load("Imagenes//encendido.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion3 = pygame.transform.scale(imagenSeleccionadaOpcion3, (70, 70))  # Ajustando el tamaño
    posicionOpcion3 = ventanaSeleccion2.blit(imagenSeleccionadaOpcion3, (800, 180))  # Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenNoSeleccionadaOpcion1 = pygame.image.load("Imagenes//apagado.png")  # Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion1 = pygame.transform.scale(imagenNoSeleccionadaOpcion1, (70, 70))  # Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion2.blit(imagenNoSeleccionadaOpcion1, (280, 180))  # Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion2 = pygame.image.load("Imagenes//apagado.png")  # Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion2 = pygame.transform.scale(imagenNoSeleccionadaOpcion2, (70, 70))  # Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion2.blit(imagenNoSeleccionadaOpcion2, (540, 180))  # Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion3 = pygame.image.load("Imagenes//apagado.png")  # Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion3 = pygame.transform.scale(imagenNoSeleccionadaOpcion3, (70, 70))  # Ajustando el tamaño
    posicionOpcion3 = ventanaSeleccion2.blit(imagenNoSeleccionadaOpcion3, (800, 180))  # Visualizar la imagen con su posición
    # ---- Imágen de los porteros ----
    imagenKane = pygame.image.load("Imagenes//Claudio Bravo.png")  # Agregando imagen de Bravo
    imagenKane = pygame.transform.scale(imagenKane, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenKane, (100, 432))  # Visualizar la imagen con su posición
    imagenMuller = pygame.image.load("Imagenes//IñakiPeña.png")  # Agregando imagen de Peña
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMuller, (360, 432))  # Visualizar la imagen con su posición
    imagenMusiala = pygame.image.load("Imagenes//Stegen.png")  # Agregando imagen de Stegen
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMusiala, (615, 432))  # Visualizar la imagen con su posición
    # ---- Imágen de los botones de selección porteros----
    # ---- Imágenes Seleccionadas ----
    porteros = 4
    imagenSeleccionada1 = pygame.image.load("Imagenes//encendido.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70))  # Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion2.blit(imagenSeleccionada1, (280, 482))  # Visualizar la imagen con su posición
    porteros = 5
    imagenSeleccionada2 = pygame.image.load("Imagenes//encendido.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70))  # Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion2.blit(imagenSeleccionada2, (540, 482))  # Visualizar la imagen con su posición
    porteros = 6
    imagenSeleccionada3 = pygame.image.load("Imagenes//encendido.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70))  # Ajustando el tamaño
    posicionOpcion3Por = ventanaSeleccion2.blit(imagenSeleccionada3, (800, 482))  # Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenSeleccionada1 = pygame.image.load("Imagenes//apagado.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70))  # Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion2.blit(imagenSeleccionada1, (280, 482))  # Visualizar la imagen con su posición
    imagenSeleccionada2 = pygame.image.load("Imagenes//apagado.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70))  # Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion2.blit(imagenSeleccionada2, (540, 482))  # Visualizar la imagen con su posición
    imagenSeleccionada3 = pygame.image.load("Imagenes//apagado.png")  # Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70))  # Ajustando el tamaño
    posicionOpcion3Por = ventanaSeleccion2.blit(imagenSeleccionada3, (800, 482))  # Visualizar la imagen con su posición
    # ---- Estableciendo el estado inicial de selección donde todas están apagadas (no seleccionadas) ----
    opcion1SeleccionadaJugadores = False
    opcion2SeleccionadaJugadores = False
    opcion3SeleccionadaJugadores = False
    opcion1SeleccionadaPorteros = False
    opcion2SeleccionadaPorteros = False
    opcion3SeleccionadaPorteros = False
    # ---- Bucle de la ventana de Selección 3 ----
    while True:
        for event in pygame.event.get():  # Iterando sobre eventos
            if event.type == pygame.QUIT:  # Si usuario intenta cerrar ventana:
                return  # Cerrar juego
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                if event.button == 1:  # Verificar si fue clic izquierdo
                    x, y = event.pos  # Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                    if 15 < x < 65 and 15 < y < 65:  # Botón de Regreso
                        enSeleccionEquipo = False
                        screenConfiguracion()  # Ir a ventana principal
                    elif posicionOpcion1.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 1
                        opcion1SeleccionadaJugadores = True  # Encendido
                        opcion2SeleccionadaJugadores = False  # Apagado
                        opcion3SeleccionadaJugadores = False  # Apagado
                    elif posicionOpcion2.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 2
                        opcion1SeleccionadaJugadores = False  # Apagado
                        opcion2SeleccionadaJugadores = True  # Encendido
                        opcion3SeleccionadaJugadores = False  # Apagado
                    elif posicionOpcion3.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaJugadores = False  # Apagado
                        opcion2SeleccionadaJugadores = False  # Apagado
                        opcion3SeleccionadaJugadores = True  # Encendido
                    elif posicionOpcion1Por.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorteros = True  # Encendido
                        opcion2SeleccionadaPorteros = False  # Apagado
                        opcion3SeleccionadaPorteros = False  # Apagado
                    elif posicionOpcion2Por.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorteros = False  # Apagado
                        opcion2SeleccionadaPorteros = True  # Encendido
                        opcion3SeleccionadaPorteros = False  # Apagado
                    elif posicionOpcion3Por.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorteros = False  # Apagado
                        opcion2SeleccionadaPorteros = False  # Apagado
                        opcion3SeleccionadaPorteros = True  # Encendido
        # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadores else imagenNoSeleccionadaOpcion1, posicionOpcion1)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadores else imagenNoSeleccionadaOpcion2, posicionOpcion2)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadores else imagenNoSeleccionadaOpcion3, posicionOpcion3)
        # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorteros else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorteros else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorteros else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
        pygame.display.flip()  # Actualizar Pantalla

# ----------------------------------- Finalizando la Ventana de Selección 2 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Selección 3 -----------------------------------
def screenSeleccion3():
    global enSeleccionEquipo #Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
    global jugadores, porteros
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaSeleccion3 = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaSeleccion3 = pygame.image.load("Imagenes//fondoSeleccion.png") #Agregando fondo de pantalla de Selección 1
    ventanaSeleccion3.blit(fondoVentanaSeleccion3, (0,0)) #Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
    ventanaSeleccion3.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
    # ---- Imágen de los jugadores ----
    imagenKane = pygame.image.load("Imagenes//HarryKane.png") #Agregando imagen de Kane
    imagenKane = pygame.transform.scale(imagenKane, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenKane, (100,130)) #Visualizar la imagen con su posición
    imagenMuller = pygame.image.load("Imagenes//ThomasMuller.PNG") #Agregando imagen de Muller
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenMuller, (360,130)) #Visualizar la imagen con su posición
    imagenMusiala = pygame.image.load("Imagenes//JamalMusiala.PNG") #Agregando imagen de Musiala
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenMusiala, (615,130)) #Visualizar la imagen con su posición
    # ---- Imágen de los botones de selección jugadores----
    # ---- Imágenes Seleccionadas ----
    jugadores = 7
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion3.blit(imagenSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
    jugadores = 8
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion3.blit(imagenSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
    jugadores = 9
    imagenSeleccionadaOpcion3 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion3 = pygame.transform.scale(imagenSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaSeleccion3.blit(imagenSeleccionadaOpcion3, (800,180)) #Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenNoSeleccionadaOpcion1 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion1 = pygame.transform.scale(imagenNoSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion3.blit(imagenNoSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion2 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion2 = pygame.transform.scale(imagenNoSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion3.blit(imagenNoSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion3 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion3 = pygame.transform.scale(imagenNoSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaSeleccion3.blit(imagenNoSeleccionadaOpcion3, (800,180)) #Visualizar la imagen con su posición
    # ---- Imágen de los porteros ----
    imagenKane = pygame.image.load("Imagenes//ManuelNeuer.PNG") #Agregando imagen de Neuer
    imagenKane = pygame.transform.scale(imagenKane, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenKane, (100,432)) #Visualizar la imagen con su posición
    imagenMuller = pygame.image.load("Imagenes//SvenUlreich.PNG") #Agregando imagen de Ulreicj
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenMuller, (360,432)) #Visualizar la imagen con su posición
    imagenMusiala = pygame.image.load("Imagenes//DanielPeretz.PNG") #Agregando imagen de Peretz
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenMusiala, (615,432)) #Visualizar la imagen con su posición
    # ---- Imágen de los botones de selección porteros----
    # ---- Imágenes Seleccionadas ----
    porteros = 7
    imagenSeleccionada1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion3.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
    porteros = 8
    imagenSeleccionada2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion3.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
    porteros = 9
    imagenSeleccionada3 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3Por = ventanaSeleccion3.blit(imagenSeleccionada3, (800,482)) #Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenSeleccionada1 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion3.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
    imagenSeleccionada2 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion3.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
    imagenSeleccionada3 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3Por = ventanaSeleccion3.blit(imagenSeleccionada3, (800,482)) #Visualizar la imagen con su posición
    # ---- Estableciendo el estado inicial de selección donde todas están apagadas (no seleccionadas) ----
    opcion1SeleccionadaJugadores = False
    opcion2SeleccionadaJugadores = False
    opcion3SeleccionadaJugadores = False
    opcion1SeleccionadaPorteros = False
    opcion2SeleccionadaPorteros = False
    opcion3SeleccionadaPorteros = False
    # ---- Bucle de la ventana de Selección 3 ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                return #Cerrar juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                    if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                        enSeleccionEquipo = False
                        screenConfiguracion() #Ir a ventana principal
                    elif (posicionOpcion1.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 1
                        opcion1SeleccionadaJugadores = True #Encendido
                        opcion2SeleccionadaJugadores = False #Apagado
                        opcion3SeleccionadaJugadores = False #Apagado
                    elif (posicionOpcion2.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 2
                        opcion1SeleccionadaJugadores = False #Apagado
                        opcion2SeleccionadaJugadores = True #Encendido
                        opcion3SeleccionadaJugadores = False #Apagado
                    elif (posicionOpcion3.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaJugadores = False #Apagado
                        opcion2SeleccionadaJugadores = False #Apagado
                        opcion3SeleccionadaJugadores = True #Encendido
                    elif (posicionOpcion1Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorteros = True #Encendido
                        opcion2SeleccionadaPorteros = False #Apagado
                        opcion3SeleccionadaPorteros = False #Apagado
                    elif (posicionOpcion2Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorteros = False #Apagado
                        opcion2SeleccionadaPorteros = True #Encendido
                        opcion3SeleccionadaPorteros = False #Apagado
                    elif (posicionOpcion3Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorteros = False #Apagado
                        opcion2SeleccionadaPorteros = False #Apagado
                        opcion3SeleccionadaPorteros = True #Encendido
            # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadores else imagenNoSeleccionadaOpcion1, posicionOpcion1)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadores else imagenNoSeleccionadaOpcion2, posicionOpcion2)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadores else imagenNoSeleccionadaOpcion3, posicionOpcion3)
            # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorteros else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorteros else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorteros else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
        pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Selección 3 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Juego -----------------------------------
imagen_equipo = None
imagen_equipo_contrario = None
resultado_opuesto = None


def equiposelec(resultado_moneda):
    global imagen_equipo, imagen_equipo_contrario, resultado_opuesto
    if equipo == 1:
        imagen_equipo = pygame.image.load("Imagenes//Argentina.png")
        imagen_equipo_contrario = pygame.image.load("Imagenes//Bayern.png")
    elif equipo == 3:
        imagen_equipo = pygame.image.load("Imagenes//Barcelona.png")
        imagen_equipo_contrario = pygame.image.load("Imagenes//Argentina.png")
    else:
        imagen_equipo = pygame.image.load("Imagenes//Bayern.png")
        imagen_equipo_contrario = pygame.image.load("Imagenes//Barcelona.png")

    if resultado_moneda == "Local":
        resultado_opuesto = "Visitante"
    else:
        resultado_opuesto = "Local"

def jugadoressel():
    global imagen_equipo, imagen_equipo_contrario
    if equipo == 1:
        if jugadores == 1:
            imagen_equipo = pygame.image.load("Imagenes//messi.png")
        elif jugadores == 2:
            imagen_equipo = pygame.image.load("Imagenes//Di María.png")
        elif jugadores == 3:
            imagen_equipo = pygame.image.load("Imagenes//dybala.png")
        if porteros == 1:
            imagen_equipo_contrario = pygame.image.load("Imagenes//Emiliano Martínez.png")
        elif porteros == 2:
            imagen_equipo_contrario = pygame.image.load("Imagenes//Gerónimo Rulli.png")
        elif porteros == 3:
            imagen_equipo_contrario = pygame.image.load("Imagenes//Franco Armani.png")
    if equipo == 3:
        if jugadores == 4:
            imagen_equipo = pygame.image.load("Imagenes//Raphinha.png")
        elif jugadores == 5:
            imagen_equipo = pygame.image.load("Imagenes//RobertLewandowski.png")
        elif jugadores == 6:
            imagen_equipo = pygame.image.load("Imagenes//FerranTorres.png")
        if porteros == 4:
            imagen_equipo_contrario = pygame.image.load("Imagenes//Claudio Bravo.png")
        elif porteros == 5:
            imagen_equipo_contrario = pygame.image.load("Imagenes//IñakiPeña.png")
        elif porteros == 6:
            imagen_equipo_contrario = pygame.image.load("Imagenes//Stegen.png")
    if equipo == 2:
        if jugadores == 7:
            imagen_equipo = pygame.image.load("Imagenes//HarryKane.png")
        elif jugadores == 8:
            imagen_equipo = pygame.image.load("Imagenes//ThomasMuller.PNG")
        elif jugadores == 9:
            imagen_equipo = pygame.image.load("Imagenes//JamalMusiala.PNG")
        if porteros == 7:
            imagen_equipo_contrario = pygame.image.load("Imagenes//ManuelNeuer.PNG")
        elif porteros == 8:
            imagen_equipo_contrario = pygame.image.load("Imagenes//SvenUlreich.PNG")
        elif porteros == 9:
            imagen_equipo_contrario = pygame.image.load("Imagenes//DanielPeretz.PNG")

def screenJuego():
    global imagen_equipo, imagen_equipo_contrario, resultado_opuesto

    pygame.mixer.music.set_volume(volumenGlobal)  # Manteniendo el volumen

    # Creando la ventana
    ventanaJuego = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption("Sorteo")

    # Definir tamaño
    ANCHO = 800
    ALTO = 600

    # Cargar imagen de la moneda
    imagen_moneda = pygame.image.load("Imagenes//Moneda.png")
    imagen_moneda = pygame.transform.scale(imagen_moneda, (400, 400))  # Ajustando el tamaño

    # Cargar la imagen del botón
    imagen_boton = pygame.image.load("Imagenes//Confirmar.png")
    imagen_boton = pygame.transform.scale(imagen_boton, (100, 100))
    boton_rect = imagen_boton.get_rect()
    boton_rect.center = (sizeScreen[0] // 2, sizeScreen[1] // 1.2)

    # Definir la clase Moneda
    class Moneda(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = imagen_moneda
            self.rect = self.image.get_rect()
            self.rect.center = (ANCHO // 2, ALTO // 2)
            self.velocidad_rotacion = random.randint(3, 3)
            self.angulo = 0
            self.lanzada = False
            self.resultado = None

        def update(self):
            if self.lanzada:
                if self.angulo % 360 < 90 or self.angulo % 360 > 270:
                    self.resultado = "Local"
                    equiposelec(self.resultado)
                else:
                    self.resultado = "Visitante"
                    equiposelec(self.resultado)
            else:
                self.angulo += self.velocidad_rotacion
                self.image = pygame.transform.rotate(imagen_moneda, self.angulo)
                self.rect = self.image.get_rect(center=self.rect.center)

        def lanzar(self):
            self.lanzada = True

    # Crear grupo de sprites y agregar la moneda
    todos_los_sprites = pygame.sprite.Group()
    moneda = Moneda()
    todos_los_sprites.add(moneda)

    # Bucle principal del juego
    ejecutando = True
    reloj = pygame.time.Clock()

    # Nuevas variables para la posición y el tamaño de la imagen del equipo
    x_equipo = 50  # Nueva posición X de la imagen del equipo
    y_equipo = 50  # Nueva posición Y de la imagen del equipo
    ancho_equipo = 200  # Nuevo ancho de la imagen del equipo
    alto_equipo = 200  # Nuevo alto de la imagen del equipo

    x_equipo_contrario = 650  # Posición X de la imagen del equipo contrario
    y_equipo_contrario = 50  # Posición Y de la imagen del equipo contrario
    y_texto_contrario = y_equipo_contrario + alto_equipo + 10  # Posición Y del texto del equipo contrario

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not moneda.lanzada:
                    moneda.lanzar()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(evento.pos):  # Verificar si se hizo clic en el botón
                    mostrar_seleccion_final()

        # Actualizar la animación de la moneda
        todos_los_sprites.update()

        # Dibujar todo
        ventanaJuego.fill((255, 255, 255))

        # Dibujar la imagen del equipo en la nueva posición y tamaño
        if imagen_equipo:
            imagen_equipo_escalada = pygame.transform.scale(imagen_equipo, (ancho_equipo, alto_equipo))
            ventanaJuego.blit(imagen_equipo_escalada, (x_equipo, y_equipo))

        # Dibujar la imagen del equipo contrario
        if imagen_equipo_contrario:
            imagen_equipo_contrario_escalada = pygame.transform.scale(imagen_equipo_contrario,
                                                                      (ancho_equipo, alto_equipo))
            ventanaJuego.blit(imagen_equipo_contrario_escalada, (x_equipo_contrario, y_equipo_contrario))

        # Mostrar resultado opuesto debajo del equipo contrario
        if resultado_opuesto:
            fuente = pygame.font.Font(None, 24)
            texto_contrario = fuente.render(resultado_opuesto, True, ("#000000"))
            ventanaJuego.blit(texto_contrario, (
            x_equipo_contrario + ancho_equipo // 2 - texto_contrario.get_width() // 2, y_texto_contrario))

        todos_los_sprites.draw(ventanaJuego)

        # Mostrar resultado después de que la moneda haya aterrizado
        if moneda.lanzada and moneda.resultado is not None:
            fuente = pygame.font.Font(None, 28)
            texto = fuente.render(f"{moneda.resultado}", True, ("#000000"))
            ventanaJuego.blit(texto, (103,250))

        # Dibujar la imagen del botón en la posición definida
        ventanaJuego.blit(imagen_boton, boton_rect)

        pygame.display.flip()
        reloj.tick(60)

def mostrar_seleccion_final():
    pygame.mixer.music.set_volume(volumenGlobal)
    ventana_seleccionfinal = pygame.display.set_mode((sizeScreen))
    pygame.display.set_caption("Selección Final")

    jugadoressel()
    ejecutando_seleccionfinal = True


    # Definir las coordenadas y dimensiones del botón de confirmar
    boton_confirmar = pygame.Rect(375, 400, 200, 50)


    while ejecutando_seleccionfinal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando_seleccionfinal = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en el botón de confirmar
                if event.button == 1 and boton_confirmar.collidepoint(event.pos):
                    print("Confirma")


        ventana_seleccionfinal.fill((122, 186, 120))
        if imagen_equipo:
            ventana_seleccionfinal.blit(imagen_equipo, (75, 100))
        if imagen_equipo_contrario:
            ventana_seleccionfinal.blit(imagen_equipo_contrario, (575, 100))

        # Dibujar el botón de confirmar
        pygame.draw.rect(ventana_seleccionfinal, (122, 186, 120), boton_confirmar)

        # Dibujar el texto del botón de confirmar
        font = pygame.font.Font(None, 36)
        texto_confirmar = font.render("Confirmar", True, (255, 255, 255))
        texto_rect = texto_confirmar.get_rect(center=boton_confirmar.center)
        ventana_seleccionfinal.blit(texto_confirmar, texto_rect)

        pygame.display.flip()


# ----------------------------------- Finalizando la Ventana de Juego ---------------------------------

# ----------------------------------- Iniciando la Ventana de Principal -----------------------------------
def screenPrincipal(volumenGlobal):
    ventanaPrincipal = pygame.display.set_mode(sizeScreen) #Creando Ventana
    fondoVentanaPrincipal = pygame.image.load("Imagenes//fondoprincipalofut-cs.png") #Agregando fondo de pantalla principal
    ventanaPrincipal.blit(fondoVentanaPrincipal, (0,0)) #Visualizar el fondo
    pygame.mixer.music.load("Musica//musicaDeportiva.mp3") #Agregando música
    pygame.mixer.music.set_volume(volumenGlobal) #Establecer el volumen antes de reproducir la música
    pygame.mixer.music.play(-1) #Repitiendo el sonido de forma ilimitada

    # ---- Función para crear botones ----
    def creandoBotones(ventanaPrincipal, boton, palabra, color):
        pygame.draw.rect(ventanaPrincipal, ("#000000"), (boton.x - 2, boton.y - 2, boton.width + 4, boton.height + 4)) #Creando borde negro a los botones
        draw.rect(ventanaPrincipal, (color), boton, 0) #Dibujando el rectángulo en pantalla
        texto = tipografia.render(palabra, True, ("#000000")) #Creando los parámetros para el texto
        ventanaPrincipal.blit(texto, (boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2)) #Colocando texto sobre rectángulo y haciendo dinámica la posición del texto

    # ---- Medidas y Posiciones del rectángulo de los botones ----
    informacion = Rect(100,570,210,60) #X, Y, Ancho, Alto
    jugar = Rect(370,570,210,60) #X, Y, Ancho, Alto
    configuracion = Rect(640,570,210,60) #X, Y, Ancho, Alto

    # ---- Llamando a los Botones ----
    creandoBotones(ventanaPrincipal, informacion, "Información", "#0297b1")
    creandoBotones(ventanaPrincipal, configuracion, "Configuración", "#3eb887")
    creandoBotones(ventanaPrincipal, jugar, "Jugar", "#7ada57")

    # ---- Ícono del Juego ----
    pygame.display.set_caption("FUT-CS") # Poniendo nombre a la ventana
    icono = pygame.image.load("Imagenes//icono.png") # Agregando imagen del icono
    pygame.display.set_icon(icono) # Colocando el icono

    while True: # Bucle para ventana principal
        for event in pygame.event.get(): # Iterando sobre eventos
            if event.type == pygame.QUIT: # Si el usuario intenta cerrar ventana
                pygame.quit() # Saliendo del juego
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # Detectar clic del mouse
                if event.button == 1: # Verificar si fue clic izquierdo
                    x, y = event.pos # Guardando en variables donde se hizo clic
                    # Verificar si el clic fue dentro de alguno de los botones de la Ventana Principal
                    if informacion.collidepoint(event.pos):
                        ventanaPrincipal.fill("#000000") # Limpiando Ventana Principal
                        screenInformacion() # Ir a Ventana de Información
                    elif configuracion.collidepoint(event.pos):
                        ventanaPrincipal.fill("#000000") # Limpiando Ventana Principal
                        screenConfiguracion() # Ir a Ventana de Configuración
                    elif jugar.collidepoint(event.pos):
                        ventanaPrincipal.fill("#000000") # Limpiando Ventana Principal
                        screenJuego() # Ir a Ventana de Juego
        pygame.display.flip() # Actualizando Pantalla
# ----------------------------------- Finalizando la Ventana Principal -----------------------------------
screenPrincipal(volumenGlobal)
pygame.quit()
