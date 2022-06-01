plainText = input("ENTER THE PLAINTEXT ").upper()
key = input("ENTER THE KEY ").upper()
temp = key
i = 0
while(len(key) < len(plainText)):
    key += temp[i]
    i = (i + 1) % len(temp)
for i, j in zip(plainText, key):
    print(chr(((ord(i) % 65) + (ord(j) % 65)) % 26 + 65))