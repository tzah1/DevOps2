import requests

response = requests.get('https://en.wikipedia.org/')
if response.status_code == 200:
    print('Page loaded lllllllsuccessfully')
    print(type(response))
    print(type(response))
    print(type(response))
    print(type(response))

    print(response.text[:100])
