import json
import urllib.request,urllib.parse,urllib.error

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    # URL OPEN:
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()

    # Exception handling for loads
    try:
        js = json.loads(data)
    except:
        js = None
    
    # Test for Google API status 'OK' && if prior loads failed
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== FAILURE TO RETRIEVE ====')
        print(data)
        continue
    
    # dumping
    print(json.dumps(js,indent=4))
