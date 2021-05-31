import requests

BASE_URL = "http://127.0.0.1:5000/"

data = [{"likes": 100, "name": "programming with bishal", "views": 300},
        {"likes": 2000, "name": "programming with janak", "views": 3000},
        {"likes": 10, "name": "programming with ram", "views": 2500}]

for i in range(len(data)):
    response = requests.put(BASE_URL + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE_URL + "video/0")
print(response)
input()
response = requests.get(BASE_URL + 'video/2')
print(response.json())
