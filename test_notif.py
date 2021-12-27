import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

sender_email = "aadit.automation@gmail.com"
receiver_email = "your@gmail.com"
password = os.environ['EMAIL_KEY']

message = MIMEMultipart("alternative")
message["Subject"] = "Amazon Kindle price update"
message["From"] = "aadit.automation@gmail.com"
message["To"] = "aadit.tambe@gmail.com"
message["Cc"] = "aadit.automation@gmail.com"


# Create the plain-text and HTML version of your message
text = """\
Hey there,
There's an update on the price of an Amazon Kindle that you might be interested in!
This message was automated with Python and GitHub Actions.
"""
html = """\
<html>
  <body>
    <p>Hey there,<br>
       There's an update on the price of an Amazon Kindle that you might be interested in!<br>
       This message was automated with Python and GitHub Actions.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
