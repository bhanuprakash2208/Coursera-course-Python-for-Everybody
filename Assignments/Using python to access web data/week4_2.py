# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

current_repeat_count = 0
url = input('Enter url: ')
repeat_count = int(input('Enter count: '))
position = int(input('Enter position: '))

def parse_html(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    return tags
name = []
while current_repeat_count < repeat_count:
    print('Retrieving: ',url)
    tags = parse_html(url)
    for index,item in enumerate(tags):
        if index == position -1:
            url = item.get('href',None)
            name.append(item.contents[0])
            break
        else:
            continue
    current_repeat_count += 1
print('Sequence of Names: ',end="")
for i in name:
    print(i,end=" ")
print()
print('Last Name: ',name[-1])
