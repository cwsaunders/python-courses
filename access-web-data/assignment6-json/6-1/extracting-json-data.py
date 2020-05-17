# Extracting Data from JSON Assignment
# Import statements
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Assignment website: http://python-data.dr-chuck.net/comments_42.json
url = input('Enter - ')
print(f'Retrieving {url}')
uh = urllib.request.urlopen(url).read()
data = uh.decode('utf-8')
print(f'Retrieved {len(data)} characters')

# Sorting JSON data
js = json.loads(data)
total = 0
count=0
for i in range(len(js['comments'])):
    total += int(js['comments'][i]['count'])
for i in range(len(js['comments'])):
    count +=1
print('Count: ',count)
print('Total: ',total)
