import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "botjeff506@gmail.com"  # Enter your address
receiver_email = "abdurahmankhalif474@gmail.com"  # Enter receiver address
password = "yeet1234"
message = """\
Subject: PS5 IS OUT !!!

Website changes detected from ps5: Get it Now Now Hurry Hurry Last Chance"""


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for i in range(1):
        server.sendmail(sender_email, receiver_email, message)

