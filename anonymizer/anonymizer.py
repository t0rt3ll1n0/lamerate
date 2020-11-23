import pyfiglet
import sys
import os
from time import sleep

class bcolors: 

	RED = '\033[31m'
	ENDC = '\033[0m'
	BLUE = '\033[94m'
	YELLOW = '\033[93m'
	BOLD = '\033[1m'
	LINK = '\033[5m'
	WARN = '\033[41m'

print(bcolors.BLUE + bcolors.YELLOW + bcolors.BOLD + bcolors.RED)
banner = pyfiglet.figlet_format("Anonimizer", font = "slant"  )
print(banner)
print(bcolors.ENDC)
print("\033[5mby t0rt3ll1n0\033[0m     v1.1")

if sys.version_info.major < 3:
	print("anonymizer supports only Python3. Rerun application in Python3 environment like sudo python3 anonymizer.py")
	exit(0)
if os.geteuid() != 0:
	exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.\n")

print("Please copy and paste the text below\n")
disclaimer = input("I WILL USE THIS SCRIPT ONLY FOR GOOD PURPOSES --> ")
if(disclaimer == 'I WILL USE THIS SCRIPT ONLY FOR GOOD PURPOSES'):
	print("Ok, you can continue.")
	sleep(2)
	os.system('clear')
	print(bcolors.RED)
	print(banner)
	print(bcolors.ENDC)
	print("\nWait, this script will prevent most common data leaks but you never be 100% anonymous\n")
	print("\n\033[94m---Tor Service Menu---\033[0m")
	print("1) Start tor service")
	print("2) Stop tor service")
	print("3) Control if tor is running")
	print("4) Restart tor service")
	print("\n\033[92m---MAC Address Spoofing Menu---\033[0m")
	print("5) Spoof a random mac") 
	print("6) Restore original mac") 
	print("\n\033[93m---Hostname Spoofing Menu---\033[0m")
	print("7) Change hostname with t0rt3ll1n0")
	print("8) Change hostname") 
	print("\n\033[31m---Ip menu---\033[0m")
	print("9) View your public ip")
	print(bcolors.RED)
	print("\n0) Exit\n")
	print(bcolors.ENDC)
	scelta = int(input("Select an option --> "))
	#tor service menu
	if(scelta == 1):
		os.system('sudo service tor start')
		print("\nTor service started")
	
	if(scelta == 2):
		os.system('sudo service tor stop')
		print("\nTor service stopped")
		
	if(scelta == 3):
		os.system('gnome-terminal -- service tor status')
		print("\nStatus of tor service")
	if(scelta == 4):
		os.system('sudo service tor start')
		print("\nTor service restarted")
	#hostname spoofing menu 
	if(scelta == 7):
		os.system('sudo hostname t0rt3ll1n0')
		print("Hostname changer with t0rt3ll1n0")
		print("Open a new terminal for look it")
	if(scelta == 8):
		new_hostname = input("Select your new hostname: ")
		os.system('sudo hostname ' + new_hostname)
		print("hostname changed to " + new_hostname)

	#exit menu
	if(scelta == 0):
		print("\nBye!!\n")
		exit(0)
	if(scelta < 0 or scelta > 9):
		print("Please select a valid option")
		exit(0)
	#mac address spoofing menu
	if(scelta == 5):
		interface = input("Enter your wireless interface (ex. wlan0): ")
		os.system('sudo ifconfig ' + interface + ' down')
		print(interface + " down now\n")
		os.system('sudo macchanger -r ' + interface)
		print("\nMAC Address changed...")
		os.system('sudo ifconfig ' + interface + ' up')
		print(interface + " up now")
	if(scelta == 6):
		interface_2 = input("Enter your wireless interface (ex. wlan0): ")
		os.system('sudo ifconfig ' + interface_2 + ' down')
		print(interface_2 + " down now\n")
		os.system('sudo macchanger -p ' + interface_2)
		print("MAC Address restored...\n")
		os.system('sudo ifconfig ' + interface_2 + ' up')
		print(interface_2 + " up now")
	if(scelta == 9): 
		os.system('curl ifconfig.me')
		print(" Is you public ip")
else:
	print("\n\033[41mYOU NEED TO ACCEPT FOR CONTINUE!!\033[0m")
	exit(0)

