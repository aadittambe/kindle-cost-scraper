import smtplib
import ssl
import pandas as pd
import os

f = open("log_price_only.txt", "r")
file = (f.read())
lines = file.split("\n")

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aadit.automation@gmail.com"  # Enter your address
receiver_email = "aadit.tambe@gmail.com"  # Enter receiver address
password = os.environ['EMAIL_KEY']

price_list = []
for line in lines:
    price = float(line.strip("$"))
    price_list.append(price)

if (price_list[-1]) < (price_list[-2]):
    msg1 = "price lower than last time!"
else:
    msg1 = ""
    print("No change in price.")

if (price_list[-1]) == min(price_list):
    msg2 = "price lowest ever!"
else:
    msg2 = ""
    print("Price is not the lowest ever.")

message = msg1 + '\n' + msg2

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
