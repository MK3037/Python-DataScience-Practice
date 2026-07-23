from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")
driver = webdriver.Chrome()
driver.get('https://in.tradingview.com/symbols/NSE-NIFTY/options-chain/')

with open('scrap10.txt', 'w', encoding='utf-8') as f:
    time.sleep(40)
    scoup = BeautifulSoup(driver.page_source, 'lxml')

    table = scoup.find('table')

    currentprice = float(scoup.find('span', attrs={'class': lambda c: c and 'priceWrap' in c}).text.replace(',', ''))

    for row in table.find_all('tr'):
        if row.get('data-strike'):
            all_tds = row.find_all('td')

            delta_td = abs(float(all_tds[4].text))
            ltp_td = float(all_tds[16].text)
            lambd1=(currentprice/ltp_td)*delta_td

            delta_td = abs(float(all_tds[45].text.replace('−', '-')))
            ltp_td = float(all_tds[33].text)
            lambd2=(currentprice/ltp_td)*delta_td

            strikeprice=all_tds[24].find('span',class_='ellipsisContainer-Mym3My5x').text
            f.write(f'{strikeprice}: {lambd1}             {lambd2}\n')

    f.write(str(currentprice))