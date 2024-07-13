import pyautogui
import time

"""

This script run only when tasks fields failed to update the required fields

main scripts me jub tasks script kam nhi karta jub ye script run karo wo sub fields update kardega
"""



# tasks = [(600,262),(600,305),(600,339),(600,374),(600,415),(600,450),(600,485),(600,520),(600,555),(600,590),(600,625),(603,674),(603,706),(603,744),(603,779),(603,814)]
hours = [(650,262),(650,305),(650,339),(650,374),(650,415),(650,450),(650,485),(650,520),(650,555),(650,590),(650,625),(650,674),(650,706),(650,744),(650,779),(650,814)]

try:
    pyautogui.hotkey("win","5")
    time.sleep(2)
    for prj in hours:
        #print(plus)
        pyautogui.moveTo(prj,duration=0.2)
        pyautogui.click(prj)
        time.sleep(0.2)
        pyautogui.hotkey("ctrl","a")
        time.sleep(0.2)
        pyautogui.typewrite("08:00")
        # pyautogui.moveTo(prj[0],prj[1]+31,duration=0.2)
        # pyautogui.click(prj[0],prj[1]+46)
        # #print(prj[0],prj[1]+30)
        # time.sleep(0.8)

except Exception:
    print("error5")



