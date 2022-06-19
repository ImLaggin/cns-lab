plainText = input("Enter the plaintext: ")
key = int(input("Enter the key: "))
if key > 26:
    key %= 26

cipherText = ''
for char in plainText:
    if char.isdigit():
        char = chr((ord(char)%48+key)%10+48)
        cipherText += char
    elif char.isalpha():
        if char.isupper():
            char = chr((ord(char)%65+key)%26+65)
            cipherText += char
        else:
            char = chr((ord(char)%97+key)%26+97)
            cipherText += char
    else:
        cipherText += char
        continue
    
print("Encrypted text is:" ,cipherText)

decryptedText = ''
for char in cipherText:
    if char.isdigit():
        char = chr((ord(char)%48-key)%10+48)
        decryptedText += char
    elif char.isalpha():
        if char.isupper():
            char = chr((ord(char)%65-key)%26+65)
            decryptedText += char
        else:
            char = chr((ord(char)%97-key)%26+97)
            decryptedText += char
    else:
        decryptedText += char
        continue
    
print("Decrypted text is:" ,decryptedText)
