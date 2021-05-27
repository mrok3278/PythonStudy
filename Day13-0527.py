# Day13-0527.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('Resource/chromedriver.exe')
driver.get('https://map.kakao.com/')

img_notice = driver.find_element_by_xpath('/html/body/div[10]/div/div/div/strong')
img_notice.click()
time.sleep(1)

btn_login = driver.find_element_by_xpath('//*[@id="btnLogin"]')
btn_login.click()
time.sleep(1)

btn_QRLogin = driver.find_element_by_xpath('//*[@id="move_to_qr"]')
btn_QRLogin.click()
time.sleep(1)

input('Press enter key after login.')

file = open("Resource/PlaceList.txt", "r", encoding="utf-8")
sLines = file.readlines()
file.close()

for sLine in sLines:
    sLine = sLine.strip()
    sPlace = sLine.split(',')[0]
    sType = sLine.split(',')[1]
    
    if not sPlace:
        continue
    
    # 장소 검색
    input_search = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
    input_search.clear()
    input_search.send_keys(sPlace, Keys.ENTER)
    time.sleep(1)
    
    # 이미 등록된 장소
    marked = driver.find_element_by_xpath('//*[@id="info.search.place.list"]/li[1]/div[1]/a[1]/span[2]')
    if marked.text:
        continue
    
    # 결과 중 첫번째 장소 북마크 클릭
    a_first_place = driver.find_element_by_xpath('//*[@id="info.search.place.list"]/li[1]/div[1]/a[1]')
    a_first_place.click()
    time.sleep(1)
    
    # 첫번째 폴더 클릭
    a_first_folder = driver.find_element_by_xpath('/html/body/div[20]/div[2]/div[2]/ul/li[2]/a')
    a_first_folder.click()
    time.sleep(1)
    
    # 색상선택
    favoriteColor = driver.find_element_by_xpath(f'//*[@id="favoriteColor{sType}"]')
    favoriteColor.click()
    
    # 완료 버튼 클릭
    btn_finish = driver.find_element_by_xpath('/html/body/div[20]/div[3]/form/fieldset/div[3]/button')
    btn_finish.click()
    time.sleep(1)
    
    # 완료 후 팝업창 닫기 클릭
    a_close = driver.find_element_by_xpath('/html/body/div[20]/div[7]/div[2]/a')
    a_close.click()
    time.sleep(1)   # 1초 대기
  