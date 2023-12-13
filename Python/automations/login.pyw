import psutil
from datetime import datetime
import time

# def get_login_time():
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def get_logout_time():
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_event(event):
    with open("login_logout_log.txt", "a") as log_file:
        log_file.write(f"{event} time: {datetime.now()}\n\n")

def monitor_login_logout():
    while True:
        if psutil.users():
            # User is logged in
            log_event("Login")
        else:
            # User is logged out
            log_event("Logout")
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    try:
        log_event("Script started")
        monitor_login_logout()
    except KeyboardInterrupt:
        log_event("Script terminated by user")
    except Exception as e:
        log_event(f"Error: {str(e)}")
