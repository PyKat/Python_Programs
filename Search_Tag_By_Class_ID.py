import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#Prints all p tags with class outer-text
print(soup.find_all('p', class_='outer-text' ))

#Prints any tag with class outer-text
#print(soup.find_all(class_='outer-text'))

#prints tag with id='first'
#print(soup.find_all(id='first'))



#Using CSS Selectors
print(soup.find_all('body p.outer-text'))