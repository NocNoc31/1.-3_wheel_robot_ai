import threading
from pynput.keyboard import Key, Listener
import sys
import cv2
import pyfirmata
import time

board = pyfirmata.Arduino("COM5")

time.sleep(2.0)


pin_2 = board.get_pin("d:2:o")
pin_3 = board.get_pin("d:3:p")
pin_4 = board.get_pin("d:4:o")
pin_5 = board.get_pin("d:5:o")
pin_6 = board.get_pin("d:6:p")
pin_7 = board.get_pin("d:7:o")

speed = 0.5

value = ""
value2 = ""
condition = True


def forward():
    global speed
    pin_3.write(speed)
    pin_5.write(0)
    pin_7.write(1)
    pin_6.write(speed)
    pin_2.write(0)
    pin_4.write(1)


def stop():
    pin_3.write(0)
    pin_5.write(0)
    pin_7.write(0)
    pin_6.write(0)
    pin_2.write(0)
    pin_4.write(0)


def reverse():
    global speed
    pin_3.write(speed)
    pin_7.write(0)
    pin_5.write(1)
    pin_6.write(speed)
    pin_4.write(0)
    pin_2.write(1)


def turn_right():
    global speed
    pin_3.write(speed - 0.2)  # speed
    pin_7.write(1)
    pin_5.write(0)
    pin_6.write(0)  # speed
    pin_4.write(0)  # 0
    pin_2.write(0)  # 1


def turn_left():
    global speed
    pin_3.write(0)  # speed
    pin_7.write(0)  # 0
    pin_5.write(0)  # 1
    pin_6.write(speed - 0.2)  # speed
    pin_4.write(1)
    pin_2.write(0)


def exit_program():
    print("Exiting the program...")
    sys.exit(0)


def on_press(key):  # ham chay khi nhan nut
    global value  # gia tri de check xe dang tien
    global value2  # gia tri de check xe dang lui
    try:
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
        elif key.char == "q":
            return False
        else:
            stop()
    except:
        stop()


def on_release(key):  # Ham chay khi nha nut
    global value
    global value2
    try:
        if key.char == "w":  # neu phim w duoc nha ra
            value = 0
            stop()
        if key.char == "s":
            value2 = 0
            stop()
        elif key.char == "a" or key.char == "d":
            if value == 1:  # xe dang tien
                forward()
            elif value2 == 1:  # xe dang lui
                reverse()
        else:
            stop()
    except:
        stop()


def get_key():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def detect(count, fingerUp):
    if fingerUp == [0, 0, 0, 0, 0]:
        stop()
    elif count == 1:
        forward()
    elif count == 2:
        reverse()
    elif count == 3:
        turn_right()
    elif count == 4:
        turn_left()
