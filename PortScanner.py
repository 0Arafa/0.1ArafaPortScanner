#!/usr/bin/python

from socket import * #We used a socket module for Port\s scanning
from os import system #We used a os module for clear The Terminal

system("clear") #Clear The Terminal
#About author
print("\n","\t"*5,"By : Abd Almoen Arafa"),print("\t"*5,"Age : 15\n"),print("\t"*3,"#"*50,"\n")
host=input("[*] Enter The Host: ") #The Host
def PortScanner(port): #We made a function called PortScanner
		    #IPv4   #TCP packets
	sock=socket(AF_INET,SOCK_STREAM)
	if sock.connect_ex((host,port)): #If there is a problem while connecting to The Port print Port is closed
		print("[!!] Port %s is closed"%(port))
	else: #If there is no problem while connecting to The Port print Port is open
		print("[+] Port %s is open"%(port))
	sock.close() #When we finish from the scanning, the connection will close
ask=input("[*] Do you want to scan a specific Port or a group of Ports?(spe,ran): ") #Asking for a specific Port scanning or a range Port scanning
if ask.lower() == "spe" or ask.lower() == "specific": #If ask is spe or specific, ask for Port and scan it
	port=int(input("[*] Enter The Port: ")) #The Port
	PortScanner(port)
else: #If ask is not spe or specific, ask for num1 and num2 and start scanning from the first Port from the lowest number to the last Port from highest number
	num1=int(input("[*] Enter the lowest number: ")) #The lowest number
	num2=int(input("[*] Enter the highest number: ")) #The highest number
	for port in range(num1,num2+1):
		PortScanner(port)
print("\n","\t"*3,"#"*50,"\n")
