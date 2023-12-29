import subprocess
import os
import time

pythonPath = "D:\\Vscode-All scripts\\All_in_one\\Python"
print(30*"#")
select = input("Please select the Folder which do you want to update?\n==> for python/terraform press [1]\n==> for other press [2]\n==>").lower()

if select == "1" or select == "python" or select == "terraform":
    python_Path = pythonPath
else:
    print("under process")


pullPush = input("Please enter want to pull or push?\n==> for push press [1]\n==> for pull press [2]\n==>").lower()

if pullPush == "push" or pullPush == "1":
    try:
        print("pushing data")
        subprocess.call(['git','status'] ,cwd=python_Path)
        subprocess.call(['git','add','-A'] ,cwd=python_Path)
        subprocess.call(['git','commit','-m','pushed code through python'] ,cwd=python_Path)
        subprocess.call(['git','push'] ,cwd=python_Path)
    except NameError as e:
        print(30*"#")
        print("Please try again with correct option")
        print(30*"#")
    
elif pullPush == "pull" or pullPush == "2":
    print("pulling data")
    subprocess.call(['git','status'] ,cwd=pythonPath)
else:
    print(30*"*")
    print("something wet wrong please try again...")
    print(30*"*")

time.sleep(5)