#!/usr/bin/env python
########################################
#                                      #
#    ZipFile Password Cracker v. 1.0   #
#     All Credit to the Author of      #
#         Violent Python Book          #
#                                      #
#      Adapted by A. J. Javier         # 
#                                      #
########################################

import zipfile
import argparse

def extract_file(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print "[+] Found password " + password + "\n"
		return True
	except:
		return False

def main():
	parser = argparse.ArgumentParser(description="Crack the password of a protected zipfile.")
	parser.add_argument("-d","--dictionary", dest="dname", help="specify dictionary file")
	parser.add_argument("-f", "--file", dest="zname", help="specify zip file")
	options = parser.parse_args()
        zname = options.zname
	dname = options.dname
	if (zname == None) | (dname == None):
		parser.print_help()
		exit(0)
	try:
		if zipfile.is_zipfile(zname):
			zFile = zipfile.ZipFile(zname)
		else:
			print "The file %s is not a valid zip file." % zname
		passFile = open(dname, "r")
	except IOError, e:
		print "We got an error Houston: ",e
		exit(0)
	except:
		print "Something is wrong, exiting."
		exit(0)
		
	if not zFile:
		exit(0)
	for line in passFile.readlines():
		password = line.strip("\n")
		print "Trying with password: ", password
		isCracked = extract_file(zFile, password)
		if isCracked:
			exit(0)

if __name__ == "__main__":
	main()
