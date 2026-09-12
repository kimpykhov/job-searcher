import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.greenhouse.com/uk")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    page_title = soup.title.text
    print("page title:", page_title)

