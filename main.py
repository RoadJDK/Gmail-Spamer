import os
import smtplib as smt
import getpass
import sys

os.system("clear || cls")

print("GMAIL SPAMER")
print("------------")
print()

dumpEmail = input("Enter your dump-email : ")
password = getpass.getpass("Enter your password : ")
victimEmail = input("Enter your victims-email : ")
message = input("What message should be sent? : ")
count = input("How many emails you want to send? : ")

try:
    gmail_server = 'smtp.gmail.com'
    port = 465
    server = smt.SMTP(gmail_server,port)
    server.ehlo()
    if gmail_server == "smtp.gmail.com":
            server.starttls()
    server.login(dumpEmail,password)
    print("login successfull - start sending now...")
    print()
    i = 0
    while i < count:
        i += 1
        server.sendmail(dumpEmail,victimEmail,message)
        print("A message has been sent!")
        sys.stdout.flush()
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
    