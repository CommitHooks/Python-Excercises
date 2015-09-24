#! python3
# Read in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

baseFile = open(".\\files\\mad_lib_base.txt", 'w')
baseFile.write(
    '''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.'''
    )
baseFile.close()

baseFile = open("mad_lib_base.txt")
text = baseFile.read()

print('Enter an adjective: ')
adj = input()
print('enter a noun')
noun1 = input()
print('Enter a verb')
verb = input()
print('Enter a noun')
noun2 = input()

newText = text.replace('ADJECTIVE', adj).replace('NOUN', noun1, 1)
newText = newText.replace('VERB', verb).replace('NOUN', noun2)

outFile = open(".\\files\\mad_lib_out.txt", 'w')
outFile.write(newText)

baseFile.close()
outFile.close()

print('\n' + newText)
