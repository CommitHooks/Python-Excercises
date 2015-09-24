#! python3
# This program opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.

import os, re

piRegex = re.compile(r'\[PiDataRefreshJob\] - Completed')

for file in os.listdir('.\\files\\logs'):
    if file.find('.log'):
        print(file + '\n')
        logFile = open('.\\files\\logs\\' + file)
        lines = logFile.readlines()
        logFile.close()

        for text in lines:
            if piRegex.search(text):
                print('Line ' + str(lines.index(text)+1) + '\n')
