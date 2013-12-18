#!/usr/bin/env python

#######################################
#                                     #
#     Credit for the author of        #
#          Violent Python             #
#           for the idea              #
#                                     #
#    Just support sha-512 right now.  #
#                                     #
#                                     #
#   Adaptation by Alix J. Javier      #
#                                     #
#######################################

import crypt, os, sys

class Cracker(object):
	''' Cracker class for crack unix passwords '''
	def __init__(self, dictFile):
		'''Constructor of the Cracker class
		   @param dictFile = Name/path for the dictionary file
		'''
		try:
			self.dictFile = open(dictFile, 'r')
		except IOError, e:
			print "Error open the file: ", e
		except:
			print "An unknow error have ocurred: ", sys.exc_info()[1]
                self.listCracked = []
        
	def __del__(self):
		self.dictFile.close()
                
	def prepare_hash(self, line):
		user = line.split(':')[0]
		cryptPass = line.split(':')[1].strip(' ')
		self.test_pass(cryptPass, user)

	def test_pass(self, cryptPass, user='Unknown'):
                ''' The method for test the password '''
		id_hash = ""
		salt = ""
		try:
			if len(cryptPass) <= 2:
				id_hash = cryptPass
			else:
		                id_hash = cryptPass[:3]
		                salt = cryptPass.split('$')[2]
		except IndexError, e:
			print "Ups, It look kinda we got a bad file and not a copy of shadow/passwd, check your file please."
			print "Error Description: ",e
		if id_hash == "$1$" or id_hash == "$2a$" or id_hash == "$5$":
			print "This script is not soporting {MD5, Blowfish, SHA-256} hash for now."
			return
                elif id_hash == "!" or id_hash == "LK" or id_hash == "*":
			print "[+] User " + user + " has the account locked!"
			self.listCracked.append(user+":Locked!")
			return
		elif id_hash == "NP":
			print "[+] User " + user + " has not password!"
			self.listCracked.append(user+":" + "Not Password!")
			return
		elif id_hash == "!!":
			print "[+] The password of user " + user + " has experied."
			self.listCracked.append(user+":Password expired!")
                        return
                elif id_hash == "$6$":
		        print "[*] Cracking Paswword for user: " + user
			for word in self.dictFile.readlines():
				word = word.strip('\n')
				cryptWord = crypt.crypt(word, id_hash+salt+'$')
				print "Trying password  ==> " + word +  " ==> for user ==> " + user  + "\n"
				if (cryptWord == cryptPass):
					self.listCracked.append(user + ":" +  word)
					print "[+] Found password: " + word + " for user ", user
					self.dictFile.seek(0,0)
					return  
			print "[-] Password Not Found.\n"
			self.dictFile.seek(0,0)
			return
		else:
			return


# Help
def help():
	''' The help of the script'''
	print """ Usage: {0}  dictionary_file  passwords_file
	           Example: {0} easy_passwors.txt  copy_shadow.txt""".format(sys.argv[0])

# banner
def banner():
	''' print banner method '''
	print """ === Unix Password Cracker ==="""
	print """           SHA-512            """
	print """________--========--__________"""
	print "\n\n"

# main
def main():
	''' Main method '''
	if len(sys.argv) < 3:
		help()
	else:
		banner()
                dict_file = sys.argv[1]
		try:
		        pass_file = open(sys.argv[2], 'r')
                        cracker = Cracker(dict_file)
			for line in pass_file.readlines():
				cracker.prepare_hash(line)

		        print "\n\n"
			for x in cracker.listCracked:
				print "Found: " + x + "\n"
			if len(cracker.listCracked) == 0:
				print "Not password found!"
		except IOError, e:
                        print "Error openning the file: ", e
                except:
			print "An unknown error have ocurred: ", sys.exc_info()[1]


if __name__ == "__main__":
	main()

