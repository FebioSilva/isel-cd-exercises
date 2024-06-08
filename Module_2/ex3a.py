import serial

def main():
    # Conectar ao Arduino via porta serial
    arduino = serial.Serial('COM3', 9600)

    while True:
        data = arduino.read()
        dataToPrintInDecimal = int.from_bytes(data, byteorder='big')
        print(dataToPrintInDecimal)
if __name__ == "__main__":
    main()