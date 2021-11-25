import os
import smtplib
import email.message
import time
from rich import print
os.system('clear')
print(""" ███▄    █ ▓█████   ██████   ██████ ▓█████▄▓██   ██▓   
 ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▒██    ▒ ▒██▀ ██▌▒██  ██▒   
▓██  ▀█ ██▒▒███   ░ ▓██▄   ░ ▓██▄   ░██   █▌ ▒██ ██░   
▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒░▓█▄   ▌ ░ ▐██▓░   
▒██░   ▓██░░▒████▒▒██████▒▒▒██████▒▒░▒████▓  ░ ██▒▓░   
░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒   ██▒▒▒    
░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ▒  ▒ ▓██ ░▒░    
   ░   ░ ░    ░   ░  ░  ░  ░  ░  ░   ░ ░  ░ ▒ ▒ ░░     
         ░    ░  ░      ░        ░     ░    ░ ░        
                                     ░      ░ ░        """)
mn = "Olá, eu sou empresário e meu celular foi roubado junto ao meu chip hoje cedo. Queria que vocês desativassem o meu número, pois há informações importantes nele. Meu número: "
user = input("digite seu e-mail: ")
senha = input("digite sua senha: ")
alvo = input("digite o seu texto para banir número: ")
print("carregando...")
time.sleep(3)
os.system('clear')
def enviar_email():
    corpo_email = alvo
    msg = email.message.Message()
    msg['Subject'] = "Ajuda"
    msg['From'] = user
    msg['To'] = 'support@support.whatsapp.com'
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Emails enviados')
while True:
	enviar_email()