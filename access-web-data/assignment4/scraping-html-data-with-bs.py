from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve/sort data
# Actual data for program: http://python-data.dr-chuck.net/comments_353539.html
# Data to test against: http://python-data.dr-chuck.net/comments_42.html
tags = soup('span')
total = 0
for tag in tags:
    total += int(tag.text)
print(total)
