import urllib.request as ur
import xml.etree.ElementTree as ET
url = input('Enter url: ')
data = ur.urlopen(url).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
sum = 0
for item in lst:
    sum += int(item.find('count').text)
print(sum)
