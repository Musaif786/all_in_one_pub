import os
import time

try:
    import tqdm
except ModuleNotFoundError:
    print('Module is not installed. Installing the module...')
    time.sleep(2)
    os.system("pip install tqdm")
    print('Waiting for the module to be installed...')
    time.sleep(5)  # Adjust the time delay as needed
    import tqdm  # Import the module again after installation

print(dir(tqdm))
