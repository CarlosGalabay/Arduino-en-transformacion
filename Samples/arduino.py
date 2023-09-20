import serial, time

# Establece la conexión serie con el puerto COM correcto y la velocidad de baudios
arduino = serial.Serial('COM3', 9600)  # Reemplaza 'COMX' con el puerto COM correcto y la velocidad de baudios adecuada

while True:
    ingreso = input("ingreso: ")
    # Envía datos al Arduino
    arduino.write(ingreso.encode())  # Convierte los datos a bytes antes de enviarlos
    time.sleep(2)

# Cierra la conexión serie cuando hayas terminado
arduino.close()
