#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.livechennai.com/gold_silverrate.asp"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.select_one('table', attrs = {'class':'table-price'})

for row in table.findAll('tr'):
    for data in row.select('td:has(font)'):
        print(data.text)
    print("*******************************")