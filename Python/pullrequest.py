import subprocess
import os

pythonPath = "D:\\Vscode-All scripts\\All_in_one\\Python"

select = input("Please select the Folder which do you want to update?\n==> for python press [1]\n==> for other press [2]\n==>").lower()

if select == "1" or select == "python":
    pythonPath


pullPush = input("Please enter want to pull or push?\n==> for push press [1]\n==> for pull press [2]\n==>").lower()

if pullPush == "push" or pullPush == "1":
    print("pushing data")
    subprocess.call(['git','status'] ,cwd=pythonPath)
    subprocess.call(['git','add','-A'] ,cwd=pythonPath)
    subprocess.call(['git','commit','-m','pushed code through python'] ,cwd=pythonPath)
    subprocess.call(['git','push'] ,cwd=pythonPath)
    
elif pullPush == "pull" or pullPush == "2":
    print("pulling data")
    subprocess.call(['git','status'] ,cwd=pythonPath)
else:
    print("something wet wrong please try again.. dewani")