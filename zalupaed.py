from bs4 import BeautifulSoup as bs
import requests as req
class Vacancy:
    vacname = ""
    salary = ""
    orgname = ""
i = 0
lang = ["1C", "C#", "Kotlin", "Java", "Python"]
text = lang[2]
baseUrl = 'https://hh.ru/search/vacancy?text='+text+'&area=1'
request = req.get('https://hh.ru/search/vacancy?text=Kotlin&area=1', headers={'User-Agent': 'Custom'})
bsparse = bs(request.text, "lxml")
f = 0
plitka = bsparse.find_all('div', 'serp-item')
for i in plitka:
    print(i.text)
    print("____")
    f = f +1
    print(f)

def get_vacname():
    strim = bsparse.find_all('a', 'serp-item__title')
def get_sallary():
    strimsal = bsparse.find_all('span', 'bloko-header-section-3')
def get_orgname():
    pass


def rab_varik():
    strim = bsparse.find_all('a', 'serp-item__title')
    strimsal = bsparse.find_all('span', 'bloko-header-section-3')
    strimname = bsparse.find_all('a', 'bloko-link bloko-link_kind-tertiary')
    for p in strim:
        print(p.text)
        i = i + 1
    print(i)
    i = 0
    print("_________________________")
    for p in strimsal:
        print(p.text)
        i = i + 1
    print(i)
    i = 0
    print("_________________________")
    for p in strimname:
        print(p.text)
        i = i + 1
    print(i)
    i = 0

