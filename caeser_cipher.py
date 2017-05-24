#making a ceaser cipher in python 

def getStr():
	return input("Enter a string: ").lower() 
 
def getKey(): #gets the key to encrypt
	return int(input("Enter the key you wish to encrypt the key in: "))

def  decrypt(myStr): #brute forces all combos into a textfile
	f=open("results.txt","w")
	for i in range(26):
		f.write(manipulateStr(myStr,i))
		f.write('\n')
	f.close()

def manipulateStr(myStr, myKey): #encrypts a string using caeser cipher
	newStr = ""
	asciiBase = 96 #As 'a' is 97 in ASCII/UNICODE
	alphaTot  = 26 #26 letters in the alphabet
	for i in range(len(myStr)):
		if (myStr[i]!=' '):
			newStr+=chr(((ord(myStr[i])+myKey-asciiBase)%alphaTot)+asciiBase) #you add/minus 96 because, 'a' is 97 in ASCII/UNICODE
		else:
			newStr+=' ' 
	return newStr

def optionMenu(): #makes it a little more user friendly
	option = 0
	while (option!=1 and option!=2):
		print("Would you like to: 1. Encrypt a message")
		print("                             2. Decrypt a message")
		print("                             3. Exit the program")
		option = int(input())
	return option
	
if __name__ == "__main__":
	option = optionMenu()
	while (option!=3):
		if (option==1): #encrypting a string
			print("The encrypted string is: " + manipulateStr(getStr(),getKey()))
		elif (option==2): #decrypting a string
			decrypt(getstr()) 

