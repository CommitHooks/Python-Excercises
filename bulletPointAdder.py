#! python3
# bulletPointAdder.py - Adds * to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
print(text)
pyperclip.copy(text)

'''
#Original:
Lists of animals
Lists of aquarium life
Lists of insects
Lists of mammals
Lists of cultivars

#After:
* Lists of animals
* Lists of aquarium life
* Lists of insects
* Lists of mammals
* Lists of cultivars

'''
