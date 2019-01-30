import requests
import bs4

def isClear(s):
    if (len(s.select('tr')) > 10):
        return False
    return True

ejudge = requests.get('http://ejudge.cfuv.ru/2018/II_semestr/standings/standings377.html')
dom = bs4.BeautifulSoup(ejudge.text, features="lxml")