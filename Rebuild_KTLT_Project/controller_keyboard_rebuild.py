# Import thư viện liên quan
import serial
import time
import threading
from pynput.keyboard import Listener

# ser = serial.Serial("COM10", 9600, timeout=1)
# time.sleep(0.5)

# Các hàm cơ bản: Tiến, Lùi, Phải, Trái


def forward():  # Tiến
    ser.write(b"w")


def stop():  # Dừng
    ser.write(b"0")


def reverse():  # Lùi
    ser.write(b"s")


def turn_left():  # Trái
    ser.write(b"a")


def turn_right():  # Phải
    ser.write(b"d")


value = ""
value2 = ""


def on_press(key):  # Hàm chạy khi nhấn nút
    global value  # Giá trị kiểm tra xe đang tiến
    global value2  # Giá trị kiểm tra xe đang lùi

    try:  # Các nút khi được bấm
        if key.char == "w":
            value = 1
            forward()
        elif key.char == "a":
            turn_left()
        elif key.char == "d":
            turn_right()
        elif key.char == "s":
            value2 = 1
            reverse()
        elif key.char == "k":
            return False
        else:
            stop()
    except:
        stop()


def on_release(key):  # Hàm chạy khi nhả nút
    global value
    global value2

    try:  # Các nút khi được nhả ra
        if key.char == "w":
            value = 0
            stop()
        if key.char == "s":
            value2 = 0
            stop()
        elif key.char == "a" or key.char == "d":
            if value == 1:  # Xe tiến
                forward()
            elif value2 == 1:  # Xe lùi
                reverse()
        else:
            stop()
    except:
        stop()


def get_key():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


thread1 = threading.Thread(target=get_key)
thread1.start()  # Tạo ra một luồng
