import requests

url = "https://biometricvisionapi.com/v1/compare"

payload = {}
files = [
    ('image1', open('/Users/rajaathota72/Desktop/puja.jpeg','rb')),
    ('image2', open('/Users/rajaathota72/PycharmProjects/Bankassistsolution/user_database/puja/puja.png','rb'))
]
headers = {
    'X-Authentication-Token': '7qiLDY2QQAfRuxH3xsoAmfSSYojjC4KQpoOkgRokTFrxcYnAunmMG5iJ1qiFZoN7',
    'Content': 'application/json',
}
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
m = response.text.find('utf8')
print(m)

