from bs4 import BeautifulSoup
import requests
import os
os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")

with open('scrap4.csv','w') as f:
    
    source=requests.get('https://www.scrapethissite.com/pages/forms/?page_num=1').text
    source=BeautifulSoup(source,'lxml')

    header_row = source.find("tr")
    columns=[x.text.strip() for x in header_row.find_all('th')]
    f.write(",".join(columns)+"\n")

    for i in range(1,25):
        source=requests.get(f'https://www.scrapethissite.com/pages/forms/?page_num={i}').text
        source=BeautifulSoup(source,'lxml')

        for x in source.find_all('tr',class_='team'):
            data=[y.text.strip() for y in x.find_all('td')]
            f.write(",".join(data)+'\n')

        # Team_Name=x.find('td',class_='name').text
        # Year=x.find('td',class_='year').text
        # Wins=x.find('td',class_='wins').text  
        # Losses=x.find('td',class_='losses').text
        # OT_Losses=x.find('td',class_='ot-losses').text
        # Wins%=x.find('td',class_='pct text-success').text
        # GoalGF=x.find('td',class_='gf').text
        # GoalAG=x.find('td',class_='ga').text
        # PlusMinus=x.find('td',class_='diff text-success').text
        #and then using f string is very long

    
    