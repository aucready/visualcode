import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/point/af/list.nhn?&page=1000"
r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")

trs = bs.select("table.list_netizen > tbody > tr")
for tr in trs:
    tds = tr.select('td')
    print(tds)
    if len(tds) != 5:
        continue
    number = tds[0].text
    point = tds[1].text
    movie = tds[1].select('a')[0].text
    writer = tds[2].select('a')[0].text 
    print(number, movie, writer, point)
