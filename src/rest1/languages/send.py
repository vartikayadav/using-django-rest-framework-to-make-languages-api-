import requests

headers={}
headers['Authorization']='Bearer put your token here'
r=requests.get('https://localhost/8000',headers=headers)
print(r.text)
