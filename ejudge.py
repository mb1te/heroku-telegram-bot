import requests
import bs4

def getPage():
    ejudge = requests.get('http://ejudge.cfuv.ru/2018/II_semestr/standings/standings377.html')
    return ejudge.text

def isClear(url):
    ejudge = requests.get(url)
    dom = bs4.BeautifulSoup(ejudge.text, features="lxml")
    if (len(dom.select('tr')) > 10):
        return False
    return True

def get_ans(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    b = bs4.BeautifulSoup(r.text, features = 'lxml')
    table = b.find_all('table')[1]
    n = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        s = []
        for c in cols:
            if c.get_text() == '\xa0':
                s.append("n")
            else:
                s.append(c.get_text())
        n.append(s)
    n.pop(0)
    ans = ""
    for i in n:
        for j in i:
            k = j.split()[0]
            ans += k[:min(len(k), 10)]
            for z in range(max(0, 10 - len(k))):
                ans += " "
        ans += "\n"
    return ans