import requests
#response = requests.get("https://api.thecatapi.com/")
#print(response.text)
#print(response.headers)
#print(response.status_code)
#print(response.reason)


##Inspecting headers
#response = requests.get("https://api.thecatapi.com/v1/breeds/abys")
#print(response.headers)
#print(response.headers.get('content-type'))

##Inspecting content type
#print(response.content)       #better used to inspect image content
#print(response.json())         #convert into a dictionary


#Query parameters
#print(requests.get("https://randomuser.me/api/?gender=female").json())
response = requests.get("https://randomuser.me/api/?gender=female&nat=de")
print(response.json())

query_params = {"gender":"Female", "nat":"de"}
requests.get("https://randomuser.me/api/", params=query_params).json()

