import json
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib 

msg = MIMEMultipart()  

print('=== Gmail sender ===')

msg['From'] = input("Your email: ")
password = input("Your password: ")
msg['To'] = input("Receiver: ") 
msg['Subject'] = input("Email title: ")
message = input("Message: ") 
msg.attach(MIMEText (message, "plain"))

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls() 
server.login(msg['From'], password) 
server.sendmail(msg['From'], msg['To'], msg.as_string()) 
server.quit()
