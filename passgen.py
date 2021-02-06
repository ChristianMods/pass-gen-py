from string import printable
import random

digit = printable.strip()
passw  = []
length = input("Password length ")
def passwords(length):
	if length == '':
		print("no password is of 0 words")
		exit()
	elif length.replace(' ','').isalpha() == True:
		print("type a number")
		exit()
	else:
		for _ in range(int(length)):
			passw.append(random.choice(digit))
	word = ''.join(passw)
	print(word)
passwords(length)