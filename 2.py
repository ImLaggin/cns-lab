import string

inputString = input("Enter the input string: ").upper().replace(
    'J', 'I').replace(' ', '')
key = input("Enter the key: ").upper().replace('J', 'I').replace(' ', '')

alphabets = string.ascii_uppercase
visited = {i: 0 for i in alphabets}
rowIndex = {}
columnIndex = {}
keyMatrix = [['a', 'a', 'a', 'a', 'a'] for i in range(5)]


def constructKeyMatrix():
    i, j = 0, 0
    for e in key:
        if(visited[e] == 1):
            continue
        if(j < 4):
            keyMatrix[i][j] = e
            rowIndex[e] = i
            columnIndex[e] = j
            j += 1
        else:
            keyMatrix[i][j] = e
            rowIndex[e] = i
            columnIndex[e] = j
            j = 0
            i += 1
        visited[e] = 1

    for e in alphabets:
        if(e == 'J'):
            continue
        if(visited[e] == 1):
            continue
        if(j < 4):
            keyMatrix[i][j] = e
            rowIndex[e] = i
            columnIndex[e] = j
            j += 1
        else:
            keyMatrix[i][j] = e
            rowIndex[e] = i
            columnIndex[e] = j
            j = 0
            i += 1
        visited[e] = 1


constructKeyMatrix()
for k in keyMatrix:
    print(k)


def playFair(c1, c2, encrypt=True):
    if encrypt:
        if(rowIndex[c1] == rowIndex[c2]):
            t1, t2 = columnIndex[c1], columnIndex[c2]
            return keyMatrix[rowIndex[c1]][(t1+1) % 5]+keyMatrix[rowIndex[c2]][(t2+1) % 5]
        elif(columnIndex[c1] == columnIndex[c2]):
            t1, t2 = rowIndex[c1], rowIndex[c2]
            return keyMatrix[(t1+1) % 5][columnIndex[c1]]+keyMatrix[(t2+1) % 5][columnIndex[c2]]
        else:
            return keyMatrix[rowIndex[c1]][columnIndex[c2]]+keyMatrix[rowIndex[c2]][columnIndex[c1]]
    else:
        if(rowIndex[c1] == rowIndex[c2]):
            t1, t2 = columnIndex[c1], columnIndex[c2]
            return keyMatrix[rowIndex[c1]][(t1-1) % 5]+keyMatrix[rowIndex[c2]][(t2-1) % 5]
        elif(columnIndex[c1] == columnIndex[c2]):
            t1, t2 = rowIndex[c1], rowIndex[c2]
            return keyMatrix[(t1-1) % 5][columnIndex[c1]]+keyMatrix[(t2-1) % 5][columnIndex[c2]]
        else:
            return keyMatrix[rowIndex[c1]][columnIndex[c2]]+keyMatrix[rowIndex[c2]][columnIndex[c1]]


def driver(choice=1):
    resultString = ""
    i = 0

    while(i < len(inputString)):
        if choice == 1:
            if(i == len(inputString)-1 or inputString[i] == inputString[i+1]):
                resultString += playFair(inputString[i], 'X')
            else:
                resultString += playFair(inputString[i],
                                         inputString[i+1])
                i += 1
            i += 1
        elif choice == 2:
            if(i == len(inputString)-1 or inputString[i] == inputString[i+1]):
                resultString += playFair(inputString[i], 'X', encrypt=False)
            else:
                resultString += playFair(inputString[i],
                                         inputString[i+1], encrypt=False)
                i += 1
            i += 1

    print("Resultant string is:", resultString)


choice = int(input("1. Encrypt\n2. Decrypt\n"))
driver(choice)
