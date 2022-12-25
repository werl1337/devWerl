# KANEKI1337
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """ 

 -  CANO BABA ID SORGULAMA PANELI  -


""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [CANO] SORGULANCAK ID YAPIM AŞAMASINDADIR SADECE İLK KISMI GÖSTERİLİR : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [CANO] MALIN TOKENI : {encodedStr}')
os.system('pause >nul') 
