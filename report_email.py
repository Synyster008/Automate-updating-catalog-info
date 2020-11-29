import os
from reports import generate_report
from emails import generate_email, send_email
from datetime import datetime, date, time


files = os.listdir("supplier-data/descriptions/")
obj = ''

for file in files:
    fl = open("supplier-data/descriptions/" + file, 'r')
    keys = ['name:', 'weight:']
    i=0
    for f in fl.readlines():
        if i<2:
            obj += keys[i]+ '' + f.strip() + '<br/>'
        i +=1
    obj += '<br/>'+'<br/>'
date = date.today()
date= date.strftime("%B %d, %Y")
title= 'Processed Update on {}'.format(date)

attachment = '/tmp/processed.pdf'
generate_report(attachment, title, obj)
user = os.getenv('USER')
sender = 'automation@example.com'
receiver = '{}@example.com'.format(user)
subject = 'Upload Completed - Online Fruit Store'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
msg = generate_email(sender, receiver, subject, body, attachment)
send_email(msg)