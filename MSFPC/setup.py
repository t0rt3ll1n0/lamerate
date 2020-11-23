#setup.py by t0rt3ll1n0

import os
import sys
from time import sleep
print("\033[94mMSFPC setup.py\033[0m\n")
meta = str(input("Have you got metasploit installed? Y/N --> "))
if(meta == "Y"):
	print("\nPerfect!!")
	sleep(1)
	print("\033[92m[*]\033[0m Installing pyautogui...")
	os.system('sudo pip3 install pyautogui')
	print("\033[92m[+]\033[0m Process finished")
if(meta == "y"):
	print("\nPerfect!!")
	sleep(1)
	print("\033[92m[*]\033[0m Installing pyautogui...")
	os.system('sudo pip3 install pyautogui')
	print("\033[92m[+]\033[0m Process finished")
if(meta == "N"):
	print("Ok, i will try to install it for you")
	sleep(1)
	print("""If you have a linux distro for pentest like kali or parrot\nyou can easily tipe 'sudo msfupdate' or 'sudo apt upgrade'\nbut if you have a normal distro like ubuntu or debian you need\nto add a pentest repo in /etc/apt/sources.list for be able\nto install some specified packages, after remove the pentest repo!.""")
	print("\033[92m[*]\033[0m Installing metasploit...")
	os.system('sudo apt update && sudo apt upgrade && sudo apt install metasploit-framework')
	print("\033[92m[+]\033[0m Process finished")
if(meta == "n"):
	print("Ok, i will try to install it for you")
	sleep(1)
	print("""If you have a linux distro for pentest like kali or parrot\nyou can easily tipe 'sudo msfupdate' or 'sudo apt upgrade'\nbut if you have a normal distro like ubuntu or debian you need\nto add a pentest repo in /etc/apt/sources.list for be able\nto install some specified packages, after remove the pentest repo!.""")
	print("\033[92m[*]\033[0m Installing metasploit...")
	os.system('sudo apt update && sudo apt upgrade && sudo apt install metasploit-framework')
	print("\033[92m[+]\033[0m Process finished")
else:
	exit("\033[41mSelect a valid option!! Exiting...\033[0m")

