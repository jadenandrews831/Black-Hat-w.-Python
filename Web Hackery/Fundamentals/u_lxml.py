from io import BytesIO # Needed in order to use a byte string as a file object while parsing the HTTP response
from lxml import etree

import requests

url = 'https://nostarch.com'
r = requests.get(url)
content = r.content
print(type(BytesIO(content)))
parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)
for link in content.findall('//a'):
  print(f"{link.get('href')} -> {link.text}")

  