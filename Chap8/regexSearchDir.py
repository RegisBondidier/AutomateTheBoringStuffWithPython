#!/usr/bin/env python3

# regexSearchDir.py - opens all . txt files in a folder and searches for any line that matches a user-supplied regular expression.
# Usage: py.exe regexSearchDir.py <dir> <regex>


import os, sys, re

if len(sys.argv) != 3:
	exit()
folder = sys.argv[1]
regex = sys.argv[2]

# Set directory
oldcwd = os.getcwd()
os.chdir(folder)

# List txt files
files = os.listdir(".")
txtfiles = []
for f in files:
	if os.path.splitext(os.path.basename(f))[1] == ".txt":
		txtfiles += [f]

# Parse with regex
research = re.compile(regex)
for f in txtfiles:
	print("file: " + f)
	fp = open(f, "r")
	lines = fp.read()
	result = research.search(lines)
	if result is not None:
		print(result.group())
	else:
		print("no pattern found")
	fp.close()

# Set current directory back
os.chdir(oldcwd)