import smtplib
import sys

try: 
    import passwordSendMail
    
except ModuleNotFoundError:
    sys.path.append("D:\\Vscode-All scripts\\Python")

#email = input("sender email")
#receiver_email = input("Receiver email")
#receiver_email ="mdmusaif.mm@gmail.com"

def sendMail(receiver_email,message,passwd):
    if "@gmail.com" not in receiver_email:
        receiver_email += "@gmail.com"
    
    email = "mdmusaif15@gmail.com"
    subject = "Programatic mail from msi"
    text = f"Subject: {subject}\n\n{message}"
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    
    server.login(email,passwd)
    
    server.sendmail(email,receiver_email,text)
    
    print("\n"+20*"#")
    print(f"Email has been sent successfully: {receiver_email}")
    print("\n"+20*"#")
    
if __name__ == "__main__":
    print(20*"#"+" Starting "+20*"#")
    password = passwordSendMail.passwordFun()
    receiver_email = input("To: ").lower()
    message = input("Write you text here: ").title()
    sendMail(receiver_email,message,password)
    