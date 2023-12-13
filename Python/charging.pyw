import psutil
import pyautogui as ui
from plyer import notification
import pyttsx3

speak = pyttsx3


print("Checking Battery Status for every 5 mins..")
def check_battery():
    battery = psutil.sensors_battery()
    if battery.percent <= 30 and not battery.power_plugged:
        message = f"Battery is low at {battery.percent}% Please plug-in your charger."
        notification.notify(
            title="Battery Alert",
            message=message,
            app_name="Battery Checker",
        )
        speak.speak(message)
        ui.alert(message)
    elif battery.percent >= 95 and battery.power_plugged:
        message = f"Battery is full at {battery.percent}%, Please Un-plug the charger."
        
        notification.notify(
            title="Battery Alert",
            message=message,
            app_name="Battery Checker",
        )
        speak.speak(message)
        ui.alert(message)


try:
    while True:
        check_battery()
        ui.sleep(300)  # Check every 5 minutes (300 seconds)
except KeyboardInterrupt:
    print("job Terminated")
    ui.sleep(5)
    
