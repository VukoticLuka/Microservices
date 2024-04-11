import requests
from requests import codes


params = {
    "name" : "Luka",
    "age" : 23
}
response = requests.get("https://httpbin.org/get",params=params)

print(response.status_code)

res_json = response.json()

#url

print(response.url)

#izvukao sam ip adresu
print(res_json['origin'])


payload = {
    "name" : "Mike",
    "age" : 25
}

response2 = requests.post("https://httpbin.org/post",data=payload)

if response.status_code == 404:
    print("Not found")

else:
    print(response.status_code)




#print(response2.json())



response3 = requests.get("https://httpbin.org/ip")

#dobije ip adresu onog ko je zatrazio informaciju
print(response3.json())