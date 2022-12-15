from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
html = requests.get(url)
html = html.text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify)
# print(soup.title.string +" : "+soup.title.name)
# print(soup.find_all('a')[0])
with open('url_file.txt', 'w') as f:
  for link in soup.find_all('a'):
    print(link.get('href'))
    f.write(link.get('href'))
    f.write("\n")


# Exotic India Main Page All URLs

url_exotic ="https://www.exoticindiaart.com/"

html_exotic = requests.get(url_exotic)
html_exotic = html_exotic.text

soup_exotic = BeautifulSoup(html_exotic, 'html.parser')
# print(soup.prettify)
# print(soup.title.string +" : "+soup.title.name)
# print(soup.find_all('a')[0])
with open('exotic_url_file.txt', 'w') as f:
  for link in soup_exotic.find_all('a'):
    print(link.get('href'))
    f.write(link.get('href'))
    f.write("\n")
