import pyautogui as py


try:
    while True:
        position = py.position()
        print(position)
except KeyboardInterrupt as k:
    print("Terminated")

