# 네이버 스펙업 공채 실시간 정보
import requests
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get(
    "https://m.cafe.naver.com/ArticleList.nhn?search.clubid=15754634&search.menuid=1481&search.boardtype=L",
    headers=headers,
)

req.encoding = "utf-8"  # Clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가해줘야합니다.

html = req.text
soup = BeautifulSoup(html, "html.parser")
posts = soup.select("strong.tit")
latest = posts[1].text

with open(os.path.join(BASE_DIR, "latest.txt"), "r+") as f_read:
    before = f_read.readline()
    if before != latest:
        # 같은 경우는 에러 없이 넘기고, 다른 경우에만
        # 메시지 보내는 로직을 넣으면 됩니다.
        f_read.close()

with open(os.path.join(BASE_DIR, "latest.txt"), "w+") as f_write:
    f_write.write(latest)
    f_write.close()


# for i, v in enumerate(posts):
#     if (len(posts) - 1) == i:
#         pass
#     else:
#         print(v.text.strip())

