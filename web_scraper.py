import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    
    print("Quotes found on the page:\n")
    for q in quotes:
        print("-", q.text)
else:
    print("Failed to fetch the webpage.")
