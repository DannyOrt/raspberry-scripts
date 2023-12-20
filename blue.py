import subprocess
import time

def make_visible():
    try:
        subprocess.run(['sudo', 'hciconfig', 'hci0', 'piscan'])
        print("Bluetooth visible para emparejamiento.")
    except Exception as e:
        print(f"Error al hacer visible el Bluetooth: {e}")

def pair_devices():
    try:
        subprocess.run(['sudo', 'bluetoothctl', 'discoverable', 'on'])
        subprocess.run(['sudo', 'bluetoothctl', 'pairable', 'on'])
        print("Esperando emparejamiento...")
        time.sleep(35)  # Ajusta el tiempo según tus necesidades
    except Exception as e:
        print(f"Error al configurar el emparejamiento: {e}")

def list_paired_devices():
    try:
        result = subprocess.run(['sudo', 'bluetoothctl', 'paired-devices'], capture_output=True, text=True, check=True)
        paired_devices = result.stdout.split('\n')
        paired_devices = [device.strip() for device in paired_devices if device.strip()]
        print("Dispositivos emparejados:")
        for device in paired_devices:
            print(device)
    except Exception as e:
        print(f"Error al obtener la lista de dispositivos emparejados: {e}")

def main():
    try:
        make_visible()
        pair_devices()
        list_paired_devices()
    except KeyboardInterrupt:
        print("Proceso interrumpido por el usuario.")
    finally:
        print("Apagando Bluetooth.")
        subprocess.run(['sudo', 'hciconfig', 'hci0', 'noscan'])

if __name__ == "__main__":
    main()
