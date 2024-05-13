import usocket as socket
from machine import Pin
import network
import utime

ssid = 'Cami'
password = '11.calibre11.'

wf = network.WLAN(network.STA_IF)
wf.active(True)
wf.connect(ssid, password)
while not wf.isconnected():
    print("No está conectado")
print("Conectado con éxito.")
print("Dirección IP asignada:", wf.ifconfig()[0])

s = socket.socket()
s.bind(("192.168.43.114", 2025))
s.listen(13)
print("Servidor iniciado")

continuar1 = True

def encender():
    print("Encendiendo...")  # Aquí puedes realizar acciones específicas de tu programa en lugar de encender un LED.

while continuar1:
    (sc, addr) = s.accept()
    print("Cliente conectado:", addr)
    continuar2 = True 
    while continuar2:
        mensaje = sc.recv(64)
        if not mensaje:
            continuar2 = False
        elif mensaje.decode() == "funcion":
            encender()
        elif mensaje.decode() == "fin":
            continuar1 = False
            continuar2 = False
            print("Mensaje de finalización recibido.")
        else:
            mensaje.decode()
    sc.close()

s.close()
print("Fin del programa")

#Averiguando IP de la Raspberry
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a la red WiFi...')
        wlan.connect('Cami', '11.calibre11.')
        while not wlan.isconnected():
            pass
    print('Conexión WiFi establecida:', wlan.ifconfig())

pines_tornillos = [Pin(pin_num, Pin.IN) for pin_num in [0, 2, 4, 6, 19, 11]]
pines_led = [Pin(pin_led, Pin.OUT) for pin_led in [18, 21, 14, 13, 9, 28]]

# Variable para mantener el estado del gol
gol_activo = False

def detectar_paleta1():
    while True:
        Paleta1 = digitalio.DigitalInOut(Pin.GP0)
        Paleta1.direction = digitalio.Direction.INPUT
        if Paleta1.value():
            apagar_leds()
        else:
            encender_leds()
def detectar_paleta2():
    while True:
        Paleta2 = digitalio.DigitalInOut(Pin.GP2)
        Paleta2.direction = digitalio.Direction.INPUT
        if Paleta2.value():
            apagar_leds()
        else:
            encender_leds()
def detectar_paleta3():
    while True:
        Paleta3 = digitalio.DigitalInOut(Pin.GP4)
        Paleta3.direction = digitalio.Direction.INPUT
        if Paleta3.value():
            apagar_leds()
        else:
            encender_leds()
def detectar_paleta4():
    while True:
        Paleta4 = digitalio.DigitalInOut(Pin.GP6)
        Paleta4.direction = digitalio.Direction.INPUT
        if Paleta4.value():
            apagar_leds()
        else:
            encender_leds()
def detectar_paleta5():
    while True:
        Paleta5 = digitalio.DigitalInOut(Pin.GP19)
        Paleta5.direction = digitalio.Direction.INPUT
        if Paleta5.value():
            apagar_leds()
        else:
            encender_leds()
def detectar_paleta6():
    while True:
        Paleta6 = digitalio.DigitalInOut(Pin.GP11)
        Paleta6.direction = digitalio.Direction.INPUT
        if Paleta6.value():
            apagar_leds()
        else:
            encender_leds()
   

def encender_leds():
    for led in pines_led:
        led.value(1)

    # Esperar un segundo antes de apagar los LEDs
    utime.sleep(0.5)

    # Apagar todos los LEDs
    for led in pines_led:
        led.value(0)

def apagar_leds():
    # Apagar todos los LEDs
    for led in pines_led:
        led.value(0)

detectar_paleta1()
detectar_paleta2()
detectar_paleta3()
detectar_paleta4()
detectar_paleta5()
detectar_paleta6()