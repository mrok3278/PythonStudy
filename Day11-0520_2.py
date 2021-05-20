# Day11-0520.py

import requests
from bs4 import BeautifulSoup

res = requests.get('https://unse.daily.co.kr/?p=zodiac')
bs = BeautifulSoup(res.text, 'html.parser')

section = bs.select_one('#card')
uls = section.select('ul')

#code_1 > li.start_li > div.txt_box > b

for ul in uls:
    
    print(ul.select_one('li.start_li > div.txt_box > b').get_text(),'=', ul.select_one('li.start_li > div.txt_box > p').get_text())
    #code_1 > li:nth-child(2) > span
    
    for i in range(2,7,1):
        year = ul.select_one(f"li:nth-of-type({i}) > span").get_text()
        text = ul.select_one(f"li:nth-of-type({i}) > p").get_text()
        print(year, "=", text)
        
    print()
