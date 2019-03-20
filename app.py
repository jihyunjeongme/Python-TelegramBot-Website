import os
import time
import random
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# # 파일의 위치
# BASE_DIR =

options = webdriver.ChromeOptions()

# options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
)
options.add_argument("lang=ko_KR")

## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(
    "/Users/jihyun/Documents/GitHub/Python-TelegramBot-Website/chromedriver",
    chrome_options=options,
)

time.sleep(5 + random.random() * 0.3)

## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
# driver.implicitly_wait(3)

## url에 접근한다.
driver.get("https://nid.naver.com/nidlogin.login")

time.sleep(5 + random.random() * 0.3)

## 아이디/비밀번호를 입력해준다.
driver.find_element_by_name("id").send_keys("stothyun&&^ㄴㅇi")
time.sleep(5 + random.random() * 0.3)

driver.find_element_by_name("pw").send_keys("gosdkdㅓㄴㅇi1")
time.sleep(5 + random.random() * 0.3)

## 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(7)

# 스펙업 카페로 이동한다.
driver.get("https://cafe.naver.com/specup")
time.sleep(3 + random.random() * 0.3)

# 스펙업 | 공채속보 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="special-menuLink-1481"]').click()
# time.sleep(3 + random.random() * 0.3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup)
# 스펙업 공채속보 - 헤드라인  뽑아 내기
headline = soup.select(
    "div.article-board m-tcol-c > table > tbody > tr > td > div.board-list > div.inner_list > a"
)

for n in headline:
    print(n.text.strip())
time.sleep(5)

# ul#special-menu-item li.selected > a
# ul  # special-menu-item li.selected > a
# ul  # special-menu-item li.selected > a

# ## 로그인 버튼을 눌러주자.
# driver.find_element_by_xpath('//*[@id="continue-button"]').click()
# time.sleep(10 + random.random() * 0.3)

