import pyautogui as py
import time

try:
    while True:
        position = py.position()
        print(position)
        time.sleep(0.5)
        
except KeyboardInterrupt as k:
    print("Terminated")

