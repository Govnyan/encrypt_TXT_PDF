###---Encrypt TXT file---###
import pyAesCrypt

password = input("Enter password: ")

#encrypt
#pyAesCrypt.encryptFile("serv.txt", "serv.txt.aes", password)

#decrypt
pyAesCrypt.decryptFile("serv.txt.aes", "serv.txt", password)