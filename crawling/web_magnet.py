from flask import Flask
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup
import re


app = Flask(__name__)


def search_google(keyword, start_page, end_page=None):
    url = 'https://www.google.com/search?&q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D&'.format(
        keyword)

    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36,gzip(gfe)'}

    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, 'lxml')
    links = bs.select('div.g > div > div.rc > div.r > a')

    results = []

    if end_page is None:
        counts = bs.select('div#resultStats')[0].text.replace(
            '검색결과 약', '').replace('개', '').replace(',', '').split('(')[0].strip()
        end_page = int(int(counts) / 10)

        if end_page > 30:
            end_page = 30

    number = 0

    for a in links:
        href = a['href']
        texta = a.select('h3')
        if len(texta) <= 0:
            continue

        title = texta[0].text

        # print(href)

        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, 'lxml')
            magnets = bs.find_all('a', href=re.compile(r'magnet:\?xt=*'))

            # print(title)
            # print('-'*40)
            # print(magnets)
            # print('+'*40)

            number += 1
            # print(start_page, '--', number)

            if len(magnets) > 0:
                magnet = magnets[0]['href']
                # print(magnet)
                # print('*'*50)
                # print('찾았습니다.')

                results.append({
                    'magnet': magnet,
                    'title': title
                })

        except:
            pass

    if start_page < end_page:
        start_page += 10
        results.extend(search_google(keyword, start_page, end_page=end_page))

    return results






@app.route('/', methods=["GET", "POST"])
def index():
    if 'keyword' in request.form:
        keyword = request.form['keyword']
        results = search_google(keyword, 0)


    else:
        results = []

    if len(results) > 0:
        return render_template('index.html', **{'magnets':results})
    else:
        return render_template('index.html')





if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 9995, debug = True)

