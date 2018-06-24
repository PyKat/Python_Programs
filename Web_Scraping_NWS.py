import requests
from bs4 import BeautifulSoup
req = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())
#print(list(soup.children))
#print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
#print(html)
#print(list(html.children))

body = list(html.children)[3]
#print(body)

ptag = list(body.children)[1]
#print(ptag)

print(ptag.get_text())

