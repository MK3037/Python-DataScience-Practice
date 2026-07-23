from bs4 import BeautifulSoup
import requests

source=requests.get("https://www.scrapethissite.com/pages/").text


# print(source)                             requests.get("") gets the required html code

soup=BeautifulSoup(source,'lxml')           #but that source code is plain text and doesnt make any scense to python, so BeautifulSoup is the architect that takes that pile of text, organizes it, and builds a neat, searchable blueprint out of it.
# print(soup.prettify())                      #is used to make that raw HTML look neat, indented, and human-readable in your terminal.

x=soup.find('title')
print(x)

for article in soup.find_all('div',class_="page"):
    heading=article.h3.text
    summary=article.p.text
    summary=summary.strip()
    heading=heading.strip()
    print(heading)
    print(summary)
    print()


#WHY BEAUTIFULL SCOUPE MATTERS:
# # Find the first <h1> heading on the page
# main_heading = soup.find('h1')

# # Grab every single hyperlink (<a> tag) on the page
# all_links = soup.find_all('a')

# # Target a very specific element using its CSS class
# sidebar = soup.find('div', class_='sidebar-content')
