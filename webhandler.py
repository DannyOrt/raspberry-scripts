import socketio
import RPi.GPIO as GPIO
import time

io = socketio.Client()

# Marcamos nuestros pines
RELE_PIN = 3  # abre y cierra el agua
RELE2_PIN = 4  # abre y cierra el gas


# Hay que verficar que pin abre cual electrovalvula
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELE_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RELE2_PIN, GPIO.OUT, initial=GPIO.LOW)

time.sleep(20)

# Valves
def close_valve1():
    GPIO.output(RELE_PIN, GPIO.HIGH)
    print('Electroválvulas cerradas')


def open_valve1():
    GPIO.output(RELE_PIN, GPIO.LOW)
    print('Electroválvulas abiertas')


def close_valve2():
    GPIO.output(RELE2_PIN, GPIO.HIGH)
    print('Electroválvulas cerradas')


def open_valve2():
    GPIO.output(RELE2_PIN, GPIO.LOW)
    print('Electroválvulas abiertas')


def handle_responses(response):
    # se tienen diferentes respuestas como OpenWater, CloseWater, OpenGas, CloseGas, OpenAll, CloseAll
    # se debe de manejar cada una de ellas

    if response == 'OpenWater':
        open_valve1()
    elif response == 'CloseWater':
        close_valve1()
    elif response == 'OpenGas':
        open_valve2()
    elif response == 'CloseGas':
        close_valve2()
    elif response == 'OpenAll':
        open_valve1()
        open_valve2()
    elif response == 'CloseAll':
        close_valve1()
        close_valve2()
    else:
        print('No se reconoce la respuesta')


@io.event
def message(data):
    print('message received with ', data)
    handle_responses(data)


@io.event
def disconnect():
    print('disconnected from server')


io.connect('https://pickled-capricious-chickadee.glitch.me/')
io.emit("join", "SCR-VAL-007")
io.wait()
