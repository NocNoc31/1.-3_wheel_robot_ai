import serial


ser = serial.Serial(
    "COM5", 9600, timeout=1
)  # Change your port name COM... and your baudrate


def retrieveData():
    ser.write(b"w")


while True:
    uInput = input("Retrieve data? ")
    if uInput == "w":
        print(retrieveData())
    else:
        ser.write(b"0")
