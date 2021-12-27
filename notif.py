import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

sender_email = "aadit.automation@gmail.com"
receiver_email = os.environ['EMAIL_ADDRESS']
password = os.environ['EMAIL_KEY']

message = MIMEMultipart("alternative")
message["Subject"] = "Amazon Kindle price update"
message["From"] = "aadit.automation@gmail.com"
message["To"] = os.environ['EMAIL_ADDRESS']
message["Cc"] = "aadit.automation@gmail.com"

f = open("log_price_only.txt", "r")
file = (f.read())
lines = file.split("\n")

price_list = []
for line in lines:
    price = float(line.strip("$"))
    price_list.append(price)

if (price_list[-1]) < (price_list[-2]):
    text = """\
    Hey there,

    There's an update on the price of an Amazon Kindle: The price has dropped!

    This message was automated with Python and GitHub Actions.
    """
    html = """\
    <html>
      <body>
        <p>Hey there,<br>
          There's an update on the price of an Amazon Kindle: The price has dropped!<br>
          This message was automated with Python and GitHub Actions.
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

else:
    print("No drop in price.")
