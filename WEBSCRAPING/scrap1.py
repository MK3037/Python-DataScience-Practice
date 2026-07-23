from bs4 import BeautifulSoup
import requests
import os
os.chdir("C:\\Users\\purve\\OneDrive\\Desktop\\extra\\webscraping")
with open("prac1.html") as html_file:
    soup=BeautifulSoup(html_file,'lxml')
print(soup)
print(soup.prettify())

# m=int(input("enter choice: "))
m=1
match m:
    case 1:
        match=soup.title
    case 2:
        match=soup.title.text
    case 2:
        match=soup.div
    case 3:
        match=soup.find('div',class_='foooter')
print(match)

for article in soup.find_all('div',class_='article'):
    heading=article.h2.a.text
    print(heading)
    summary=article.p.text
    print(summary)
    print() 