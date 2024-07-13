import pyautogui
import time

"""

it will work only on zoom 80% for webpage

CG SIRI Engineering & Support Services [P000271]
EMP Consulting Hour [607]
08:00


cords: [(108,312),(108,359)]
"""
delete = [(177,261),(177,300),(177,340),(177,380),(177,420),(177,450),(177,490),(177,530),(177,560),(177,595),(177,630),(177,670),(177,705),(177,745),(177,780),(177,815)]
plusbtn = [(90,262),(89,300),(89,337),(89,374),(89,409),(89,449),(89,486),(89,522),(89,560),(89,596),(89,634),(89,670),(89,707),(89,745),(89,780),(89,818)]

project =[(427,262),(427,305),(427,339),(427,374),(427,415),(427,450),(427,485),(427,530),(428,570),(427,612),(427,648),(427,687),(427,722),(427,762),(427,798),(427,834)]

tasks = [(600,262),(600,300),(600,342),(600,382),(600,422),(600,462),(600,502),(600,542),(600,582),(600,622),(600,662),(600,702),(600,742),(600,782),(600,822),(600,862)]

#insideproject = [(405,262),(412,300),(418,337),(427,391),(427,430),(427,466),(427,503),(427,542),(427,575),(427,612),(427,648),(427,687),(427,722),(427,762),(427,798),(427,834)]
try:
    pyautogui.hotkey("win","5")
    time.sleep(1)
    # pyautogui.hotkey("clt","t")
    # # time.sleep(3)
    # pyautogui.typewrite("https://solugenix.criterionhcm.com/ui/#dashboard")
    # pyautogui.press("enter")
    # time.sleep(5)
    # #timesheet
    # pyautogui.moveTo(30,224)
    # pyautogui.press("enter")
    # time.sleep(1)
    # #click on my timesheet inside
    # pyautogui.moveTo(74,225)
    # pyautogui.press("enter")

    # time.sleep(5)
    # #finding not submit png
    # submitBtn = pyautogui.locateOnScreen("Not submitted.png")
    # pyautogui.moveTo(submitBtn)
    # pyautogui.click(submitBtn)
    #print(pyautogui.locateOnScreen("Not submitted.png"))
    # pyautogui.click(31,262)
    time.sleep(5)

     # Delete all plus
    for delte in delete:
        #print(plus)
        pyautogui.moveTo(delte,duration=0.5)
        pyautogui.click(delte)
        time.sleep(0.2)

    # time.sleep(5)
    # # click plus buttons
    for plus in plusbtn:
        #print(plus)
        pyautogui.click(plus)
        time.sleep(0.2)

    # time.sleep(5)
    # # # click and select project
    # for prj in project:
    #     #print(plus)
    #     pyautogui.moveTo(prj,duration=0.8)
    #     pyautogui.click(prj)
    #     pyautogui.moveTo(prj[0],prj[1]+31,duration=0.8)
    #     pyautogui.click(prj[0],prj[1]+31)
        #print(prj[0],prj[1]+30)
        # time.sleep(0.8)

    # time.sleep(5)  
    # for prj in tasks:
    #     #print(plus)
    #     pyautogui.click(prj)
    #     pyautogui.click(prj[0],prj[1]+48)
    #     #print(prj[0],prj[1]+30)
    #     time.sleep(0.8)

except Exception:
    print("error5")



