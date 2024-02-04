import string
import random



def fromFile():

    filename = ""
    with open(filename,"r+") as f:
      file = file.read()
      return file
    
def passwordCrack(passwd):
    try:
        
        if (char.isdigit() for char in passwd):
            pass


        # if have any file and want to find passwrd from the file then use file method to find the passowrd.
        filetoCheck = fromFile()


        #variables
        count = 0
        while True:
            check = "".join(random.choices(string.ascii_letters + string.digits, k=len(passwd)))
            count += 1
            print(check)  # verbose mode

            if check == passwd:    # or passwd in filetoCheck:
                print(f"Password is : {passwd} \nFound at {count} attempts")
                break
            if count >=500000:
                # print(f"Tried {check} times, password not found Please try again...")
                break
    except KeyboardInterrupt:
        print("Job Terminated!")


password = input("Enter your password: ")
passwordCrack(password)