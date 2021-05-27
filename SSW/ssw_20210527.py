'''
Chromedriver 다운로드
    https://chromedriver.chromium.org/downloads
    
Selenium 설치 방법
    pip install selenium
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://map.kakao.com/')

# 지도 설정 관련 안내 레이어 닫기
img_notice = driver.find_element_by_xpath('/html/body/div[10]/div/div/div/strong')
img_notice.click()
time.sleep(1)   # 1초 대기

# 로그인 버튼 클릭
btn_login = driver.find_element_by_xpath('//*[@id="btnLogin"]')
btn_login.click()
time.sleep(1)   # 1초 대기

# QR 코드로 로그인 버튼 클릭
btn_qr = driver.find_element_by_xpath('//*[@id="move_to_qr"]')
btn_qr.click()
time.sleep(1)   # 1초 대기

input('로그인 후 엔터키를 눌러주세요.')

f = open('placelist.txt', 'r', encoding='utf-8')
placelist = f.readlines()
f.close()

for place in placelist:
    print(place)

    # 장소 검색
    input_search = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
    input_search.clear()    # 기존 입력된 내용 삭제
    input_search.send_keys(place, Keys.ENTER)
    time.sleep(1)   # 1초 대기

    # 즐겨찾기 등록 여부 확인
    marked = driver.find_element_by_xpath('//*[@id="info.search.place.list"]/li[1]/div[1]/a[1]/span[2]')
    print(marked.text)
    if marked.text:
        print('이미 등록되어 있습니다.')
    else:
        # 결과 중 첫번째 장소 북마크 클릭
        a_first_place = driver.find_element_by_xpath('//*[@id="info.search.place.list"]/li[1]/div[1]/a[1]')
        a_first_place.click()
        time.sleep(1)   # 1초 대기

        # 첫번째 폴더 클릭
        a_first_folder = driver.find_element_by_xpath('/html/body/div[20]/div[2]/div[2]/ul/li[2]/a')
        a_first_folder.click()
        time.sleep(1)   # 1초 대기

        # 완료 버튼 클릭
        btn_finish = driver.find_element_by_xpath('/html/body/div[20]/div[3]/form/fieldset/div[3]/button')
        btn_finish.click()
        time.sleep(1)   # 1초 대기

        # 완료 후 팝업창 닫기 클릭
        a_close = driver.find_element_by_xpath('/html/body/div[20]/div[7]/div[2]/a')
        a_close.click()
        time.sleep(1)   # 1초 대기

print('즐겨찾기 완료!')
