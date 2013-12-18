#!/usr/bin/env python

import nmap
import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		screenLock.acquire()
		print "[+] %d/tcp open" % tgtPort
		print "[+] " + str(results)
	except:
		screenLock.acquire()
		print "[-] %d/tcp closed" % tgtPort
	finally:
		screenLock.release()
		connSkt.close()

#not for use now
def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[+] Cannont resolve '%s': Unknown host" % tgtHost
		return
	print "\n[+] Scan Reults for: " + tgtIP
	nmScan.scan(tgtHost, tgtPort)
	state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print "[*] " + tgtHost + " tcp/" + tgtPort + " " + state
        

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host" % tgtHost
		return
	print "\n[+] Scan Results for: " + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def banner():
	print """ 
	          ____===== SIMPLE PYTHON PORTS SCANNER =====____
	          _______________________________________________
	      """

def main():
	parser = argparse.ArgumentParser(description="A simple python ports' scanner")
	parser.add_argument("-t", "--target", dest="host", help="specify target host")
	parser.add_argument("-p", "--port", dest="port", help="specify taget port[s] separated by comman")
#	parser.add_argument("-n", "--nmap", dest="nmap", help="specify this option for a nmap scan")
	args = parser.parse_args()
	tgtHost = args.host
	tgtPorts = str(args.port).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		parser.print_help()
		exit(0)
	banner()
	portScan(tgtHost, tgtPorts)
if __name__ == "__main__":
	main()
