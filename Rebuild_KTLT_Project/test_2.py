import threading
from pynput.keyboard import Key, Listener
import sys
import cv2

# import pyfirmata

value = ""
value2 = ""


def forward():
    print("1")


def stop():
    print("0")


def reverse():
    print("2")


def turn_right():
    print("3")


def turn_left():
    print("4")


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
