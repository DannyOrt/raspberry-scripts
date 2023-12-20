import time
import requests
import RPi.GPIO as GPIO


RELE_PIN = 3  # Reemplazar con el número del pin GPIO conectado a la electroválvula 1
RELE2_PIN = 4  # Reemplazar con el número del pin GPIO conectado a la electroválvula 2
API_URL = 'https://sea-turtle-app-mv9s4.ondigitalocean.app/api/sismo' # Remplazar con la url final del proyecto web

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELE_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RELE2_PIN, GPIO.OUT, initial=GPIO.LOW)


def check_api_and_control_valves():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            print('API devuelve estado 200 - Cerrando electroválvulas')
            close_valves()
            # Espera 5 minutos antes de abrir las electroválvulas
            time.sleep(300)
            # Se abren las valvulas
            open_valves()
            
        else:
            print(f'API devuelve estado {response.status_code} - No se realiza ninguna acción')

    except Exception as e:
        print(f'Error al realizar la solicitud a la API: {e}')


def close_valves():
    GPIO.output(RELE_PIN, GPIO.HIGH)
    GPIO.output(RELE2_PIN, GPIO.HIGH)
    print('Electroválvulas cerradas')


def open_valves():
    GPIO.output(RELE_PIN, GPIO.LOW)
    GPIO.output(RELE2_PIN, GPIO.LOW)
    print('Electroválvulas abiertas')


def main():
    # Verificar la API cada 5 segundos
    time.sleep(20)
    while True:
        #time.sleep(60)
        check_api_and_control_valves()
        time.sleep(5)  # Espera 5 segundos entre iteraciones


if __name__ == "__main__":
    main()
