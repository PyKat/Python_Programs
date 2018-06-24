import requests
from bs4 import BeautifulSoup

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
soup = BeautifulSoup(page.content, 'html.parser')
#soup.find_all('p')      Finds AllInstances
#Below statement prints First occarance of P tag. It also prints the text inside the tag
print(soup.find_all('p')[0].get_text())
