import urllib.parse
import urllib.request

# url = 'https://www.google.com'
# with urllib.request.urlopen(url) as response:
#   content = response.read()

# print(content)

info = {'amount': 2500, 'sender': 'ADJF2089HG0AK039FKF0038', 'recipient': 'GJ29420SK349GJ20JG94J20'}
data = urllib.parse.urlencode(info).encode()

req = urllib.request.Request('http://localhost:3000/transaction', data)
with urllib.request.urlopen(req) as response:
  content = response.read()

print(content)