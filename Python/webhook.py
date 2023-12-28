import webhook_url as url
import requests

urlMain = url.urlFun()


def reqFun(params):
    try:
        res = requests.get(urlMain, params=params)
        if res.status_code == 200:
            print("Successfully submitted request")
        else:
            print("Faild to submit request")
    except:
        print("Error")

def mainFun(): 
    
    gatherInfo = input("What action do you want to perform?\n==> Send mail [Press 1]\n==> Want return call [Press 2]\n==> Want to send Whatsapp msg [Press 3]\n==> Other activity [Press 4]\n\n==>")
    
    if not gatherInfo.isdigit():
         print("invalid input, Please provide the correct opition")
         exit()

    if gatherInfo == "1":
        mailid = input("Please Enter the Mail-Id : ==>")
        mail = input("Please write your mail/msg here: ==>")
        params = {
        "speak": "mail",
        "msg": mail,
        "mailid": mailid,
        }
        reqFun(params)
    elif gatherInfo == "2":
        number = int(input("Please Enter the phone number: ==>"))
        params = {
        "speak": "call",
         "num": number,
        }
        reqFun(params)
    elif gatherInfo == "3":
        msg = input("Please Enter Your Msg here: ==>")
        number = int(input("Please Enter the phone number: ==>"))

        params = {
        "speak": "whatsapp",
        "msg": msg,
        "num": number,
        }
        reqFun(params)
    elif gatherInfo == "4":
        speakCmd = input("Please Enter below commands: \n==>To find the device enter [findmydevice]\n==>To enable data enter [data]\n==>To location enter [location]\n==>To block screen enter [touch]\n==>To start alarm enter [alarm]\n==>Enter cancel to kill all the process or activity [cancel]\n\n==>")
        params = {
        "speak": speakCmd if speakCmd != "" else "Hello! Everyone",
        }
        reqFun(params)
    

if __name__ == "__main__":
    print("ok")
    mainFun()