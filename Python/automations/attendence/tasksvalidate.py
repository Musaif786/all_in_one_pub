import pyautogui
import time

"""

This script run only when tasks fields failed to update the required fields

main scripts me jub tasks script kam nhi karta jub ye script run karo wo sub fields update kardega
"""



tasks = [(600,262),(600,305),(600,339),(600,374),(600,415),(600,450),(600,485),(600,520),(600,555),(600,590),(600,625),(603,674),(603,706),(603,744),(603,779),(603,814)]
def tasksMainFun(tasks):
    try:
        # pyautogui.hotkey("win","5")
        time.sleep(2)
        for prj in tasks:
            #print(plus)
            pyautogui.moveTo(prj,duration=0.2)
            pyautogui.click(prj)
            pyautogui.moveTo(prj[0],prj[1]+31,duration=0.2)
            pyautogui.click(prj[0],prj[1]+46)
            #print(prj[0],prj[1]+30)
            time.sleep(0.8)
        
        print("successfully updated timesheet")

    except Exception:
        print("error5")

if __name__=="__main__":
    tasksMainFun(tasks)



