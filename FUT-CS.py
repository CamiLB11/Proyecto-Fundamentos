import random
import sys
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
def screenConfiguracion():
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
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//Seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaConfiguracion.blit(imagenSeleccionadaOpcion1, (190,470)) #Visualizar la imagen con su posición
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//Seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaConfiguracion.blit(imagenSeleccionadaOpcion2, (440,470)) #Visualizar la imagen con su posición
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
def screenSeleccion1():
        global enSeleccionEquipo #Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
        pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
        ventanaSeleccion1 = pygame.display.set_mode(sizeScreen) #Creación de Ventana
        fondoVentanaSeleccion2 = pygame.image.load("Imagenes//fondoSeleccion.png") #Agregando fondo de pantalla de Selección 1
        ventanaSeleccion1.blit(fondoVentanaSeleccion2, (0,0)) #Visualizar el fondo
        # ---- Botón de Regreso ----
        botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
        botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
        ventanaSeleccion1.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
        # ---- Imágen de los jugadores ----
        imagenKane = pygame.image.load("Imagenes//Di María.png") #Agregando imagen de Di María
        imagenKane = pygame.transform.scale(imagenKane, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenKane, (100,130)) #Visualizar la imagen con su posición
        imagenMuller = pygame.image.load("Imagenes//messi.png") #Agregando imagen de Messi
        imagenMuller = pygame.transform.scale(imagenMuller, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMuller, (360,130)) #Visualizar la imagen con su posición
        imagenMusiala = pygame.image.load("Imagenes//dybala.png") #Agregando imagen de Dybala
        imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
        ventanaSeleccion1.blit(imagenMusiala, (615,130)) #Visualizar la imagen con su posición
        # ---- Imágen de los botones de selección jugadores----
        # ---- Imágenes Seleccionadas ----
        imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
        posicionOpcion1 = ventanaSeleccion1.blit(imagenSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
        imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
        posicionOpcion2 = ventanaSeleccion1.blit(imagenSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
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
        imagenSeleccionada1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
        posicionOpcion1Por = ventanaSeleccion1.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
        imagenSeleccionada2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
        imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
        posicionOpcion2Por = ventanaSeleccion1.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
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
    global enSeleccionEquipo #Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaSeleccion2 = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaSeleccion2 = pygame.image.load("Imagenes//fondoSeleccion.png") #Agregando fondo de pantalla de Selección 1
    ventanaSeleccion2.blit(fondoVentanaSeleccion2, (0,0)) #Visualizar el fondo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//botondeRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (45, 45)) #Ajustando el tamaño
    ventanaSeleccion2.blit(botonRegreso, (10,10)) #Visualizar la imagen con su posición
    # ---- Imágen de los jugadores ----
    imagenKane = pygame.image.load("Imagenes//Raphinha.png") #Agregando imagen de Raphinha
    imagenKane = pygame.transform.scale(imagenKane, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion2.blit(imagenKane, (100,130)) #Visualizar la imagen con su posición
    imagenMuller = pygame.image.load("Imagenes//RobertLewandowski.png") #Agregando imagen de Lewandowski
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMuller, (360,130)) #Visualizar la imagen con su posición
    imagenMusiala = pygame.image.load("Imagenes//FerranTorres.png") #Agregando imagen de Torres
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMusiala, (615,130)) #Visualizar la imagen con su posición
    # ---- Imágen de los botones de selección jugadores----
    # ---- Imágenes Seleccionadas ----
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion2.blit(imagenSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion2.blit(imagenSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
    imagenSeleccionadaOpcion3 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion3 = pygame.transform.scale(imagenSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaSeleccion2.blit(imagenSeleccionadaOpcion3, (800,180)) #Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenNoSeleccionadaOpcion1 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion1 = pygame.transform.scale(imagenNoSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion2.blit(imagenNoSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion2 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion2 = pygame.transform.scale(imagenNoSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion2.blit(imagenNoSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion3 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion3 = pygame.transform.scale(imagenNoSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaSeleccion2.blit(imagenNoSeleccionadaOpcion3, (800,180)) #Visualizar la imagen con su posición
    # ---- Imágen de los porteros ----
    imagenKane = pygame.image.load("Imagenes//Claudio Bravo.png") #Agregando imagen de Bravo
    imagenKane = pygame.transform.scale(imagenKane, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion2.blit(imagenKane, (100,432)) #Visualizar la imagen con su posición
    imagenMuller = pygame.image.load("Imagenes//IñakiPeña.png") #Agregando imagen de Peña
    imagenMuller = pygame.transform.scale(imagenMuller, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMuller, (360,432)) #Visualizar la imagen con su posición
    imagenMusiala = pygame.image.load("Imagenes//Stegen.png") #Agregando imagen de Stegen
    imagenMusiala = pygame.transform.scale(imagenMusiala, (180, 175)) #Ajustando el tamaño
    ventanaSeleccion2.blit(imagenMusiala, (615,432)) #Visualizar la imagen con su posición
    # ---- Imágen de los botones de selección porteros----
    # ---- Imágenes Seleccionadas ----
    imagenSeleccionada1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion2.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
    imagenSeleccionada2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion2.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
    imagenSeleccionada3 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3Por = ventanaSeleccion2.blit(imagenSeleccionada3, (800,482)) #Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenSeleccionada1 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion2.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
    imagenSeleccionada2 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion2.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
    imagenSeleccionada3 = pygame.image.load("Imagenes//apagado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada3 = pygame.transform.scale(imagenSeleccionada3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3Por = ventanaSeleccion2.blit(imagenSeleccionada3, (800,482)) #Visualizar la imagen con su posición
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
            ventanaSeleccion2.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaJugadores else imagenNoSeleccionadaOpcion1, posicionOpcion1)
            ventanaSeleccion2.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaJugadores else imagenNoSeleccionadaOpcion2, posicionOpcion2)
            ventanaSeleccion2.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaJugadores else imagenNoSeleccionadaOpcion3, posicionOpcion3)
            # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
            ventanaSeleccion2.blit(imagenSeleccionadaOpcion1 if opcion1SeleccionadaPorteros else imagenNoSeleccionadaOpcion1, posicionOpcion1Por)
            ventanaSeleccion2.blit(imagenSeleccionadaOpcion2 if opcion2SeleccionadaPorteros else imagenNoSeleccionadaOpcion2, posicionOpcion2Por)
            ventanaSeleccion2.blit(imagenSeleccionadaOpcion3 if opcion3SeleccionadaPorteros else imagenNoSeleccionadaOpcion3, posicionOpcion3Por)
        pygame.display.flip() #Actualizar Pantalla
# ----------------------------------- Finalizando la Ventana de Selección 2 ---------------------------------

# ----------------------------------- Iniciando la Ventana de Selección 3 -----------------------------------
def screenSeleccion3():
    global enSeleccionEquipo #Globalizando mi variable para saber si estoy en ventanas de selección de jugadores
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
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaSeleccion3.blit(imagenSeleccionadaOpcion1, (280,180)) #Visualizar la imagen con su posición
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaSeleccion3.blit(imagenSeleccionadaOpcion2, (540,180)) #Visualizar la imagen con su posición
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
    imagenSeleccionada1 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada1 = pygame.transform.scale(imagenSeleccionada1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1Por = ventanaSeleccion3.blit(imagenSeleccionada1, (280,482)) #Visualizar la imagen con su posición
    imagenSeleccionada2 = pygame.image.load("Imagenes//encendido.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionada2 = pygame.transform.scale(imagenSeleccionada2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2Por = ventanaSeleccion3.blit(imagenSeleccionada2, (540,482)) #Visualizar la imagen con su posición
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
def screenJuego():
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaInformacion = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    ventanaInformacion.fill("#FFC154") #Color de fondo
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
