import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = "mdmusaif15@gmail.com"
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to the SMTP server (if authentication is required)
        server.login(to_email, smtp_password)

        # Send the email
        server.sendmail(to_email, msg.as_string())

if __name__ == "__main__":
    # Set your email details
    subject = "Test Email"
    body = "This is a test email sent from Python."
    to_email = "mdmusaif15@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Update the port accordingly
    #smtp_username = "python"
    smtp_password = "wobo fhhe garn jmms"

    # Send the email
    send_email(subject, body, to_email, smtp_server, smtp_port, smtp_password)

