#!/usr/bin/env python3

import pyperclip

# Paste text from the clipboard
text = pyperclip.paste()

# Add bullet point
textlist = text.split('\n')
for i in range(len(textlist)):
	textlist[i] = '* ' + textlist[i]
modifiedtext = '\n'.join(textlist)

# Copy the new text to the clipboard
pyperclip.copy(modifiedtext)
