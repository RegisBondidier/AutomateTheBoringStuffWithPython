#!/usr/bin/env python3

# findBigFile.py
# Usage: ./findBigFile.py <min_size_in_MB> <folder>

import os, sys

# Read cmd line arguments
if len(sys.argv) != 3:
	print("wrong arguments")
	exit()
min_size = int(sys.argv[1]) * 1000000 # in bytes
folder = sys.argv[2]

# Parse source directory
for foldername, subfolders, filenames in os.walk(folder):
	for filename in filenames:
		if os.path.getsize(os.path.join(foldername, filename)) > min_size:
			print(os.path.join(foldername, filename))





