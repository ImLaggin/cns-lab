def encryptRailFence(text, key):
	rail = [[' ' for i in range(len(text))] for j in range(key)]
	
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down

		rail[row][col] = text[i]
		col += 1

		if dir_down:
			row += 1
		else:
			row -= 1

	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != ' ':
				result.append(rail[i][j])
				
	for i in range(key):
	    for j in range(len(text)):
	        print(rail[i][j], end=" ")
	    print("\n")
			
	return("" . join(result))
	
def decryptRailFence(cipher, key):
	rail = [['\n' for i in range(len(cipher))] for j in range(key)]
	
	dir_down = None
	row, col = 0, 0
	
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		

		rail[row][col] = '*'
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
			
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		
		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False
			
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
			
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

print(encryptRailFence("defendtheeastwall", 3))
print(decryptRailFence("dnetleedheswlftaa", 3))
