import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import sys
sys.stdout.flush()


# ----------------------------- Functions

# ---------------------------------
def findArticles(currentArticles):
    articles_list = []
    articles = currentArticles.find_all('article')
    for article in articles:
        articles_list.append(article.find('div', {"class": "preview-mini-wrap clearfix"}).find('div', {
            "class": "meta"}).find('div', {"class": "title-wrap"}).find('h3', {"class": "title"}).text)
    return articles_list


# Mail Setting =============================================================================

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "botjeff506@gmail.com"  # Enter your address
receiver_email = "abdurahmankhalif474@gmail.com"  # Enter receiver address
password = "yeet1234"
message = """\
Subject: Press AU New News !!!

Press AU New NEWS CHECK IT OUT !!!"""

print("1",  flush=True)
# ============================================================================================

url = 'https://press-start.com.au/'
req = Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
)
response = urlopen(req).read()
soup = BeautifulSoup(response, 'html.parser')
currentArticles = soup.find(
    'div', {"class": "block block-1 clearfix preview-review-bot"})
final_currentArticles = findArticles(currentArticles)


while True:

    try:
        time.sleep(60)
        response = urlopen(req).read()
        soup = BeautifulSoup(response, 'html.parser')
        currentArticles = soup.find(
            'div', {"class": "block block-1 clearfix preview-review-bot"})
        newArticle = findArticles(currentArticles)
        if newArticle == final_currentArticles:
            print("No changes to site - "+url,  flush=True)
            continue

        else:

            print("Change Detected url - "+url,  flush=True)
            context = ssl.create_default_context()
            # Send message
            alertArticle = newArticle[0].strip("'")
            message = """\
            Subject: Press AU New News !!!

            Press AU New NEWS CHECK IT OUT  With new Article """+alertArticle+"""!!!"""
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                for i in range(20):
                    server.sendmail(sender_email, receiver_email, message)

            # If article new is found we need to reset current hash
            response = urlopen(req).read()
            soup = BeautifulSoup(response, 'html.parser')
            currentArticles = soup.find(
                'div', {"class": "block block-1 clearfix preview-review-bot"})
            final_currentArticles = findArticles(currentArticles)

            continue

    except Exception as e:
        print("Server Error",  flush=True)
        print(e,  flush=True)
