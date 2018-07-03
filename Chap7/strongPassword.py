#!/usr/bin/env python3

import re

def isStrongPassword(pw):
	# test length
	if len(pw) < 8:
		print("Password not long enough")
		return False
	# test presence of uppercase characters
	upperRegex = re.compile(r'[A-Z]')
	if upperRegex.search(pw) is None:
		print("No uppercase letters in password")
		return False
	# test presence of lowercase characters
	lowerRegex = re.compile(r'[a-z]')
	if lowerRegex.search(pw) is None:
		print("No lowercase letters in password")
		return False
	# test presence of at least one digit	
	digitRegex = re.compile(r'\d')
	if digitRegex.search(pw) is None:
		print("No digit in password")
		return False
	return True

print('Enter password:')
text = input()
if isStrongPassword(text):
	print("This is a strong password")
else:
	print("Please change password")