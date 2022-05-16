import requests

req = requests.get('https://alexa-skills-erickson-lopes.herokuapp.com/wilt')


for key, value in req.json().items():
    print(key, value)

