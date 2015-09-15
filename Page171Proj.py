#! python 3

import re

def isLongerThanEight(password):
    if len(password) >= 8:
        return True

def hasUpperCaseLetter(password):   
    pswdRegex = re.compile(r'[A-Z]+')
    if pswdRegex.search(password).group():
        return True

def hasLowerCaseLetter(password):   
    pswdRegex = re.compile(r'[a-z]+')
    if pswdRegex.search(password).group():
        return True

def hasDigit(password):  
    pswdRegex = re.compile(r'\d+')
    if pswdRegex.search(password).group():
        return True


print('Please enter your password:')
pw = input()

while not (isLongerThanEight(pw) and hasUpperCaseLetter(pw) and hasLowerCaseLetter(pw) and hasDigit(pw)):
    print('Invalid password. Please enter again: ')
    pw = input()

print('Password entered is valid. Thank you!')

    
    
    
