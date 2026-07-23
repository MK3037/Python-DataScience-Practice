import requests
from bs4 import BeautifulSoup
import os

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")
source=requests.get('https://www.scrapethissite.com/pages/simple/').text

source=BeautifulSoup(source,'lxml')
# print(source)

print(source.find('title').text)        #.text to remove <title>

for x in source.find_all('div', class_="col-md-12"):
    paragraph = x.find('p', class_="lead")
    
    if paragraph: 
        print(paragraph.text.strip())

with open('scrap3.csv','w',encoding='utf-8') as f:

    f.write('COUNTRY, CAPITAL, POPULATION, AREA(KM^2), POPULATION/KM^2\n')
    for x in source.find_all('div',class_='col-md-4 country'):
        places=x.find('h3')
        capital=x.find('span')
        population=x.find('span',class_='country-population')
        area=x.find('span',class_='country-area')
        population_persqkm=float(population.text)/float(area.text) if float(area.text) > 0 else 0
        f.write(f'{places.text.strip()},{capital.text.strip()},{population.text.strip()},{area.text.strip()},{population_persqkm}\n')

