Unix Password Cracker or something like that
============================================

The original script from the book only "crack"
passwords in the old unix format, when the passwords
was in the passwd file.

So i adapted the script to be able to "crack" the actual
format(in fact, just for Linux, not BSD or others unixes), 
which is sha-512 using a salt and all that stuff.

I changed other things (I guess). For help, see the help!
Notice that it needs a copy of the /etc/shadow file not
the /etc/passwd file.

I quoted the word "crack" because this not exactly "cracking",
but simple attack dicctionary.
