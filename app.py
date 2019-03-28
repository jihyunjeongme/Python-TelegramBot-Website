# 네이버 스펙업 공채 실시간 정보
import requests
from bs4 import BeautifulSoup
import os
import telegram

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get(
    "https://m.cafe.naver.com/ArticleList.nhn?search.clubid=15754634&search.menuid=1481&search.boardtype=L",
    headers=headers,
)

# 토큰을 지정해서 bot을 선언해줍니다.
bot = telegram.Bot(token="781872977:AAH2AcUUdtdRDY_M1WhQQrAG6lfxhnYjteA")

# 테스트 봇, 가장 마지막으로 bot에게 말을 건 사람의 id를 지정
chat_id = bot.getUpdates()[-1].message.chat.id

req.encoding = "utf-8"  # Clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가해줘야합니다.

html = req.text
soup = BeautifulSoup(html, "html.parser")
posts = soup.select("strong.tit")
latest = posts[1].text

with open(os.path.join(BASE_DIR, "latest.txt"), "r+") as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id, text="새 글이 올라왔습니다!")
    else:  # 테스트 차 넣었음. 원래 필요 없음
        bot.sendMessage(chat_id=chat_id, text="새 글이 없어요ㅠ")
    f_read.close()

with open(os.path.join(BASE_DIR, "latest.txt"), "w+") as f_write:
    f_write.write(latest)
    f_write.close()


# for i, v in enumerate(posts):
#     if (len(posts) - 1) == i:
#         pass
#     else:
#         print(v.text.strip())

