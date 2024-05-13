import random
import sys
from time import sleep

import pygame
import pygame.time
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
        global opcion1SeleccionadaJugadoresArgentina, opcion2SeleccionadaJugadoresArgentina, opcion3SeleccionadaJugadoresArgentina
        global opcion1SeleccionadaPorterosArgentina, opcion2SeleccionadaPorterosArgentina, opcion3SeleccionadaPorterosArgentina
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
        imagenDybala = pygame.image.load("Imagenes//dybala.png") #Agregando imagen de Dybala
        imagenDybala = pygame.transform.scale(imagenDybala, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenDybala, (615,130)) #Visualizar la imagen con su posición
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
        imagenMartinez = pygame.image.load("Imagenes//Emiliano Martínez.png") #Agregando imagen de Martínez
        imagenMartinez = pygame.transform.scale(imagenMartinez, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMartinez, (100,432)) #Visualizar la imagen con su posición
        imagenRulli = pygame.image.load("Imagenes//Gerónimo Rulli.png") #Agregando imagen de Rulli
        imagenRulli = pygame.transform.scale(imagenRulli, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenRulli, (360,432)) #Visualizar la imagen con su posición
        imagenArmani = pygame.image.load("Imagenes//Franco Armani.png") #Agregando imagen de Armani
        imagenArmani = pygame.transform.scale(imagenArmani, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenArmani, (615,432)) #Visualizar la imagen con su posición
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
        opcion1SeleccionadaJugadoresArgentina = False
        opcion2SeleccionadaJugadoresArgentina = False
        opcion3SeleccionadaJugadoresArgentina = False
        opcion1SeleccionadaPorterosArgentina = False
        opcion2SeleccionadaPorterosArgentina = False
        opcion3SeleccionadaPorterosArgentina = False
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
                            opcion1SeleccionadaJugadoresArgentina = True #Encendido
                            opcion2SeleccionadaJugadoresArgentina = False #Apagado
                            opcion3SeleccionadaJugadoresArgentina = False #Apagado
                        elif (posicionOpcion2.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 2
                            opcion1SeleccionadaJugadoresArgentina = False #Apagado
                            opcion2SeleccionadaJugadoresArgentina = True #Encendido
                            opcion3SeleccionadaJugadoresArgentina = False #Apagado
                        elif (posicionOpcion3.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaJugadoresArgentina = False #Apagado
                            opcion2SeleccionadaJugadoresArgentina = False #Apagado
                            opcion3SeleccionadaJugadoresArgentina = True #Encendido
                        elif (posicionOpcion1Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaPorterosArgentina = True #Encendido
                            opcion2SeleccionadaPorterosArgentina = False #Apagado
                            opcion3SeleccionadaPorterosArgentina = False #Apagado
                        elif (posicionOpcion2Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaPorterosArgentina = False #Apagado
                            opcion2SeleccionadaPorterosArgentina = True #Encendido
                            opcion3SeleccionadaPorterosArgentina = False #Apagado
                        elif (posicionOpcion3Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                            opcion1SeleccionadaPorterosArgentina = False #Apagado
                            opcion2SeleccionadaPorterosArgentina = False #Apagado
                            opcion3SeleccionadaPorterosArgentina = True #Encendido
                # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadoresArgentina else imagenNoSeleccionadaOpcion1, posicionOpcion1)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadoresArgentina else imagenNoSeleccionadaOpcion2, posicionOpcion2)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadoresArgentina else imagenNoSeleccionadaOpcion3, posicionOpcion3)
                # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorterosArgentina else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorterosArgentina else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
                ventanaSeleccion1.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorterosArgentina else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
            pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Selección 1 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Selección 2 -----------------------------------
def screenSeleccion2():
    global opcion1SeleccionadaJugadoresBarcelona, opcion2SeleccionadaJugadoresBarcelona, opcion3SeleccionadaJugadoresBarcelona
    global opcion1SeleccionadaPorterosBarcelona, opcion2SeleccionadaPorterosBarcelona, opcion3SeleccionadaPorterosBarcelona
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
    imagenRaphinha = pygame.image.load("Imagenes//Raphinha.png")  # Agregando imagen de Raphinha
    imagenRaphinha = pygame.transform.scale(imagenRaphinha, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenRaphinha, (100, 130))  # Visualizar la imagen con su posición
    imagenRobertLewandowski = pygame.image.load("Imagenes//RobertLewandowski.png")  # Agregando imagen de Lewandowski
    imagenRobertLewandowski = pygame.transform.scale(imagenRobertLewandowski, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenRobertLewandowski, (360, 130))  # Visualizar la imagen con su posición
    imagenFerranTorres = pygame.image.load("Imagenes//FerranTorres.png")  # Agregando imagen de Torres
    imagenFerranTorres = pygame.transform.scale(imagenFerranTorres, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenFerranTorres, (615, 130))  # Visualizar la imagen con su posición
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
    imagenBravo = pygame.image.load("Imagenes//Claudio Bravo.png")  # Agregando imagen de Bravo
    imagenBravo = pygame.transform.scale(imagenBravo, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenBravo, (100, 432))  # Visualizar la imagen con su posición
    imagenPeña = pygame.image.load("Imagenes//IñakiPeña.png")  # Agregando imagen de Peña
    imagenPeña = pygame.transform.scale(imagenPeña, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenPeña, (360, 432))  # Visualizar la imagen con su posición
    imagenStegen = pygame.image.load("Imagenes//Stegen.png")  # Agregando imagen de Stegen
    imagenStegen = pygame.transform.scale(imagenStegen, (180, 175))  # Ajustando el tamaño
    ventanaSeleccion2.blit(imagenStegen, (615, 432))  # Visualizar la imagen con su posición
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
    opcion1SeleccionadaJugadoresBarcelona = False
    opcion2SeleccionadaJugadoresBarcelona = False
    opcion3SeleccionadaJugadoresBarcelona = False
    opcion1SeleccionadaPorterosBarcelona = False
    opcion2SeleccionadaPorterosBarcelona = False
    opcion3SeleccionadaPorterosBarcelona = False
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
                        opcion1SeleccionadaJugadoresBarcelona = True  # Encendido
                        opcion2SeleccionadaJugadoresBarcelona = False  # Apagado
                        opcion3SeleccionadaJugadoresBarcelona = False  # Apagado
                    elif posicionOpcion2.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 2
                        opcion1SeleccionadaJugadoresBarcelona = False  # Apagado
                        opcion2SeleccionadaJugadoresBarcelona = True  # Encendido
                        opcion3SeleccionadaJugadoresBarcelona = False  # Apagado
                    elif posicionOpcion3.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaJugadoresBarcelona = False  # Apagado
                        opcion2SeleccionadaJugadoresBarcelona = False  # Apagado
                        opcion3SeleccionadaJugadoresBarcelona = True  # Encendido
                    elif posicionOpcion1Por.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorterosBarcelona = True  # Encendido
                        opcion2SeleccionadaPorterosBarcelona = False  # Apagado
                        opcion3SeleccionadaPorterosBarcelona = False  # Apagado
                    elif posicionOpcion2Por.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorterosBarcelona = False  # Apagado
                        opcion2SeleccionadaPorterosBarcelona = True  # Encendido
                        opcion3SeleccionadaPorterosBarcelona = False  # Apagado
                    elif posicionOpcion3Por.collidepoint(event.pos):  # Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorterosBarcelona = False  # Apagado
                        opcion2SeleccionadaPorterosBarcelona = False  # Apagado
                        opcion3SeleccionadaPorterosBarcelona = True  # Encendido
        # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadoresBarcelona else imagenNoSeleccionadaOpcion1, posicionOpcion1)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadoresBarcelona else imagenNoSeleccionadaOpcion2, posicionOpcion2)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadoresBarcelona else imagenNoSeleccionadaOpcion3, posicionOpcion3)
        # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorterosBarcelona else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorterosBarcelona else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
        ventanaSeleccion2.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorterosBarcelona else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
        pygame.display.flip()  # Actualizar Pantalla

# ----------------------------------- Finalizando la Ventana de Selección 2 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Selección 3 -----------------------------------
def screenSeleccion3():
    global opcion1SeleccionadaJugadoresBayern, opcion2SeleccionadaJugadoresBayern, opcion3SeleccionadaJugadoresBayern
    global opcion1SeleccionadaPorterosBayern, opcion2SeleccionadaPorterosBayern, opcion3SeleccionadaPorterosBayern
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
    imagenNeuer = pygame.image.load("Imagenes//ManuelNeuer.PNG") #Agregando imagen de Neuer
    imagenNeuer = pygame.transform.scale(imagenNeuer, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenNeuer, (100,432)) #Visualizar la imagen con su posición
    imagenSvenUlreich = pygame.image.load("Imagenes//SvenUlreich.PNG") #Agregando imagen de Ulreicj
    imagenSvenUlreich = pygame.transform.scale(imagenSvenUlreich, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenSvenUlreich, (360,432)) #Visualizar la imagen con su posición
    imagenPeretz = pygame.image.load("Imagenes//DanielPeretz.PNG") #Agregando imagen de Peretz
    imagenPeretz = pygame.transform.scale(imagenPeretz, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion3.blit(imagenPeretz, (615,432)) #Visualizar la imagen con su posición
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
    opcion1SeleccionadaJugadoresBayern = False
    opcion2SeleccionadaJugadoresBayern = False
    opcion3SeleccionadaJugadoresBayern = False
    opcion1SeleccionadaPorterosBayern = False
    opcion2SeleccionadaPorterosBayern = False
    opcion3SeleccionadaPorterosBayern = False
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
                        opcion1SeleccionadaJugadoresBayern = True #Encendido
                        opcion2SeleccionadaJugadoresBayern = False #Apagado
                        opcion3SeleccionadaJugadoresBayern = False #Apagado
                    elif (posicionOpcion2.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 2
                        opcion1SeleccionadaJugadoresBayern = False #Apagado
                        opcion2SeleccionadaJugadoresBayern = True #Encendido
                        opcion3SeleccionadaJugadoresBayern = False #Apagado
                    elif (posicionOpcion3.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaJugadoresBayern = False #Apagado
                        opcion2SeleccionadaJugadoresBayern = False #Apagado
                        opcion3SeleccionadaJugadoresBayern = True #Encendido
                    elif (posicionOpcion1Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorterosBayern = True #Encendido
                        opcion2SeleccionadaPorterosBayern = False #Apagado
                        opcion3SeleccionadaPorterosBayern = False #Apagado
                    elif (posicionOpcion2Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorterosBayern = False #Apagado
                        opcion2SeleccionadaPorterosBayern = True #Encendido
                        opcion3SeleccionadaPorterosBayern = False #Apagado
                    elif (posicionOpcion3Por.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1SeleccionadaPorterosBayern = False #Apagado
                        opcion2SeleccionadaPorterosBayern = False #Apagado
                        opcion3SeleccionadaPorterosBayern = True #Encendido
            # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadoresBayern else imagenNoSeleccionadaOpcion1, posicionOpcion1)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadoresBayern else imagenNoSeleccionadaOpcion2, posicionOpcion2)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadoresBayern else imagenNoSeleccionadaOpcion3, posicionOpcion3)
            # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorterosBayern else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorterosBayern else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
            ventanaSeleccion3.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorterosBayern else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
        pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Selección 3 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Juego -----------------------------------
def equiposelec():
    global resultado_moneda
    resultado_moneda = random.choice(["Local", "Visitante"])
    if resultado_moneda == "Local":
        print("El equipo es local")
    else:
        print("El equipo es visitante")
    return resultado_moneda

def screenJuego():
    # Creando la ventana
    ventanaJuego = pygame.display.set_mode(sizeScreen)
    pygame.mixer.music.set_volume(volumenGlobal)  # Manteniendo el volumen
    fondoVentanaJuego = pygame.image.load("Imagenes//fondojuego.png")
    ventanaJuego.blit(fondoVentanaJuego, (0,0))

    # Cargar imagen de la moneda
    imagen_moneda = pygame.image.load("Imagenes//Moneda.png")
    imagen_moneda = pygame.transform.scale(imagen_moneda, (320, 320))

    # Imágenes de Botón de Parar (Seleccionar)
    imagenParar = pygame.image.load("Imagenes//botonparar.png")
    imagenParar = pygame.transform.scale(imagenParar, (200, 200))
    botonParar = ventanaJuego.blit(imagenParar, (390,500))
    
    # Botón de Regreso
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png")
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45))
    ventanaJuego.blit(botonRegreso, (10,10))
    
    # Definir la clase Moneda
    class Moneda(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = imagen_moneda
            self.rect = self.image.get_rect(center=(450, 360))
            self.velocidad_rotacion = random.randint(3, 3)
            self.angulo = 0
            self.lanzada = False
            self.resultado = None

        def update(self):
            if self.lanzada:
                if self.angulo % 360 < 90 or self.angulo % 360 > 270:
                    self.resultado = "Local"
                else:
                    self.resultado = "Visitante"
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
    resultado_moneda = None

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: # Clic izquierdo
                    if botonParar.collidepoint(evento.pos):
                        moneda.lanzar()
                        resultado_moneda = equiposelec()
                        screenResultados()
                    elif 15 < evento.pos[0] < 65 and 15 < evento.pos[1] < 65:
                        screenPrincipal(volumenGlobal) # Botón de Regreso

        # Actualizar la animación de la moneda
        todos_los_sprites.update()

        # Dibujando rectángulo
        pygame.draw.rect(ventanaJuego, pygame.Color("#FFFFFF"), (160, 180, 600, 450), 0)

        # Mostrar resultado opuesto debajo del equipo contrario
        todos_los_sprites.draw(ventanaJuego)
        ventanaJuego.blit(imagenParar, botonParar)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
# ----------------------------------- Finalizando la Ventana de Juego ---------------------------------

# ----------------------------------- Iniciando la Ventana de Resultados -----------------------------------
def screenResultados():
    global equipoSeleccionado, equipo_contrario, equipo
    equipo = None
    equipo_contrario = None
    ventanaResultados = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaResultados = pygame.image.load("Imagenes//Fondo Resultados.png") #Agregando fondo de pantalla de Configuración
    ventanaResultados.blit(fondoVentanaResultados, (0,0)) #Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
    ventanaResultados.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
    # ---- Botón de JUGAR ----
    botonPlay = pygame.image.load("Imagenes//BotonPLAY.png") #Agregando Imagen representativa de botón de regreso
    botonPlay = pygame.transform.scale(botonPlay, (100, 100)) #Ajustando el tamaño
    ventanaResultados.blit(botonPlay, (425,535)) #Visualizar la imagen con su posición
    # ---- Imágen Árbitro ----
    imagenArbitro = pygame.image.load("Imagenes//arbitro.png") #Agregando Imagen representativa de botón de regreso
    imagenArbitro = pygame.transform.scale(imagenArbitro, (200, 270)) #Ajustando el tamaño
    ventanaResultados.blit(imagenArbitro, (373,240)) #Visualizar la imagen con su posición
    # ---- Imágen de los Equipos ----
    imagenArgentina = pygame.image.load("Imagenes//Argentina.png") #Agregando imagen Argentina
    imagenArgentina = pygame.transform.scale(imagenArgentina, (150, 150)) #Ajustando el tamaño
    imagenBarcelona = pygame.image.load("Imagenes//Barcelona.png") #Agregando imagen Barcelona
    imagenBarcelona = pygame.transform.scale(imagenBarcelona, (150, 150)) #Ajustando el tamaño
    imagenBayern = pygame.image.load("Imagenes//Bayern.png") #Agregando imagen Bayern
    imagenBayern = pygame.transform.scale(imagenBayern, (150, 150)) #Ajustando el tamaño
    # ---- Imágen de los jugadores Argentina ----
    imagenDiMaria = pygame.image.load("Imagenes//Di María.png") #Agregando imagen de Di María
    imagenDiMaria = pygame.transform.scale(imagenDiMaria, (180, 110)) #Ajustando el tamaño
    imagenMessi = pygame.image.load("Imagenes//messi.png") #Agregando imagen de Messi
    imagenMessi = pygame.transform.scale(imagenMessi, (180, 110)) #Ajustando el tamaño
    imagenDybala = pygame.image.load("Imagenes//dybala.png") #Agregando imagen de Dybala
    imagenDybala = pygame.transform.scale(imagenDybala, (180, 110)) #Ajustando el tamaño
    # ---- Imágen de los porteros Argentina----
    imagenMartinez = pygame.image.load("Imagenes//Emiliano Martínez.png") #Agregando imagen de Martínez
    imagenMartinez = pygame.transform.scale(imagenMartinez, (180, 110)) #Ajustando el tamaño
    imagenRulli = pygame.image.load("Imagenes//Gerónimo Rulli.png") #Agregando imagen de Rulli
    imagenRulli = pygame.transform.scale(imagenRulli, (180, 110)) #Ajustando el tamaño
    imagenArmani = pygame.image.load("Imagenes//Franco Armani.png") #Agregando imagen de Armani
    imagenArmani = pygame.transform.scale(imagenArmani, (180, 110)) #Ajustando el tamaño
    # ---- Imágen de los jugadores Barcelona----
    imagenRaphinha = pygame.image.load("Imagenes//Raphinha.png")  # Agregando imagen de Raphinha
    imagenRaphinha = pygame.transform.scale(imagenRaphinha, (180, 110))  # Ajustando el tamaño
    imagenRobertLewandowski = pygame.image.load("Imagenes//RobertLewandowski.png")  # Agregando imagen de Lewandowski
    imagenRobertLewandowski = pygame.transform.scale(imagenRobertLewandowski, (180, 110))  # Ajustando el tamaño
    imagenFerranTorres = pygame.image.load("Imagenes//FerranTorres.png")  # Agregando imagen de Torres
    imagenFerranTorres = pygame.transform.scale(imagenFerranTorres, (180, 110))  # Ajustando el tamaño
    # ---- Imágen de los porteros Barcelona----
    imagenBravo = pygame.image.load("Imagenes//Claudio Bravo.png")  # Agregando imagen de Bravo
    imagenBravo = pygame.transform.scale(imagenBravo, (180, 110))  # Ajustando el tamaño
    imagenPeña = pygame.image.load("Imagenes//IñakiPeña.png")  # Agregando imagen de Peña
    imagenPeña = pygame.transform.scale(imagenPeña, (180, 110))  # Ajustando el tamaño
    imagenStegen = pygame.image.load("Imagenes//Stegen.png")  # Agregando imagen de Stegen
    imagenStegen = pygame.transform.scale(imagenStegen, (180, 110))  # Ajustando el tamaño
    # ---- Imágen de los jugadores Bayern ----
    imagenKane = pygame.image.load("Imagenes//HarryKane.png") #Agregando imagen de Kane
    imagenKane = pygame.transform.scale(imagenKane, (180, 110)) #Ajustando el tamaño
    imagenMuller = pygame.image.load("Imagenes//ThomasMuller.PNG") #Agregando imagen de Muller
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 110)) #Ajustando el tamaño
    imagenMusiala = pygame.image.load("Imagenes//JamalMusiala.PNG") #Agregando imagen de Musiala
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 110)) #Ajustando el tamaño
    # ---- Imágen de los porteros Bayern----
    imagenNeuer = pygame.image.load("Imagenes//ManuelNeuer.PNG") #Agregando imagen de Neuer
    imagenNeuer = pygame.transform.scale(imagenNeuer, (180, 110)) #Ajustando el tamaño
    imagenSvenUlreich = pygame.image.load("Imagenes//SvenUlreich.PNG") #Agregando imagen de Ulreicj
    imagenSvenUlreich = pygame.transform.scale(imagenSvenUlreich, (180, 110)) #Ajustando el tamaño
    imagenPeretz = pygame.image.load("Imagenes//DanielPeretz.PNG") #Agregando imagen de Peretz
    imagenPeretz = pygame.transform.scale(imagenPeretz, (180, 110)) #Ajustando el tamaño
    # ---- Bucle Principal de resultados ----
    while True: #Bucle para ventana principal
        for event in pygame.event.get(): # Iterando sobre eventos
            if event.type == pygame.QUIT: # Si el usuario intenta cerrar ventana
                pygame.quit() # Saliendo del juego
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # Detectar clic del mouse
                if event.button == 1: # Verificar si fue clic izquierdo
                    x, y = event.pos # Guardando en variables donde se hizo clic
                    # Verificar si el clic fue dentro de alguno de los botones de la Ventana Principal
                    if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                        screenJuego() #Ir a ventana principal
                    if (425 < x < 525 and 535 < y < 635): #Botón de Regreso
                        screenEstadisticas() #Ir a ventana de Estadisticas
                    # ---- Encontrando equipo contrario ----
                    equipos_disponibles = ["Argentina", "Barcelona", "Bayern"]
                    if equipoSeleccionado in equipos_disponibles:
                        equipos_disponibles.remove(equipoSeleccionado)  # Eliminar el equipo seleccionado de la lista
                    else:
                        equipo_contrario = random.choice(equipos_disponibles)
                    print("Equipo contrario:", equipo_contrario)
                    if (resultado_moneda == "Local"):
                        if (equipoSeleccionado == 1):  #Argentina
                            equipos_disponibles = ["Barcelona", "Bayern"]
                            equipo_contrario = random.choice(equipos_disponibles)
                            print("Equipo contrario:", equipo_contrario)
                            # ---- Encontrando equipo contrario ----
                            if equipo_contrario == "Barcelona":
                                jugadores_equipo_contrario = [imagenRaphinha, imagenRobertLewandowski, imagenFerranTorres]
                                porteros_equipo_contrario = [imagenBravo, imagenPeña, imagenStegen]
                                img_equipo_contrario = imagenBarcelona
                            elif equipo_contrario == "Bayern":
                                jugadores_equipo_contrario = [imagenKane, imagenMuller, imagenMusiala]
                                porteros_equipo_contrario = [imagenNeuer, imagenSvenUlreich, imagenPeretz]
                                img_equipo_contrario = imagenBayern
                            elif equipo_contrario == "Argentina":
                                jugadores_equipo_contrario = [imagenDiMaria, imagenMessi, imagenDybala]
                                porteros_equipo_contrario = [imagenMartinez, imagenRulli, imagenArmani]
                                img_equipo_contrario = imagenArgentina
                            jugador_contrario = random.choice(jugadores_equipo_contrario)
                            portero_contrario = random.choice(porteros_equipo_contrario)
                            # ---- COMIENZO ----
                            ventanaResultados.blit(imagenArgentina, (115, 165))
                            equipo == "Local" #Definiendo si es local o visitante
                            if (opcion1SeleccionadaJugadoresArgentina):
                                ventanaResultados.blit(imagenDiMaria, (105, 360))
                            elif (opcion2SeleccionadaJugadoresArgentina):
                                ventanaResultados.blit(imagenMessi, (105, 360))
                            elif (opcion3SeleccionadaJugadoresArgentina):
                                ventanaResultados.blit(imagenDybala, (105, 360))
                            if (opcion1SeleccionadaPorterosArgentina):
                                ventanaResultados.blit(imagenMartinez, (105, 480))
                            elif (opcion2SeleccionadaPorterosArgentina):
                                ventanaResultados.blit(imagenRulli, (105, 480))
                            elif (opcion3SeleccionadaPorterosArgentina):
                                ventanaResultados.blit(imagenArmani, (105, 480))
                            ventanaResultados.blit(jugador_contrario, (660, 360))
                            ventanaResultados.blit(portero_contrario, (660, 480))
                            ventanaResultados.blit(img_equipo_contrario, (676,165))
                        elif (equipoSeleccionado == 2): #Barcelona
                            equipos_disponibles = ["Argentina", "Bayern"]
                            equipo_contrario = random.choice(equipos_disponibles)
                            print("Equipo contrario:", equipo_contrario)
                            # ---- Encontrando equipo contrario ----
                            if equipo_contrario == "Barcelona":
                                jugadores_equipo_contrario = [imagenRaphinha, imagenRobertLewandowski, imagenFerranTorres]
                                porteros_equipo_contrario = [imagenBravo, imagenPeña, imagenStegen]
                                img_equipo_contrario = imagenBarcelona
                            elif equipo_contrario == "Bayern":
                                jugadores_equipo_contrario = [imagenKane, imagenMuller, imagenMusiala]
                                porteros_equipo_contrario = [imagenNeuer, imagenSvenUlreich, imagenPeretz]
                                img_equipo_contrario = imagenBayern
                            elif equipo_contrario == "Argentina":
                                jugadores_equipo_contrario = [imagenDiMaria, imagenMessi, imagenDybala]
                                porteros_equipo_contrario = [imagenMartinez, imagenRulli, imagenArmani]
                                img_equipo_contrario = imagenArgentina
                            jugador_contrario = random.choice(jugadores_equipo_contrario)
                            portero_contrario = random.choice(porteros_equipo_contrario)
                            # ---- COMIENZO ----
                            ventanaResultados.blit(imagenBarcelona, (113,170))
                            equipo == "Local" #Definiendo si es local o visitante
                            if (opcion1SeleccionadaJugadoresBarcelona):
                                ventanaResultados.blit(imagenRaphinha, (105, 360))
                            elif (opcion2SeleccionadaJugadoresBarcelona):
                                ventanaResultados.blit(imagenRobertLewandowski, (105, 360))
                            elif(opcion3SeleccionadaJugadoresBarcelona):
                                ventanaResultados.blit(imagenFerranTorres, (105, 360))
                            if (opcion1SeleccionadaPorterosBarcelona):
                                ventanaResultados.blit(imagenBravo, (105, 480))
                            elif (opcion2SeleccionadaPorterosBarcelona):
                                ventanaResultados.blit(imagenPeña, (105, 480))
                            elif(opcion3SeleccionadaPorterosBarcelona):
                                ventanaResultados.blit(imagenStegen, (105, 480))
                            ventanaResultados.blit(jugador_contrario, (660, 360))
                            ventanaResultados.blit(portero_contrario, (660, 480))
                            ventanaResultados.blit(img_equipo_contrario, (676,165))
                        elif (equipoSeleccionado == 3): #Bayern
                            equipos_disponibles = ["Barcelona", "Argentina"]
                            equipo_contrario = random.choice(equipos_disponibles)
                            print("Equipo contrario:", equipo_contrario)
                            # ---- Encontrando equipo contrario ----
                            if equipo_contrario == "Barcelona":
                                jugadores_equipo_contrario = [imagenRaphinha, imagenRobertLewandowski, imagenFerranTorres]
                                porteros_equipo_contrario = [imagenBravo, imagenPeña, imagenStegen]
                                img_equipo_contrario = imagenBarcelona
                            elif equipo_contrario == "Bayern":
                                jugadores_equipo_contrario = [imagenKane, imagenMuller, imagenMusiala]
                                porteros_equipo_contrario = [imagenNeuer, imagenSvenUlreich, imagenPeretz]
                                img_equipo_contrario = imagenBayern
                            elif equipo_contrario == "Argentina":
                                jugadores_equipo_contrario = [imagenDiMaria, imagenMessi, imagenDybala]
                                porteros_equipo_contrario = [imagenMartinez, imagenRulli, imagenArmani]
                                img_equipo_contrario = imagenArgentina
                            jugador_contrario = random.choice(jugadores_equipo_contrario)
                            portero_contrario = random.choice(porteros_equipo_contrario)
                            # ---- COMIENZO ----
                            ventanaResultados.blit(imagenBayern, (115,160))
                            equipo == "Local" #Definiendo si es local o visitante
                            if (opcion1SeleccionadaJugadoresBayern):
                                ventanaResultados.blit(imagenKane, (105, 360))
                            elif (opcion2SeleccionadaJugadoresBayern):
                                ventanaResultados.blit(imagenMuller, (105, 360))
                            elif(opcion3SeleccionadaJugadoresBayern):
                                ventanaResultados.blit(imagenMusiala, (105, 360))
                            if (opcion1SeleccionadaPorterosBayern):
                                ventanaResultados.blit(imagenNeuer, (105, 480))
                            elif (opcion2SeleccionadaPorterosBayern):
                                ventanaResultados.blit(imagenSvenUlreich, (105, 480))
                            elif(opcion3SeleccionadaPorterosBayern):
                                ventanaResultados.blit(imagenPeretz, (105, 480))
                            ventanaResultados.blit(jugador_contrario, (660, 360))
                            ventanaResultados.blit(portero_contrario, (660, 480))
                            ventanaResultados.blit(img_equipo_contrario, (676,165))
                            
                    if (resultado_moneda == "Visitante"):
                        if (equipoSeleccionado == 1):  # Argentina
                            equipos_disponibles = ["Barcelona", "Bayern"]
                            equipo_contrario = random.choice(equipos_disponibles)
                            print("Equipo contrario:", equipo_contrario)
                            # ---- Encontrando equipo contrario ----
                            if equipo_contrario == "Barcelona":
                                jugadores_equipo_contrario = [imagenRaphinha, imagenRobertLewandowski, imagenFerranTorres]
                                porteros_equipo_contrario = [imagenBravo, imagenPeña, imagenStegen]
                                img_equipo_contrario = imagenBarcelona
                            elif equipo_contrario == "Bayern":
                                jugadores_equipo_contrario = [imagenKane, imagenMuller, imagenMusiala]
                                porteros_equipo_contrario = [imagenNeuer, imagenSvenUlreich, imagenPeretz]
                                img_equipo_contrario = imagenBayern
                            elif equipo_contrario == "Argentina":
                                jugadores_equipo_contrario = [imagenDiMaria, imagenMessi, imagenDybala]
                                porteros_equipo_contrario = [imagenMartinez, imagenRulli, imagenArmani]
                                img_equipo_contrario = imagenArgentina
                            jugador_contrario = random.choice(jugadores_equipo_contrario)
                            portero_contrario = random.choice(porteros_equipo_contrario)
                            # ---- COMIENZO ----
                            ventanaResultados.blit(imagenArgentina, (676, 165))
                            equipo == "Visitante" #Definiendo si es local o visitante
                            if (opcion1SeleccionadaJugadoresArgentina):
                                ventanaResultados.blit(imagenDiMaria, (660, 360))
                            elif (opcion2SeleccionadaJugadoresArgentina):
                                ventanaResultados.blit(imagenMessi, (660, 360))
                            elif (opcion3SeleccionadaJugadoresArgentina):
                                ventanaResultados.blit(imagenDybala, (660, 360))
                            if (opcion1SeleccionadaPorterosArgentina):
                                ventanaResultados.blit(imagenMartinez, (660, 480))
                            elif (opcion2SeleccionadaPorterosArgentina):
                                ventanaResultados.blit(imagenRulli, (660, 480))
                            elif (opcion3SeleccionadaPorterosArgentina):
                                ventanaResultados.blit(imagenArmani, (660, 480))
                            ventanaResultados.blit(jugador_contrario, (105, 360))
                            ventanaResultados.blit(portero_contrario, (105, 480))
                            ventanaResultados.blit(img_equipo_contrario, (115,165))
                        elif (equipoSeleccionado == 2): #Barcelona
                            equipos_disponibles = ["Bayern", "Argentina"]
                            equipo_contrario = random.choice(equipos_disponibles)
                            print("Equipo contrario:", equipo_contrario)
                            # ---- Encontrando equipo contrario ----
                            if equipo_contrario == "Barcelona":
                                jugadores_equipo_contrario = [imagenRaphinha, imagenRobertLewandowski, imagenFerranTorres]
                                porteros_equipo_contrario = [imagenBravo, imagenPeña, imagenStegen]
                                img_equipo_contrario = imagenBarcelona
                            elif equipo_contrario == "Bayern":
                                jugadores_equipo_contrario = [imagenKane, imagenMuller, imagenMusiala]
                                porteros_equipo_contrario = [imagenNeuer, imagenSvenUlreich, imagenPeretz]
                                img_equipo_contrario = imagenBayern
                            elif equipo_contrario == "Argentina":
                                jugadores_equipo_contrario = [imagenDiMaria, imagenMessi, imagenDybala]
                                porteros_equipo_contrario = [imagenMartinez, imagenRulli, imagenArmani]
                                img_equipo_contrario = imagenArgentina
                            jugador_contrario = random.choice(jugadores_equipo_contrario)
                            portero_contrario = random.choice(porteros_equipo_contrario)
                            # ---- COMIENZO ----
                            ventanaResultados.blit(imagenBarcelona, (676,170))
                            equipo == "Visitante" #Definiendo si es local o visitante
                            if (opcion1SeleccionadaJugadoresBarcelona):
                                ventanaResultados.blit(imagenRaphinha, (660, 360))
                            elif (opcion2SeleccionadaJugadoresBarcelona):
                                ventanaResultados.blit(imagenRobertLewandowski, (660, 360))
                            elif(opcion3SeleccionadaJugadoresBarcelona):
                                ventanaResultados.blit(imagenFerranTorres, (660, 360))
                            if (opcion1SeleccionadaPorterosBarcelona):
                                ventanaResultados.blit(imagenBravo, (660, 480))
                            elif (opcion2SeleccionadaPorterosBarcelona):
                                ventanaResultados.blit(imagenPeña, (660, 480))
                            elif(opcion3SeleccionadaPorterosBarcelona):
                                ventanaResultados.blit(imagenStegen, (660, 480))
                            ventanaResultados.blit(jugador_contrario, (105, 360))
                            ventanaResultados.blit(portero_contrario, (105, 480))
                            ventanaResultados.blit(img_equipo_contrario, (115,165))
                        elif (equipoSeleccionado == 3): #Bayern
                            equipos_disponibles = ["Barcelona", "Argentina"]
                            equipo_contrario = random.choice(equipos_disponibles)
                            print("Equipo contrario:", equipo_contrario)
                            # ---- Encontrando equipo contrario ----
                            if equipo_contrario == "Barcelona":
                                jugadores_equipo_contrario = [imagenRaphinha, imagenRobertLewandowski, imagenFerranTorres]
                                porteros_equipo_contrario = [imagenBravo, imagenPeña, imagenStegen]
                                img_equipo_contrario = imagenBarcelona
                            elif equipo_contrario == "Bayern":
                                jugadores_equipo_contrario = [imagenKane, imagenMuller, imagenMusiala]
                                porteros_equipo_contrario = [imagenNeuer, imagenSvenUlreich, imagenPeretz]
                                img_equipo_contrario = imagenBayern
                            elif equipo_contrario == "Argentina":
                                jugadores_equipo_contrario = [imagenDiMaria, imagenMessi, imagenDybala]
                                porteros_equipo_contrario = [imagenMartinez, imagenRulli, imagenArmani]
                                img_equipo_contrario = imagenArgentina
                            jugador_contrario = random.choice(jugadores_equipo_contrario)
                            portero_contrario = random.choice(porteros_equipo_contrario)
                            # ---- COMIENZO ----
                            ventanaResultados.blit(imagenBayern, (676,160))
                            equipo == "Visitante" #Definiendo si es local o visitante
                            if (opcion1SeleccionadaJugadoresBayern):
                                ventanaResultados.blit(imagenKane, (660, 360))
                            elif (opcion2SeleccionadaJugadoresBayern):
                                ventanaResultados.blit(imagenMuller, (660, 360))
                            elif(opcion3SeleccionadaJugadoresBayern):
                                ventanaResultados.blit(imagenMusiala, (660, 360))
                            if (opcion1SeleccionadaPorterosBayern):
                                ventanaResultados.blit(imagenNeuer, (660, 480))
                            elif (opcion2SeleccionadaPorterosBayern):
                                ventanaResultados.blit(imagenSvenUlreich, (660, 480))
                            elif(opcion3SeleccionadaPorterosBayern):
                                ventanaResultados.blit(imagenPeretz, (660, 480))
                            ventanaResultados.blit(jugador_contrario, (105, 360))
                            ventanaResultados.blit(portero_contrario, (105, 480))
                            ventanaResultados.blit(img_equipo_contrario, (115,165))
        pygame.display.flip() #Actualizando Pantalla

# ----------------------------------- Finalizando la Ventana de Resultados ---------------------------------

# ----------------------------------- Iniciando la Ventana de Estadisticas -----------------------------------
def screenEstadisticas():
    global equipo_contrario, estado_gol
    global equipo1_goles, equipo2_goles  # Contadores de goles
    equipo1_goles = 0
    equipo2_goles = 0
    estado_gol = None
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaEstadisticas = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaEstadisticas = pygame.image.load("Imagenes//Estadisticas.png") #Agregando fondo de pantalla de Información
    ventanaEstadisticas.blit(fondoVentanaEstadisticas, (0,0)) #Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
    ventanaEstadisticas.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
    # ---- Imágenes de estado de gol ----
    esperandoGol = pygame.image.load("Imagenes//esperandogol.png") #Agregando Imagen representativa de botón de regreso
    esperandoGol = pygame.transform.scale(esperandoGol, (70, 70)) #Ajustando el tamaño
    siGol = pygame.image.load("Imagenes//SIgol.png") #Agregando Imagen representativa de botón de regreso
    siGol = pygame.transform.scale(siGol, (70, 70)) #Ajustando el tamaño
    noGol = pygame.image.load("Imagenes//NOgol.png") #Agregando Imagen representativa de botón de regreso
    noGol = pygame.transform.scale(noGol, (70, 70)) #Ajustando el tamaño
    
    # Cargar el archivo de sonido
    sonido_festejo = pygame.mixer.Sound("Musica//APLAUSOS.mpeg")
    sonido_tristeza = pygame.mixer.Sound("Musica//ABUCHEO.mp3")
    sonido_silbato = pygame.mixer.Sound("Musica//SILBATO.mp3")
    sonido_comienzo = pygame.mixer.Sound("Musica//CONTADOR.mp3")
    
    # ---- Orden Sonidos ----
    canal_silbato = pygame.mixer.Channel(0)  # Crear un nuevo canal para el silbato
    canal_comienzo = pygame.mixer.Channel(1)  # Crear un nuevo canal para el comienzo
    
    sonido_silbato.play() # Sonando apenas se abre la ventana
    canal_comienzo.play(sonido_comienzo) # Sonando de comienzo
    pygame.time.wait(int(sonido_comienzo.get_length() * 1000))  # Esperar la duración del sonido de comienzo
    canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles
    
    # Generar posición aleatoria para el portero
    portero_posicion = random.randint(1, 6)
    pos_x_portero = 115 + ((portero_posicion - 1) * 110)  # Calcular la posición x de la paleta seleccionada
    # Dibujar el portero invisible
    portero_invisible = pygame.image.load("Imagenes//paleta.png")
    portero_invisible = pygame.transform.scale(portero_invisible, (183, 300))
    ventanaEstadisticas.blit(portero_invisible, (pos_x_portero, 350))  # La posición y puede ajustarse según sea necesario
    
    # ---- Imágenes de paletas ----
    paleta1 = pygame.image.load("Imagenes//paleta.png") #Agregando Imagen representativa de botón de regreso
    paleta1 = pygame.transform.scale(paleta1, (183, 300)) #Ajustando el tamaño
    posicionPaleta1 = ventanaEstadisticas.blit(paleta1, (115,350)) #Visualizar la imagen con su posición
    paleta2 = pygame.image.load("Imagenes//paleta.png") #Agregando Imagen representativa de botón de regreso
    paleta2 = pygame.transform.scale(paleta2, (183, 300)) #Ajustando el tamaño
    posicionPaleta2 = ventanaEstadisticas.blit(paleta2, (225,350)) #Visualizar la imagen con su posición
    paleta3 = pygame.image.load("Imagenes//paleta.png") #Agregando Imagen representativa de botón de regreso
    paleta3 = pygame.transform.scale(paleta3, (183, 300)) #Ajustando el tamaño
    posicionPaleta3 = ventanaEstadisticas.blit(paleta3, (335,350)) #Visualizar la imagen con su posición
    paleta4 = pygame.image.load("Imagenes//paleta.png") #Agregando Imagen representativa de botón de regreso
    paleta4 = pygame.transform.scale(paleta4, (183, 300)) #Ajustando el tamaño
    posicionPaleta4 = ventanaEstadisticas.blit(paleta4, (445,350)) #Visualizar la imagen con su posición
    paleta5 = pygame.image.load("Imagenes//paleta.png") #Agregando Imagen representativa de botón de regreso
    paleta5 = pygame.transform.scale(paleta5, (183, 300)) #Ajustando el tamaño
    posicionPaleta5 = ventanaEstadisticas.blit(paleta5, (555,350)) #Visualizar la imagen con su posición
    paleta6 = pygame.image.load("Imagenes//paleta.png") #Agregando Imagen representativa de botón de regreso
    paleta6 = pygame.transform.scale(paleta6, (183, 300)) #Ajustando el tamaño
    posicionPaleta6 = ventanaEstadisticas.blit(paleta6, (665,350)) #Visualizar la imagen con su posición
    
    # Coordenadas para los círculos de "esperando gol" ELEGIDO POR USUARIO
    coordenadas_esperando_gol_elegido = [(50, 185), (130, 185), (210, 185), (290, 185), (370, 185)]
    # Coordenadas para los círculos de "esperando gol" EQUIPO CONTRARIO
    coordenadas_esperando_gol_contrario = [(510, 185), (590, 185), (670, 185), (750, 185), (830, 185)]
    
    # ---- Variables de temporización ----
    tiempo_entre_turnos = 3000  # 3 segundos en milisegundos
    tiempo_ultimo_clic = pygame.time.get_ticks()  # Variable para almacenar el tiempo del último clic
    
    # Definir la función para determinar el equipo que tiene el turno
    def determinarTurno(clics_totales):
        # Si el recuento total de clics es par, es el turno del segundo equipo
        if clics_totales % 2 == 0:
            return 2
        else:
            return 1

    # Dibujar los primeros 5 círculos negros de "esperando gol" ELEGIDO POR USUARIO
    for coordenada in coordenadas_esperando_gol_elegido:
        ventanaEstadisticas.blit(esperandoGol, coordenada)
    # Dibujar los primeros 5 círculos negros de "esperando gol" EQUIPO CONTRARIO
    for coordenada in coordenadas_esperando_gol_contrario:
        ventanaEstadisticas.blit(esperandoGol, coordenada)
    
    # Definir la función para actualizar la apariencia de los círculos de gol
    def aparienciaGol(gol, turno_equipo):
        if gol:  # Si hubo gol
            if turno_equipo == 1:  # Si es el turno del primer equipo (local)
                if coordenadas_esperando_gol_elegido:  # Verificar si hay elementos en la lista
                    coordenada = coordenadas_esperando_gol_elegido.pop(0)  # Tomar la primera coordenada del equipo local
                    ventanaEstadisticas.blit(siGol, coordenada)  # Dibujar círculo de gol para el equipo local
            else:  # Si es el turno del segundo equipo (visitante)
                if coordenadas_esperando_gol_contrario:  # Verificar si hay elementos en la lista
                    coordenada = coordenadas_esperando_gol_contrario.pop(0)  # Tomar la primera coordenada del equipo contrario
                    ventanaEstadisticas.blit(siGol, coordenada)  # Dibujar círculo de gol para el equipo contrario
        else:  # Si no hubo gol
            if turno_equipo == 1:  # Si es el turno del primer equipo (local)
                if coordenadas_esperando_gol_elegido:  # Verificar si hay elementos en la lista
                    coordenada = coordenadas_esperando_gol_elegido.pop(0)  # Tomar la primera coordenada del equipo local
                    ventanaEstadisticas.blit(noGol, coordenada)  # Dibujar círculo de no gol para el equipo local
            else:  # Si es el turno del segundo equipo (visitante)
                if coordenadas_esperando_gol_contrario:  # Verificar si hay elementos en la lista
                    coordenada = coordenadas_esperando_gol_contrario.pop(0)  # Tomar la primera coordenada del equipo contrario
                    ventanaEstadisticas.blit(noGol, coordenada)  # Dibujar círculo de no gol para el equipo contrario

    #---- Comienzo de Equipo ----
    turno_equipo = 1  # Empezamos con el equipo local
    clics_totales = 0  # Inicializamos el contador de clics totales
    
    #----Variables de tiempo paletas----
    tiempoPrimerPaleta = 0
    tiempoSegundaPaleta = 0
    tiempoTercerPaleta = 0
    tiempoCuartaPaleta = 0
    tiempoQuintaPaleta = 0
    tiempoSextaPaleta = 0

    # ---- Bucle de la ventana de Estadisticas ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                pygame.quit() #Cerrando ventana
                sys.exit() #Saliendo del script Python por completo para detener el programa en su totalidad
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                    if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                        screenPrincipal(volumenGlobal) #Ir a ventana principal
                    if turno_equipo == 1: # Si es el turno del equipo local
                        
                        if (posicionPaleta1.collidepoint(event.pos)):
                            # Verificar si ha pasado el tiempo adecuado entre clics
                            if tiempoPrimerPaleta + tiempo_entre_turnos < pygame.time.get_ticks():
                                # Actualizar el tiempo del último clic
                                tiempoPrimerPaleta = pygame.time.get_ticks()
                                pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                                if (portero_posicion == 1):
                                    sonido_tristeza.play()
                                    print("No fue gol")
                                    gol = False
                                else:
                                    sonido_festejo.play()
                                    print("GOL")
                                    gol = True
                                if tiempoTercerPaleta > tiempo_entre_turnos:
                                    sonido_tristeza.play()
                                    print("No fue gol")
                                    gol = False
                                clics_totales += 1  # Incrementar el contador de clics totales
                                turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                                aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                                canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles

                            
                        if (posicionPaleta2.collidepoint(event.pos)):
                            # Verificar si ha pasado el tiempo adecuado entre clics
                            if tiempoSegundaPaleta + tiempo_entre_turnos < pygame.time.get_ticks():
                                # Actualizar el tiempo del último clic
                                tiempoSegundaPaleta = pygame.time.get_ticks()
                                pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                                tiempoSegundaPaleta = pygame.time.get_ticks() #Obteniendo el tiempo inicial de la segunda paleta
                                if (portero_posicion == 2):
                                    sonido_tristeza.play()
                                    print("No fue gol")
                                    gol = False
                                else:
                                    sonido_festejo.play()
                                    print("GOL")
                                    gol = True
                                if tiempoSegundaPaleta > tiempo_entre_turnos:
                                    sonido_tristeza.play()
                                    print("No fue gol")
                                    gol = False
                                clics_totales += 1  # Incrementar el contador de clics totales
                                turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                                aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                                canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles
                            
                        if (posicionPaleta3.collidepoint(event.pos)):
                            # Verificar si ha pasado el tiempo adecuado entre clics
                            if tiempoTercerPaleta + tiempo_entre_turnos < pygame.time.get_ticks():
                                # Actualizar el tiempo del último clic
                                tiempoTercerPaleta = pygame.time.get_ticks()
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            tiempoTercerPaleta = pygame.time.get_ticks() #Obteniendo el tiempo inicial de la tercer paleta
                            if (portero_posicion == 3):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            if tiempoTercerPaleta > tiempo_entre_turnos:
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                            canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles
                            
                        if (posicionPaleta4.collidepoint(event.pos)):
                            # Verificar si ha pasado el tiempo adecuado entre clics
                            if tiempoCuartaPaleta + tiempo_entre_turnos < pygame.time.get_ticks():
                                # Actualizar el tiempo del último clic
                                tiempoCuartaPaleta = pygame.time.get_ticks()
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            tiempoCuartaPaleta = pygame.time.get_ticks() #Obteniendo el tiempo inicial de la cuarta paleta
                            if (portero_posicion == 4):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            if tiempoCuartaPaleta > tiempo_entre_turnos:
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                            canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles
                            
                        if (posicionPaleta5.collidepoint(event.pos)):
                            # Verificar si ha pasado el tiempo adecuado entre clics
                            if tiempoQuintaPaleta + tiempo_entre_turnos < pygame.time.get_ticks():
                                # Actualizar el tiempo del último clic
                                tiempoQuintaPaleta = pygame.time.get_ticks()
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            tiempoQuintaPaleta = pygame.time.get_ticks() #Obteniendo el tiempo inicial de la quinta paleta
                            if (portero_posicion == 5):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            if tiempoQuintaPaleta > tiempo_entre_turnos:
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                            canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles
                            
                        if (posicionPaleta6.collidepoint(event.pos)):
                            # Verificar si ha pasado el tiempo adecuado entre clics
                            if tiempoSextaPaleta + tiempo_entre_turnos < pygame.time.get_ticks():
                                # Actualizar el tiempo del último clic
                                tiempoSextaPaleta = pygame.time.get_ticks()
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            tiempoSextaPaleta = pygame.time.get_ticks() #Obteniendo el tiempo inicial de la sexta paleta
                            if (portero_posicion == 6):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            if tiempoSextaPaleta > tiempo_entre_turnos:
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                            canal_silbato.play(sonido_silbato) # Sonando para comenzar a tirar goles
                    else:
                        if (posicionPaleta1.collidepoint(event.pos)):
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            if (portero_posicion == 1):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                        if (posicionPaleta2.collidepoint(event.pos)):
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            if (portero_posicion == 2):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                        if (posicionPaleta3.collidepoint(event.pos)):
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            if (portero_posicion == 3):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                        if (posicionPaleta4.collidepoint(event.pos)):
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            if (portero_posicion == 4):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                        if (posicionPaleta5.collidepoint(event.pos)):
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            if (portero_posicion == 5):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                        if (posicionPaleta6.collidepoint(event.pos)):
                            pygame.mixer.music.set_volume(volumenGlobal * 0.005)  # Reducir el volumen de la música de fondo a la mitad
                            if (portero_posicion == 6):
                                sonido_tristeza.play()
                                print("No fue gol")
                                gol = False
                            else:
                                sonido_festejo.play()
                                print("GOL")
                                gol = True
                            clics_totales += 1  # Incrementar el contador de clics totales
                            turno_equipo = determinarTurno(clics_totales)  # Determinar el turno del equipo
                            aparienciaGol(gol, turno_equipo)  # Actualizar la apariencia de los círculos de gol
                        
                    if(equipoSeleccionado):
                        if (equipoSeleccionado==1):
                            equipo1 = tipografia.render("Argentina", True, ("#7ED957")) #Indicando el equipo
                            ventanaEstadisticas.blit(equipo1, (180, 120)) #Reflejando el texto
                        elif (equipoSeleccionado==2):
                            equipo2 = tipografia.render("Barcelona", True, ("#7ED957")) #Indicando el equipo
                            ventanaEstadisticas.blit(equipo2, (180, 120)) #Reflejando el texto
                        elif (equipoSeleccionado==3):
                            equipo3 = tipografia.render("Bayern", True, ("#7ED957")) #Indicando el equipo
                            ventanaEstadisticas.blit(equipo3, (180, 120)) #Reflejando el texto
                    if(equipo_contrario):
                        if (equipo_contrario=="Argentina"):
                            equipo4 = tipografia.render("Argentina", True, ("#5CE1E6")) #Indicando el equipo
                            ventanaEstadisticas.blit(equipo4, (670, 120)) #Reflejando el texto
                        elif (equipo_contrario=="Barcelona"):
                            equipo5 = tipografia.render("Barcelona", True, ("#5CE1E6")) #Indicando el equipo
                            ventanaEstadisticas.blit(equipo5, (670, 120)) #Reflejando el texto
                        elif (equipo_contrario=="Bayern"):
                            equipo6 = tipografia.render("Bayern", True, ("#5CE1E6")) #Indicando el equipo
                            ventanaEstadisticas.blit(equipo6, (670, 120)) #Reflejando el texto
                    tiempo_actual = pygame.time.get_ticks()
                    if (tiempo_actual - tiempo_ultimo_clic) > tiempo_entre_turnos:
                        # Realizar acciones del clic (reproducir sonido, verificar gol, etc.)
                        tiempo_ultimo_clic = tiempo_actual  # Actualizar el tiempo del último clic
        pygame.display.flip( )
# ----------------------------------- Finalizando la Ventana de Estadisticas ---------------------------------

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
                        screenJuego() #Ir a Ventana de Juego
        pygame.display.flip() #Actualizando Pantalla
# ----------------------------------- Finalizando la Ventana Principal -----------------------------------
screenPrincipal(volumenGlobal)
pygame.quit()
