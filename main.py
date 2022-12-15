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
    # print(link.get('href'))
    f.write(link.get('href'))
    f.write("\n")

# Exotic India Main Page All URLs

url_exotic ="https://www.exoticindiaart.com"

html_exotic = requests.get(url_exotic)
html_exotic = html_exotic.text
list_of_link =[]
soup_exotic = BeautifulSoup(html_exotic, 'html.parser')
# print(soup.prettify)
# print(soup.title.string +" : "+soup.title.name)
# print(soup.find_all('a')[0])
with open('exotic_url_file.txt', 'w') as f:
  for link in soup_exotic.find_all('a'):
    # print(link.get('href'))
    f.write(link.get('href'))
    list_of_link.append(link.get('href'))
    f.write("\n")

use_url=[]
for i in list_of_link[25:50]:
  print(url_exotic+i)
  use_url.append(url_exotic+i)
# for i in use_url[0:3]:
#   print(use_url[0:3])

html_exotic = requests.get(url_exotic)
html_exotic = html_exotic.text
list_of_link =[]
soup_exotic = BeautifulSoup(html_exotic, 'html.parser')
with open('exotic_url_file.txt', 'w') as f:
  for i in use_url:
    html_exotic = requests.get(i)
    html_exotic = html_exotic.text
    list_of_link =[]
    soup_exotic = BeautifulSoup(html_exotic, 'html.parser')
    for link in soup_exotic.find_all('a'):
      # print(link.get('href'))
      f.write(link.get('href'))
      list_of_link.append(link.get('href'))
      f.write("\n")