#! python3
# Regex version of strip()

import re

def strip_white_space(s):
    """
    When passed in only one string, remove the whitespaces from the
    beginning and end of the string
    """
    white_space_regex_1 = re.compile(r'^\s*')
    white_space_regex_2 = re.compile(r'\s*$')
    temp_str = white_space_regex_1.sub('', s)
    return white_space_regex_2.sub('', temp_str)

# When two arguments are passed in, remove the charactors specified in the second arguments
def strip_chars(s, chars):
    chars_regex = re.compile(chars)
    return chars_regex.sub('', s)

print('Enter the original string:')
orig_str = input()
print('Enter the characters to be substitute: ')
sub_chars = input()

if not sub_chars:
    print(strip_white_space(orig_str))
else:
    print(strip_chars(orig_str, sub_chars))
