import requests

response = requests.get("http://localhost:5000/names")
test_txt = response.text
print(test_txt)

