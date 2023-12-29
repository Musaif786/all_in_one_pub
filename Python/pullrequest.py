import subprocess
import os
import time

pythonPath = "D:\\Vscode-All scripts\\All_in_one\\Python"
reactPath = "D:\\Vscode-All scripts\\react-js\\Tudolist"

print(30*"#")
select = input("Please select the Folder which do you want to update?\n==> for python/terraform press [1]\n==> for react project press [2]\n==>for others press [3]").lower()

if select == "1" or select == "python" or select == "terraform":
    path = pythonPath
elif select == "2" or select == "react" :
    path = reactPath
elif select == "3" or select == "others" :
    path = reactPath
else:
    print("under process")


pullPush = input("Please enter want to pull or push?\n==> for push press [1]\n==> for pull press [2]\n==>for status press [3]\n==>").lower()

if pullPush == "push" or pullPush == "1":
    try:
        print("pushing data")
        subprocess.call(['git','status'] ,cwd=path)
        subprocess.call(['git','add','-A'] ,cwd=path)
        subprocess.call(['git','commit','-m','pushed code through python'] ,cwd=path)
        subprocess.call(['git','push'] ,cwd=path)
    except NameError as e:
        print(30*"#")
        print("Please try again with correct option")
        print(30*"#")
    
elif pullPush == "pull" or pullPush == "2":
    print("pulling data")
    subprocess.call(['git','status'] ,cwd=path)
    
elif pullPush == "status" or pullPush == "3":
    print("pulling data")
    subprocess.call(['git','status'] ,cwd=path)
else:
    print(30*"*")
    print("something wet wrong please try again....")
    print(30*"*")

time.sleep(5)