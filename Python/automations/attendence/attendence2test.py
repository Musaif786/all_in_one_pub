import pyautogui
import time
import tasksvalidate as tk
import sys

"""

it will work only on zoom 80% for webpage

CG SIRI Engineering & Support Services [P000271]
EMP Consulting Hour [607]
08:00


cords: [(108,312),(108,359)]
"""
delete = [(177,261),(177,300),(177,340),(177,380),(177,420),(177,450),(177,490),(177,530),(177,560),(177,595),(177,630),(177,670),(177,705),(177,745),(177,780),(177,815)]
plusbtn = [(90,262),(89,300),(89,337),(89,374),(89,409),(89,449),(89,486),(89,522),(89,560),(89,596),(89,634),(89,670),(89,707),(89,745),(89,780),(89,818)]

# project =[(427,262),(427,305),(427,339),(427,374),(427,415),(427,450),(427,485),(427,520),(427,555),(427,590),(427,625),(427,660),(427,695),(427,730),(427,765),(427,800)]
project =[(427,262),(427,305),(427,339),(427,374),(427,415),(427,450),(427,485),(427,520),(427,555),(427,590),(427,625),(430,674),(430,706),(430,744),(430,779),(430,814)]




# tasks = [(600,265),(600,305),(600,345),(600,385),(600,425),(600,465),(600,505),(600,545),(600,585),(600,622),(600,662),(600,702),(600,742),(600,782),(600,822),(600,862)]
tasks = [(600,262),(600,305),(600,339),(600,374),(600,415),(600,450),(600,485),(600,520),(600,555),(600,590),(600,625),(603,674),(603,706),(603,744),(603,779),(603,814)]
# tasks = [(600,262),(600,305)]

hours = [(650,262),(650,305),(650,339),(650,374),(650,415),(650,450),(650,485),(650,520),(650,555),(650,590),(650,625),(650,674),(650,706),(650,744),(650,779),(650,814)]




############
 #functions

def tasksFun(project, count):
    projects = project
    for prj in projects:
        #print(plus)
        pyautogui.moveTo(prj,duration=0.2)
        pyautogui.click(prj)
        pyautogui.moveTo(prj[0],prj[1]+count,duration=0.2)
        pyautogui.click(prj[0],prj[1]+count)
        #print(prj[0],prj[1]+30)
        time.sleep(0.8)


def findpng():
    count = 0
    while True:
        submitBtn = pyautogui.locateOnScreen("Not submitted.png")
        if submitBtn:
            pyautogui.moveTo(submitBtn)
            pyautogui.click(submitBtn)
            break
        elif count >=100:
             print("Failed to find the image, try again")
             sys.exit()

        else:
            print("finding image pls wait")
            count += 1
            continue
        

def deleteExistingValuesAndAddingFun(delete):
        for delte in delete:
            #print(plus)
            pyautogui.moveTo(delte,duration=0.2)
            pyautogui.click(delte)
            time.sleep(0.2)




def hoursAddingFun(hours):
       for prj in hours:
            #print(plus)
            pyautogui.moveTo(prj,duration=0.2)
            pyautogui.click(prj)
            time.sleep(0.2)
            pyautogui.hotkey("ctrl","a")
            time.sleep(0.2)
            pyautogui.typewrite("08:00")


try:
    time.sleep(3)
    pyautogui.hotkey("win","5")
    time.sleep(2)
    pyautogui.hotkey("ctrl","t")
    time.sleep(3)
    pyautogui.typewrite("https://solugenix.criterionhcm.com/ui/#dashboard")
    pyautogui.press("enter")
    time.sleep(5)
    #timesheet
    pyautogui.moveTo(30,224)
    pyautogui.press("enter")
    time.sleep(1)
    #click on my timesheet inside
    pyautogui.moveTo(74,225)
    pyautogui.press("enter")

    time.sleep(5)


    #finding not submit png
    findpng()

    # print(pyautogui.locateOnScreen("Not submitted.png"))
    # pyautogui.click(31,262)
    time.sleep(3)

    #  # Delete all plus
    deleteExistingValuesAndAddingFun(delete)

    time.sleep(3)
    deleteExistingValuesAndAddingFun(plusbtn)
    # # click plus buttons
    
    prject_count = 31
    tasks_counts = 46

    tasksFun(project,prject_count)
    time.sleep(3)
    tasksFun(tasks,tasks_counts)

    #update the times or 8 hours
    hoursAddingFun(hours)

    time.sleep(3)
    print("validating...")
    try:
        tk.tasksMainFun(tasks)
    except:
         pass

except Exception:
    print("Something went wrong, please try again...")







