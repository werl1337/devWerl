from colorama import Fore, init
import requests
import json
import os

init()
os.system("title CANOBABA1000 IP SORGU")
os.system("cls")
banner = (Fore.MAGENTA + """
 
  -  CANOBABA IP ADRES SORGU  -
 
""" + Fore.LIGHTCYAN_EX)

print(banner); print(" [CANO] discord.gg/zcheck \n")
ip = input(" [CANO] IP ADDRESI GIR PICIN OGLU : "); ip.replace(" ", "")
r = requests.get(f"http://ip-api.com/json/{ip}")
r2 = requests.get(f"https://ipinfo.io/{ip}")
values = json.loads(r.text)
data = r2.json()
city = data["city"]
location = data["loc"].split(",")
latitude = location[0]
longitude = location[1]

print("\n [1] : " + values["country"] + f" [{values['countryCode']}]")
print(" [2] : " + values["regionName"] + f" [{values['region']}]")
print(" [3] : " + city)
print(" [4] : " + values["timezone"])
print(" [5] : " + values["isp"])
print(" [6] : " + latitude, "|", longitude)
os.system("pause >nul") 
