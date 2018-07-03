#!/usr/bin/env python3

import re

numberRegex = re.compile(r'^\d{1,3}(,\d{3})*$')

text = "12,445,343"
for r in numberRegex.findall(text):
	print(r)