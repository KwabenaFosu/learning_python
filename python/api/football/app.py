import requests
import json
import credentials
endpoint = "https://api.football-data.org/v4/competitions/PL/teams/"

headers = {"X-Auth-Token" : credentials.key}
response = requests.get(endpoint, headers = headers)
teams = response.json()["teams"]
coaches = [team['coach'] for team in teams ] 
names = [coach['name'] for coach in coaches]
print(names)