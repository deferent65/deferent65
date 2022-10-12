import requests , datetime
import time , os , random
#----------------------------[الالوان]----------------------#
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
#--------------------------------------------------------------#

logo = '''____        __                     _
|  _ \  ___ / _| ___ _ __ ___ _ __ | |_
| | | |/ _ \ |_ / _ \ '__/ _ \ '_ \| __|
| |_| |  __/  _|  __/ | |  __/ | | | |_
|____/ \___|_|  \___|_|  \___|_| |_|\__|
'''
print (B + logo)
ID = input (Z+"Entar id tele : ")
Token = input ("Entar token bot : ")
time.sleep(3)
os.system('clear')
hit=0
Er=0
while True:
	
	log = ("\n=====================================\n")
	
	red = 'pppoooiiiuuuyyytttrrreeewwwqqqlllkkkjjjhhhgggfffdddsssaaammmnnnbbbvvvcccxxxzzz'    
	user = str (''.join(random.choice(red)for z in range (int(5))))
	url = f"https://info-telegram-stef.hlwy.repl.co/index.php?user={user}"
	ue = requests.get(url).text
	if ue=='Not Available':
		Er+= 1
		oo=f"\nAvailable: {hit}"
		pp=f"\nNot Available : {Er}"
		ii= f"\nuser : {user}\n"
		
		print (X+log , F+oo , Z+pp, Y+ii , X+log)
		time.sleep (2)
		os.system('clear')
	if ue=='Available or Band':
		hit+= 1
		oo=f"\nAvailable: {hit}"
		pp=f"\nNot Available : {Er}"
		ii=f"\nuser : {user}\n"
		print (X+log , F+oo , Z+pp, Y+ii , X+log)
		deferent = f"""Don User
hit : {hit}
User : @{user}
bv @deferent_404"""
		tele = (f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={deferent}')
		req = requests.post(tele)
		time.sleep (2)
		os.system('clear')
