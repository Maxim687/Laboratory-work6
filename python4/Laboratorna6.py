from bs4 import BeautifulSoup
import requests
from collections import Counter
from lxml import html
from string import punctuation

r = requests.get("https://moz.gov.ua/article/news/oznaki-dlja-viznachennja-regionu-zi-znachnim-poshirennjam-covid-19")
soup = BeautifulSoup(r.text, 'html.parser')
links = [a['href'] for a in soup.find_all('a')]
print('Посилання на сторінці:')
for i in links:
    print(i)
    count = len(links)
print('Кількість посилань: {}'.format(count))

images = soup.find_all('img')
print ('Кількість зображень:', len(images))

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
counter = Counter(x.rstrip(punctuation).lower() for y in text for x in y.split())
print('Підрахунок різних слів:', counter.most_common())

cont = html.fromstring(r.content)
items = cont.cssselect('*')
tags = [x.tag for x in items]
c = Counter(tags)
print ('Теги на сторінці:', repr(c).strip('Counter'))