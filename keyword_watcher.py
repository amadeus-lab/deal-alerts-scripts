#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import codecs
from html.parser import HTMLParser
import smtplib
from email.mime.text import MIMEText
import time
import sys

if len(sys.argv) != 4:
    print("Wrong arguments! Usage: python keyword_watcher.py <URL> <PASSWORD> <EMAIL_LIST_PATH>")
    exit(0)

URL = sys.argv[1]
PASSWORD = sys.argv[2]
EMAIL_LIST = sys.argv[3]

print('Checking Status...')
req = urllib.request.Request(URL)
with urllib.request.urlopen(req) as response:
   html = response.read()

html = str(html, 'utf-8')
if '逆天价：'  in html:
    sender = 'small@oppai.faith'
    email_file = open(EMAIL_LIST, "r")
    recipient = email_file.read().split(',')
    server = smtplib.SMTP('smtp.zoho.com', 587)
    server.starttls()

    # Next, log in to the sercxver
    server.login('small@oppai.faith', PASSWORD)

    # Send the mail
    msg = MIMEText(URL)
    msg['Subject'] = "ACTION NEEDED: 新的逆天价出现了"
    msg['From'] = sender
    msg['To'] = ", ".join(recipient)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
    print('YAY')
