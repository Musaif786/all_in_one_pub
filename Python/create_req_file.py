
import os

def create_req_file():
    if not os.path.isfile("requirement.txt"): # file nhi hai to create karo warna nhi
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirement.txt'), 'w'):
            print('created')
            
        return
    else: # else part is only for validation 
        print(os.path.abspath(__file__)) # this path #d:\Vscode-All scripts\All_in_one\Python\create_req_file.py
        print(os.path.dirname(os.path.abspath(__file__))) #d:\Vscode-All scripts\All_in_one\Python\  only directory
    

create_req_file()
#print(os.path.abspath(__file__))
print(os.getcwd())