import requests
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame()
tabs = []
website_url = requests.get(
    "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area").text
soup = BeautifulSoup(website_url, "lxml")
# print(soup.prettify())
my_table = soup.find('table', {'class': 'wikitable sortable'})
# print(my_table)

links = my_table.findAll('a')
# print(links)

for tr in my_table.find_all('tr'):
    tabs.append({
        'Rank': tr.find_all('td')[0].string,
        'Area': tr.find_all('td')[2].string,
        'Notes': tr.find_all('td')[3].string
    })

print(tabs)

countries = []
for link in links:
    countries.append(link.get('title'))

#print(countries)

# Convertimos la lista en un Datframe de Pandas
df['Country'] = countries

df