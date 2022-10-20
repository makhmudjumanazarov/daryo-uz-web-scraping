from bs4 import BeautifulSoup
import requests

import csv

t = True
i = 0

big_url = input('Linkni kiriting>>> ')
name = input('Dataframega nom bering:>>>')
header = ['title', 'content']
def script(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    try:
        title = soup.find('b').text
    except:
        title = 0
    contents_border = soup.find("div", class_="default__section border")
    c = ''
    if contents_border:
        contents = contents_border.findAll('p')
        for content in contents:
            try:
                c+=content.text
            except:
                c = c
    writer.writerow([title, c])


def page(big_url):
    html_text = requests.get(big_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('a', class_="mini__article-link")
    div = soup.find('div',class_='mini__article')
    s = 0
    if div:
        for new in news:
            url = f"https://daryo.uz{new['href']}"
            script(url)
        return True
    else:
        s+=1
        if s==5:
            return False
        else:
            return True

with open(f"{name}.csv", 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    while t:
        t = page(f"{big_url}?page={i}&per-page=10")
        i+=1



