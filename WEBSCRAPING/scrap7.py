from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\python\\WEBSCRAPING")
driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/frames/')

with open('scrap7.txt','w',encoding='utf-8') as f:
    
    #GETTING TITLE FROM MAIN PAGE
    time.sleep(2)
    scoup=BeautifulSoup(driver.page_source,'lxml')

    title=scoup.find('div',id ='page').find('div',class_='col-md-12')
    title=title.find('h1').text
    f.write(title.strip())

    #MOVING INSIDE THOSE IFRAMES
    driver.get('https://www.scrapethissite.com/pages/frames/?frame=i')
    time.sleep(2)
    scoup=BeautifulSoup(driver.page_source,'lxml')
    cards=scoup.find_all('div',class_='col-md-4 turtle-family-card')

    #LOOPING THROUGH EACH CARD OF DIFFERENT TURTELS IN IFRAME
    for x in cards:
        heading=x.find('h3').text
        f.write('\n'+heading.strip())

        #GOING INSIDE LINK OF EACH TURTLE
        link='https://www.scrapethissite.com'+x.find('a')['href']
        driver.get(link)
        time.sleep(2)
        scoup1=BeautifulSoup(driver.page_source,'lxml')

        detail=scoup1.find('p').text

        f.write('\n'+detail.strip()+'\n')

driver.quit()