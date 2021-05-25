'''
웹 스크래핑과 웹 크롤링

- 웹 스크래핑
    * 웹 사이트 상에서 원하는 정보를 추출하는 기술

- 웹 크롤링
    * 웹 크롤러(자동화 봇)가 일정 규칙으로 웹 페이지를 브라우징하는 것

- 주의점
    * 서버에 과부하를 주는 등의 피해를 줄 수 있으므로, 법적인 문제에 대해 전문적으로 알아볼 것
    * 특히, 학습용이 아닌 상용을 목적으로 크롤링 및 스크래핑시에는 더욱 주의할 것
    * robots.txt 에서 크롤링 가능 여부 확인
        .검색엔진 크롤링 봇들이 해당 파일 조회 후 수집 여부 결정
        .참조: https://searchadvisor.naver.com/guide/seo-basic-robots
'''

import requests    # 웹 페이지 접속
from bs4 import BeautifulSoup   # HTML 문서 파싱(구문 분석)

res = requests.get('https://finance.naver.com')
print(res.status_code)
# print(res.text)

bs = BeautifulSoup(res.text, 'lxml')    # 구문분석기: 'lxml', 'html.parser', ...
title = bs.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > h3')
print(title.get_text()) # get_text(): 해당 HTML 요소의 텍스트 추출

# company_name = bs.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr.down > th > a')
# print(company_name.get_text())

# company_name = bs.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-of-type(2) > th > a')    # 퀴즈: HMM 가져오기
# print(company_name.get_text())

# 부모 요소 찾기
tbody = bs.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')

# 자식 요소 찾기
trs = tbody.select('tr')
# print(trs)

for tr in trs:
    # print(tr.get_text())
    '''
    nth-child(n): 모든 요소가 순서에 포함
    nth-of-type(n): 해당 요소만 순서에 포함 (td 중에 n번째 요소)
    '''
    company_name = tr.select_one('th > a').get_text()
    price = tr.select_one('td:nth-of-type(1)').get_text()
    # 퀴즈: 변동량을 가져와보세요
    diff = tr.select_one('td:nth-of-type(2) > span').get_text()
    icon = tr.get('class')[0]
    print(company_name, price, diff, icon)
