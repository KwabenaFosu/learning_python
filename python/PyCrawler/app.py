import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com/questions")
print(response)
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".s-post-summary.js-post-summary")
for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".s-post-summary--stats-item").getText())
    



