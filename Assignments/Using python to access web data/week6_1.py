#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_318305.json (Sum ends with 3)

import json
import urllib.request as ur
url = input('Enter url: ')
data = ur.urlopen(url).read()
info = json.loads(data)
sum = 0
for item in info['comments']:
    sum += item['count']
print(sum)
