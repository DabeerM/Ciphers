#Viginere cipher encryption in Python. Done in O(n)

if __name__ == '__main__':
    phrase = input("Enter the phrase you wanna encrypt: ").upper()
    key = input("Enter the word you wanna use as the key: ")
    encrypted_phrase = ''

    for i in range(len(phrase)):
        cur_letter = ord(phrase[i])-64 #Current character we're on in the phrase
        key_letter = ord(key[i%(len(key))])-64 #The current character in the key
        encrypted_phrase += chr((cur_letter + key_letter)%26 + 63)

    print('The encrypted phrase is: ' + encrypted_phrase)
