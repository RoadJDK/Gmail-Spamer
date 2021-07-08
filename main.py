import os
from re import X
import sys

os.system("clear || cls")

print("GMAIL BOMBER")
print("------------")

dumpEmail = input("Enter your dump-email")
password = input("Enter your password")
victimEmail = input("Enter your victims-email")
messsage = input("What message should be sent?")
count = input("How many emails you want to send?")

try:
    print()
except(KeyboardInterrupt):
    print("Your interupted the process")
    sys.exit()
except:
    print("The username or password you entered is wrong")
    print("Check if your account has less secure apps activated")
    print("https://hotter.io/docs/email-accounts/secure-app-gmail/")
    