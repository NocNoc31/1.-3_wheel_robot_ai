import threading
import serial

# ser = serial.Serial(
#     "COM10", 9600, timeout=1
# )  # Change your port name COM... and your baudrate

#USING HC0

def send_detect_cmd(ser, number):
    try:
        if number == 0:
            ser.write(b"0")  # Send "0" command to stop
        elif number == 1:
            ser.write(b"w")  # Send "w" command to move forward
        elif number == 2:
            ser.write(b"s")  # Send "s" command to move backward
        elif number == 3:
            ser.write(b"d")  # Send "d" command to turn right
        elif number == 4:
            ser.write(b"a")  # Send "a" command to turn left
    except Exception as e:
        print(f"Error sending command: {e}")


thread2 = threading.Thread(target=send_detect_cmd)
thread2.start()  # phan luong cho get key chay
