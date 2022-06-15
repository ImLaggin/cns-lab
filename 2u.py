def mat_fill(key):      # function to make the key matrix
    key = key.upper()
    mat = [[0 for i in range(5)] for j in range(5)]     # initializing matrix to 0
    exists = []
    r = 0
    c = 0

    for letter in key:      # checks if letter already exists
        if letter == ' ':   # avoids spaces in matrix
            continue
        elif letter not in exists:  
            mat[r][c] = letter
            exists.append(letter)
        else:
            continue
        if (c == 4):
            c = 0
            r += 1
        else:
            c += 1

    for letter in range(65, 91):    # appending the remaining letters into the exists
        if letter == 74:    # ignoring j as i/j are in the same block
            continue
        if (chr(letter) not in exists):
            exists.append(chr(letter))

    k = 0
    for i in range(5):      # Transfering the contents of exists into a matrix
        for j in range(5):
            mat[i][j] = exists[k]
            k += 1
    
    print(mat)
    return mat

def split(pt):      # function to pair letters and remove common letter pairs
    pos = 0
    while (pos < len(pt)):
        l1 = pt[pos]
        if pos == len(pt)-1:    # pairing the last letter with X if odd number of letters exist
            pt = pt + 'X'
            pos += 2
            continue
        l2 = pt[pos+1]
        if l1 == l2:    # splitting common letter pairs 
            pt = pt[:pos+1] + "X" + pt[pos+1:]
        pos += 2
    return pt

def indexpos(letter, mat):  # function to return the current index positon of the letters 
    for i in range(5):
        try:
            index = mat[i].index(letter)
            return (i, index)
        except:
            continue

def playfair(key, pt, encrypt=True):    # function to cypher and decypher the message
    inc = 1
    if encrypt == False:
        inc = -1
    mat = mat_fill(key)
    pt = pt.upper()
    pt = pt.replace(' ', '')
    pt = split(pt)
    ct = ''

    for (l1, l2) in zip(pt[0::2], pt[1::2]):
        row1, col1 = indexpos(l1, mat)
        row2, col2 = indexpos(l2, mat)

        if row1 == row2:    # case 1: same row
            ct += mat[row1][(col1+inc) % 5] + mat[row2][(col2+inc) % 5]
        elif col1 == col2:  # case 2: same column
            ct += mat[(row1+inc) % 5][col1] + mat[(row2+inc) % 5][col2]
        else:   # case 3: different row and column
            ct += mat[row1][col2] + mat[row2][col1]

    return ct

pt = input("Enter the Message: ")
key = input("Enter Key:")
ct = playfair(key, pt)
print(ct)
npt = playfair(key, ct, False)
print(npt)
