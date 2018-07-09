#!/usr/bin/env python3

# selCp.py - walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg ). Copy these files from whatever location they are in to a new folder.
# Usage: ./selCp.py <extension_file_type> <source_root_folder> <destination_folder>


import os, sys, shutil

# Read cmd line arguments
if len(sys.argv) != 4:
	print("wrong arguments")
	exit()
ext = sys.argv[1].lower()
source = sys.argv[2]
dest = sys.argv[3]

# Create destination folder
if not os.path.exists(dest):
	os.makedirs(dest)

# Parse source directory
for foldername, subfolders, filenames in os.walk(source):
	for filename in filenames:
		srcfile = os.path.join(foldername, filename)
		file_base, file_extension = os.path.splitext(srcfile)
		if file_extension.lower() == ext:
			# copy file to dest
			print("cp " + srcfile + " " + dest)
			shutil.copy(srcfile, dest)





