plainText = input("ENTER THE PLAINTEXT ").upper()
key = input("ENTER THE KEY ").upper()
cipherText = []
decryptedText = []

temp = key
i = 0
while(len(key) < len(plainText)):
    key += temp[i]
    i = (i + 1) % len(temp)
    
for i, j in zip(plainText, key):
    cipherText.append(chr(((ord(i) % 65) + (ord(j) % 65)) % 26 + 65))
    
cipherText = str("".join(cipherText))
print(cipherText)

for i, j in zip(cipherText, key):
    decryptedText.append(chr(((ord(i) % 65) - (ord(j) % 65)) % 26 + 65))
    
decryptedText = str("".join(decryptedText))
print(decryptedText)
