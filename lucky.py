#!python3
# luck.py - Open several Google search results
# To run this program, type "python lucky.py [word1] [word2]"
"""
This is what your program does:
 - Gets search keywords from the command line arguments.
 - Retrieves the search results page.
 - Opens a browser tab for each result.
"""

import requests, sys, webbrowser, bs4

print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
