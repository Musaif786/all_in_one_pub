import os

try:
    import pyautogui 
    print("Module found")

except ModuleNotFoundError:
    print("Module not found")

#print("Musaif")

while True:
    userInput = input('Please enter q to quite:')

    if userInput == "q":
        break
    else:
        print("Hello world..")
