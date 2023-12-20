import serial
import RPi.GPIO as GPIO
import time
import bluetooth

RELE_PIN = 3
RELE2_PIN = 4  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELE_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RELE2_PIN, GPIO.OUT, initial=GPIO.LOW)


def open_valve(rele_pin):
    GPIO.output(rele_pin, GPIO.LOW)
    valmag = 6.3
    #ser.write(str(valmag).encode('utf-8'))
    time.sleep(0.4)

def close_valve(rele_pin):
    GPIO.output(rele_pin, GPIO.HIGH)


host = "00:00:00:00:00:00"
port = 3
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Se creo el servidor bluetooth")

try:
    server.bind((host, port))
    print("Bulding completo")
except:
    print("No se creo el building")

server.listen(1)

client, direction = server.accept()

print(f"El cliente es: {client}, a direccion: {direction}")


try:
    while True:
        data = client.recv(1024)

        if data == '01':  # Command to open valve 1
            open_valve(RELE_PIN)
        elif data == '00':  # Command to close valve 1
            close_valve(RELE_PIN)
        elif data == '11':  # Command to open valve 2
            open_valve(RELE2_PIN)
        elif data == '10':  # Command to close valve 2
            close_valve(RELE2_PIN)
        elif data == '100':  # Command to close all valve
            close_valve(RELE2_PIN)
        elif data == '101':  # Command to close all valve
            close_valve(RELE2_PIN)
        else:
            print(data)
except KeyboardInterrupt:
    client.close()
    server.close()
