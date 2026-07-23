from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time instead of time with specifcally waiting for 2 sec, we use wait to exit the moment data is loaded
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")
driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/ajax-javascript/')
wait = WebDriverWait(driver, 10)
years=['2015','2014','2013','2012','2011','2010']

with open('scrap5.csv','w') as f:
    driver.find_element(By.LINK_TEXT,'2015').click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'th')))
    scoup=BeautifulSoup(driver.page_source,'lxml')

    columns=[x.text.strip() for x in scoup.find_all('th')]
    f.write('Year,'+','.join(columns)+'\n')

    for i in years:
        driver.find_element(By.LINK_TEXT,i).click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'film')))
        livehtml=driver.page_source
        scoup=BeautifulSoup(livehtml,'lxml')

        year=scoup.find('div',class_='col-md-12 text-center').find('a',class_='year-link active').text

        x=scoup.find('tr',class_='film')
        first=[y.text.strip() for y in x.find_all('td')]
        f.write(f"{year},{','.join(first)}\n")

    driver.quit()