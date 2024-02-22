import imaplib
import email
from email.header import decode_header
from datetime import datetime, timedelta
import passwordSendMail

# creds
email_address = "mdmusaif15@gmail.com"
password = passwordSendMail.passwordFun()

# Connecting to Gmail's IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login in
mail.login(email_address, password)

# Selecting the mailbox to read emails from 
mail.select("inbox")

# setting only todays date
today = (datetime.now() - timedelta(days=1)).strftime("%d-%b-%Y")

# Searching for emails
status, messages = mail.search(None, f'(SINCE "{today}")')
message_ids = messages[0].split()

for message_id in message_ids:
    # Fetching the email by ID
    status, msg_data = mail.fetch(message_id, "(RFC822)")
    raw_email = msg_data[0][1]
    
    msg = email.message_from_bytes(raw_email)

    # Getting subject and sender details
    subject, encoding = decode_header(msg["Subject"])[0]
    sender, encoding = decode_header(msg.get("From"))[0]
    
    
    # Print the email details, ignoring characters that can't be encoded
    print(f"Subject: {subject.encode('ascii', 'ignore').decode('ascii')}")
    print(f"From: {sender.encode('ascii', 'ignore').decode('ascii')}")

    # To print the email body
   """ 
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode("utf-8")
                print(f"Body: {body}")
    else:
        body = msg.get_payload(decode=True).decode("utf-8")
        print(f"Body: {body}")

    print("\n")
   """

# Logout from the server
mail.logout()
