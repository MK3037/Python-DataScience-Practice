from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")
driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/ajax-javascript/')
years=['2015','2014','2013','2012','2011','2010']

with open('scrap5.csv','w') as f:
    driver.find_element(By.LINK_TEXT,'2015').click()
    time.sleep(1.5)
    scoup=BeautifulSoup(driver.page_source,'lxml')
    
    columns=[x.text.strip() for x in scoup.find_all('th')]
    f.write('Year,'+','.join(columns)+'\n')

    for i in years:
        driver.find_element(By.LINK_TEXT,i).click()
        time.sleep(1.5)
        livehtml=driver.page_source
        scoup=BeautifulSoup(livehtml,'lxml')

        year=scoup.find('div',class_='col-md-12 text-center').find('a',class_='year-link active').text

        x=scoup.find('tr',class_='film')
        first=[y.text.strip() for y in x.find_all('td')]
        f.write(f"{year},{','.join(first)}\n")

    driver.quit()