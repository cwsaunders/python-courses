import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as et

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Assignment website: http://python-data.dr-chuck.net/comments_200531.xml
url = input('Enter - ')
print(f'Retrieving {url}')
xml = urllib.request.urlopen(url).read()

# XML Parsing
tree = et.fromstring(xml)
counts = tree.findall('.//count')
print(f'Comment count: {len(counts)}')

total = 0
for count in counts:
    total += int(count.text)


print ("Total: ",total)
