# Random Password Generator

import random
import sys

def passgen(length_of_pass):
	characters = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890@$qwertyuiopasdfghjklzxcvbnm'

	password = ''

	for c in range(0, length_of_pass):
		password += random.choice(characters)
		
	return password	

print(passgen(int(sys.argv[1])))
