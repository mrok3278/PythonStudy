# Day11-0520.py

import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com')

if res.status_code != 200:
    print("Connection failed")
    exit()

bs = BeautifulSoup(res.text, 'lxml')
#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > th > a

company_name = bs.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr.down > th > a')
print(company_name.get_text())

tbody = bs.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
print(tbody.get_text())

trs = tbody.select('tr')
print(trs)

for tr in trs:
    print("*" * 30)
   
    #container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > th > a
    name = tr.select_one('th > a').get_text()
    
    #container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > td:nth-child(2)
    price = tr.select_one('td:nth-of-type(1)').get_text()
    
    #container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > td:nth-child(3) > span
    diff = tr.select_one('td:nth-of-type(2) > span').get_text()
    
    #container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > td:nth-child(3) > em
    icon = tr.get('class')
    
    print(name, price, diff, icon)
