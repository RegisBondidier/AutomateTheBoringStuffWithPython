#!/usr/bin/env python3

import re

def regStrip(text, ch=None):
	if ch is None:
		stripRegex = re.compile(r'^\s*|\s*$')
		return stripRegex.sub('', text)
	charRegex = re.compile(r'^[' + ch + r']*|[' + ch + r']*$')
	return charRegex.sub('', text)


text = "     fdhdjksfhfdjkfh.    "
ch = "f d."
print(regStrip(text, ch))