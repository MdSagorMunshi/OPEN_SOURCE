import time
import json
import sys
import os
import requests
def delete():
  os.system('rm -rf wlist.txt')
put = input("id:")
#put1=input("id2:")
token = open('token.txt').read()
cookie = open('cookie.txt').read()
coki = {"cooki":cookie}
url = requests.get('https://graph.facebook.com/%s?fields=name,id,first_name,last_name&access_token=%s'%(put,token),cookies=coki)
#for song in url["name"]:
a = "123"
b =  "1234"
 
#print(song)
events = url.json()


zeyad = events['name']
zeyad1 = events['name'] + "1234" 
zeyad2 = events['name'] + "123"
zeyad3 = events['name'] + "12"
zeyad4 = events['first_name']
zeyad5 = events['first_name'] + "1234"
zeyad6 = events['first_name'] + "123"
zeyad7 = events['first_name'] + "12"
zeyad8 = events['last_name']
zeyad9 = events['last_name'] + "1234" 
zeyad10 = events['last_name'] + "123"
zeyad11 = events['last_name'] + "12"
zeyad12 = "1987" '\n' "1988"
from rich.console import Console
console = Console()
console.print(events['name']+ "",style="bold underline green",sep="")
print(events['first_name'],events['last_name'],sep="")
print(events['name'] +b , sep='')
print(events['name'] +a ,sep='')
print(events['first_name'] +b ,sep='')
print(events['first_name'] +a ,sep='')
print(events['last_name'] +b ,sep='')
print(events['last_name'] +a ,sep='')
cps = open('wlist.txt','a')
cps.write(zeyad +   '\n' + zeyad1 +  '\n' + zeyad2 + '\n' + zeyad3 + '\n' + zeyad4 + '\n' + zeyad5 + '\n' + zeyad6 + '\n' + zeyad7 + '\n'+ zeyad12)


delete()
