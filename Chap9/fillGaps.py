#!/usr/bin/env python3

# fillGaps.py - 
# Usage: ./fillGaps.py <prefix> <folder>


import os, sys, shutil, re

# Read cmd line arguments
if len(sys.argv) != 3:
	print("wrong arguments")
	exit()
prefix = sys.argv[1]
folder = sys.argv[2]

# Create regex
prefixRE = re.compile(r'^' + prefix +  # begining of the filename start with prefix
	r"""(\d{3}) # 3 digits
	\.		# dot
	(.*)$	# extension
	""", re.VERBOSE)

# Parse folder
filenames = os.listdir(folder)
os.chdir(folder)
filenames.sort()
index = 1
for filename in filenames:
	mo = prefixRE.search(filename)
	if mo is None:
		continue
	if int(mo.group(1)) != index:
		# missing index : renaming file
		shutil.move(filename, prefix + '{:03d}'.format(index) + "." + mo.group(2))
	index += 1
	


