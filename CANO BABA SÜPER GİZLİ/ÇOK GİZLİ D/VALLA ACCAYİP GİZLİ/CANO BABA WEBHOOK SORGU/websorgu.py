import os
try:
    from dhooks import Webhook
except:
    os.system("py -m pip install dhooks")
    from dhooks import Webhook
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
    
init()
os.system("title CANO BABA WEBHOOK SORGULAMA")
banner = (Fore.MAGENTA + """
 
  -  CANO BABA WEBHOOK SORGULAMA  -
 
 """ + Fore.LIGHTCYAN_EX)

print(banner)
hook = Webhook(input(" WEBHOOK : "))
hook.get_info()
print(f"\n SUNUCU ID    : {hook.guild_id}")
print(f" KANALIN ID  : {hook.channel_id}")
print(f" WEBHOOKUN ADI    : {hook.default_name}")
print(f" RESMI VARSA RESMI       : {hook.default_avatar_url}")
os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
exit()
