import time
import os
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
try:
    import requests
except:
    os.system("py -m pip instamm requests")
    import requests

init()
os.system("title CANO BABA WEBHOOK SİLİCİ")
banner = (Fore.MAGENTA + """

    -  CANO BABA WEBHOOK SİLİCİ  -

""" + Fore.LIGHTCYAN_EX)
print(banner)
webhook = input(" [CANO] WEBHOOKU GİR : ")

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n [CANO] WEBHOOK SILINDI")
        os.system("pause >nul")  
    elif check.status_code == 200:
        print("\n [CANO] WEBHOOKU SİLEMEDIM")
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print("\n [CANO] BOYLE Bİ WEBHOOK YOK MK")
    os.system("pause >nul")
elif test.status_code == 200:
    print("\n [CANO] WEBHOOK BULUNDU")
    delete()
