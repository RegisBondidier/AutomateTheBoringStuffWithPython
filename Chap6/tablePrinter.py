#!/usr/bin/env python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'], 
			 ['dogs', 'cats', 'moose', 'goose']]

def printTable(t):
	# find max width for each column
	width = [0] * len(t)
	for x in range(len(t)):
		for y in range(len(t[x])):
			if width[x] < len(t[x][y]) :
				width[x] = len(t[x][y])

	# Store created lines in display
	display = [''] * len(t[0])
	for x in range(len(t)):
		for y in range(len(t[x])):
			display[y] = display[y] + ' ' + t[x][y].rjust(width[x])
	
	# print the table
	for i in range(len(display)):
		print(display[i])

printTable(tableData)
