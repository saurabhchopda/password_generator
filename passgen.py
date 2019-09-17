import random

characters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890@$'

password = ''

print('Enter the length of the password :')

length_of_pass = int(input())


for c in range(0, length_of_pass):
    password += random.choice(characters)

print(password)
