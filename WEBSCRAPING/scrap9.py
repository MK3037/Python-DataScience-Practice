from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")
driver=webdriver.Chrome()
driver.get('https://www.nseindia.com/')

with open('scrap9.txt','w') as f:
    time.sleep(1)
    scoup=BeautifulSoup(driver.page_source,'lxml')
    
    f.write('#MARKET STATISTICS\n')
    for x in  scoup.find('div',class_='ms_indicater').find_all('div',class_='col-xxl-3 col-xl-3 col-lg-3 col-md-3 col-sm-6 col-6'):
        data=x.find('a').text
        title=x.find('p').text
        f.write(title.strip()+': '+ data+'\n')

    for x in scoup.find('div',class_='ms-no-stocks').find_all('div',class_='col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6'):
        data=x.find('a').text
        title=x.find('p').text
        f.write(title.strip()+': '+ data+'\n')
    
    f.write('\n#MARKET TURNOVER\n')
    column = ['product', 'volume', 'value', 'open interest', 'updated on']
    cells = scoup.find('div', class_='col-xxl-6 col-xl-6 col-lg-6 col-md-12 col-sm-12 col-12 mt-5 mt-lg-0').find('tr', class_='Total').find_all('td')
    row_dict = dict(zip(column,[x.text.strip() for x in cells]))
    for title, data in row_dict.items():
            f.write(f'{title}: {data}\n')
