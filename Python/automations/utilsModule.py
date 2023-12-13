import psutil

# Get a list of all running processes
process_list = psutil.process_iter()
for process in process_list:
    print(f"Process Name: {process.name()}, PID: {process.pid}")
