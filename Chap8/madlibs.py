#!/usr/bin/env python3

# Ask user for words
print("Enter an adjective:")
adj = str(input())
print("Enter a noun:")
noun1 = str(input())
print("Enter a verb:")
verb = str(input())
print("Enter another noun:")
noun2 = str(input())

# Read the text files
template = open("mad_template.txt", 'r')
text = template.read()
template.close()

# find and replace string
text = text.replace("ADJECTIVE", adj).replace("NOUN", noun1, 1).replace("VERB", verb).replace("NOUN", noun2, 1)

print(text)

# write the new file
result = open("mad.txt", 'w')
result.write(text)
result.write('\n')
result.close()