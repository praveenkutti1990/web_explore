#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://economictimes.indiatimes.com/markets/gold-rate-in-india-today"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table_list = soup.findAll('table', attrs={'class':'table lg_txt rf_rr'})

# for row in table_list[1].find_all('tr'):
#     print("************")
#     data = row.find_all('td')
#     if len(data) > 0:
#         print(data[0].text, data[1].text, data[2].text)

rows = table_list[1].find_all('tr')
data = rows[1].find_all('td')
if len(data) > 0:
    print(data[0].text, data[1].text, data[2].text)