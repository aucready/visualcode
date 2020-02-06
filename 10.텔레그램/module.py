import os
import requests
from bs4 import BeautifulSoup



def get_dir_list(dir):
    str_list = ''
    if os.path.exists(dir):
        file_list = os.listdir(dir)
        file_list.sort()
        for f in file_list:
            full_path = os.path.join(dir, f)
            if os.path.isdir(full_path):
                f = '[' + f + ']'

            str_list += f
            str_list += '\n'
    str_list.split()
    return str_list


def get_weather(where):
    # div.today_area > ul.info_list
    weather = ''
    url = 'https://search.naver.com/search.naver?&query={}+날씨'.format(where)

    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'lxml')
    w_box = bs.select('div.today_area > div.main_info')
    # sub_box = bs.select('div.today_area > dl.indicator')
    print(w_box)

    if len(w_box) > 0:
        # indigator = bs.select('dt > a')
        
        temperature = bs.select('span.todaytemp')
        cast_text = bs.select('p.cast_txt')
        indicators = bs.select('span.indicator')

        if len(temperature) > 0 and len(cast_text) > 0 and len(indicators) > 0:
            # indigator = indigator[0].text
            temperature = temperature[0].text.strip()
            cast_text = cast_text[0].text.strip()
            indicators = indicators[0].text.strip()
            # print(temperature, cast_text, indicators)
            weather = '{}˚C\r\n{}\r\n{}'.format(
                temperature, cast_text, indicators)
    return weather

money_name = {
    '유로': '유럽연합 EUR',
    '엔': '일본 JPY (100엔)',
    '위안': '중국 CNY',
    '홍콩달라': '홍콩 HKD',
    '타이완달라': '대만 TWD',
    '파운드': '영국 GBP',
    '달라': '미국 USD'
}

def get_exchange_info():

    url = 'https://finance.naver.com//marketindex/exchangeList.nhn'
    EXCHANGE_LIST = {}

    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'lxml')
    trs = bs.select('table.tbl_exchange > tbody > tr')
    for tr in trs:
        tds = tr.select('td')
        name = tds[0].text.strip()
        value = tds[1].text.strip().replace(',', '')
        EXCHANGE_LIST[name] = value
    return EXCHANGE_LIST


def money_translate(keyword):
    EXCHANGE_LIST = get_exchange_info()
    keywords = []
    for m in money_name.keys():
        if m in keyword:
            keywords.append(keyword[0:keyword.find(m)].strip())    
            keywords.append(m)
            break

    if keywords[1] in money_name:
        country = money_name[keywords[1]]

        if country in EXCHANGE_LIST:
            money = float(EXCHANGE_LIST[country])
            if country == '일본 JPY (100엔)':
                money /= 100
            money = format(round(float(money) * float(keywords[0]), 3), ',')
            output = '{} 원'.format(money)
            return output



    print(keywords)







# get_weather('서울')

if __name__ == "__main__":
    print(money_translate('150홍콩달라'))






