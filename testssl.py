from lxml import html
import requests




r=requests.get('https://github.com', verify=True)
#r.headers
print r.headers
#r.request.headers
print r.request.headers



def internet_on():
    try:
        response=requests.get('https://github.com', verify=True)
        return True
    except urllib2.URLError as err: pass
    return False
