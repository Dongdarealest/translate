import requests
import os 
OKGREEN = '\033[92m'
ENDC = '\033[0m'
os.system("clear")
def ggdich():
 vanban = str(input("Văn bản cần dịch :"))
 if len(vanban) == 0:
   exit(0)
 else:
  dich = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=vi&dt=t&q="+ vanban).json()
  dich2 = dich[0][0][0]
  print("Văn bản trên có nghĩa là :"+ OKGREEN + dich2 + ENDC + "\n")
while True: 
 ggdich()
