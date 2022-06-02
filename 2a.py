key = input("Enter the key to generate table")
table = ""
for i in range(0, len(key)):
    if key[i] == "j":
        key[i] = "i"
    if key[i] not in table:
        table += key[i]
for x in range(ord("a"), ord("z") + 1):
    if chr(x) not in table:
        if chr(x) == "j":
            if "i" not in table:
                table += "i"
        else:
            table += chr(x)
print(table)

x = input("Enter the plaintext: ")
if len(x) % 2 != 0:
    x += "x"
n = len(x)
cipher = ""
k = 0
for i in range(0, n, 2):
    a = x[i]
    b = x[i + 1]
    if a == "j":
        a = "i"
    if b == "j":
        b = "i"
    c = (int(table.index(a) / 5), table.index(a) % 5)
    d = (int(table.index(b) / 5), table.index(b) % 5)
    if c[0] == d[0]:
        cipher += table[c[0] * 5 + (c[1] + 1) % 5]
        cipher += table[d[0] * 5 + (d[1] + 1) % 5]
    elif c[1] == d[1]:
        cipher += table[((c[0] + 1) % 5) * 5 + c[1]]
        cipher += table[((d[0] + 1) % 5) * 5 + d[1]]
    else:
        cipher += table[c[0] * 5 + d[1]]
        cipher += table[d[0] * 5 + c[1]]
print(cipher)
decipher = ""
for i in range(0, n, 2):
    a = cipher[i]
    b = cipher[i + 1]
    c = (int(table.index(a) / 5), table.index(a) % 5)
    d = (int(table.index(b) / 5), table.index(b) % 5)
    if c[0] == d[0]:
        decipher += table[c[0] * 5 + (c[1] - 1) % 5]
        decipher += table[d[0] * 5 + (d[1] - 1) % 5]
    elif c[1] == d[1]:
        decipher += table[((c[0] - 1) % 5) * 5 + c[1]]
        decipher += table[((d[0] - 1) % 5) * 5 + d[1]]
    else:
        decipher += table[c[0] * 5 + d[1]]
        decipher += table[d[0] * 5 + c[1]]
print(decipher)
