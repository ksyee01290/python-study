import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

for autho,quote in zip(author,quotes):
    print(autho.text,quote.text)

