import requests
import bs4

def isClear():
    ejudge = requests.get('http://ejudge.cfuv.ru/2018/II_semestr/standings/standings377.html')
    dom = bs4.BeautifulSoup(ejudge.text, features="lxml")
    if (len(dom.select('tr')) > 10):
        return False
    return True