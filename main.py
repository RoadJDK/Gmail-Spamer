import smtplib as smt
import getpass
import time
import sys
import os

from email.message import EmailMessage

os.system("clear || cls")

print("GMAIL SPAMER")
print("------------")
print()

dumpEmail = input("Enter your dump-email : ")
password = getpass.getpass("Enter your password : ")
victimEmail = input("Enter your victims-email : ")
subject = input("Enter the subject : ")
message = input("What message should be sent? : ")
count = int(input("How many emails you want to send? : "))
delay = float(input("Do you want to add a delay? (ms) : "))

try:
    gmail_server = 'smtp.gmail.com'
    port = 587
    server = smt.SMTP(gmail_server,port)
    server.ehlo()
    if gmail_server == "smtp.gmail.com":
            server.starttls()
    server.login(dumpEmail,password)
    print("login successfull - start sending now...")
    print()

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = dumpEmail
    msg['To'] = victimEmail
    msg.set_content(message)
    i = 0

    while i < count:
        i += 1

        server.send_message(msg)
        print("A message has been sent!")
        sys.stdout.flush()
        time.sleep(delay / 1000)
    server.quit
    print()
    print("------------")
    print("Every message has been sent!")
except(KeyboardInterrupt):
    print()
    print("Your interupted the process")
    sys.exit()
except smt.SMTPAuthenticationError:
    print()
    print("The username or password you entered is wrong")
    print("Check if your account has less secure apps activated")
    print("https://hotter.io/docs/email-accounts/secure-app-gmail/")
    