#!/usr/bin/env python3

import pyperclip
import re

# Get text from clipboard
text = str(pyperclip.paste())

# Find phone numbers and email addresses
phoneRegex = re.compile(r'''
	(\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    ''', re.VERBOSE)

emailRegex = re.compile(r'''
	[a-zA-Z0-9._%+-]+		# username
	@						# @
	[a-zA-Z0-9._%+-]+		# domain
	\.						# .
	[a-zA-Z]+				# domain extension
	''', re.VERBOSE)

result = ''
for p in phoneRegex.findall(text):
	result += ''.join(list(p)) + '\n'
for e in emailRegex.findall(text):
	result += e + '\n'

# Paste result to clipboar
pyperclip.copy(result)


