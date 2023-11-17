import requests
import json
import config

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photo"
cred = config.key
query_params = {"api_key": cred , "earth_date": "2023-07-02"}
response = requests.get(endpoint, params=query_params)

print(response)