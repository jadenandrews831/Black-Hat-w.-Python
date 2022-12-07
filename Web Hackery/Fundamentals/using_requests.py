import requests
url = 'http://localhost:3000/blockchain'
response = requests.get(url)

data = {'amount': 300, 'sender': 'DSJ02110GMDOG20NG02', 'recipient': 'VO2N10NVE90VN2D02DMS'}
response = requests.post('http://localhost:3000/transaction', data=data)
print(response.text)