import json
import os
import time 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib 
# Corpo da mensagem do email 
msg = MIMEMultipart()  
#detalhes descartaveis
print('Carregando...')
time.sleep(0.1)
print('Carregado com sucesso!')
time.sleep(0.1)
os.system("clear")
#
print('=== Enviador de gmail com python ===')
# Credenciais e assunto do email 
msg['From'] = input("Insira seu email: ")
password = input("Insira a senha do seu Gmail: ")
msg['To'] = input("Insira o destinatário: ") 
msg['Subject'] = input("Insira o título do email: ")
message = input("Insira a mensagem que você deseja enviar: ") 
msg.attach(MIMEText (message, "plain"))
#port
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls() 
server.login(msg['From'], password) 
server.sendmail(msg['From'], msg['To'], msg.as_string()) 
server.quit()
