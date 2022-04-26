#web2.py
from imp import source_from_cache
import urllib.request
from bs4 import BeautifulSoup

#파일에 쓰기(wt= write text)
f = open("c:\\work\\webtoon.txt","wt",encoding="utf-8")

#규칙이 있는 숫자의 열(수열)을 생성하는 코드
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" +str(i)
    print(url) 
    #웹사이트에 요청해서 문자열 받기
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체 만들기
    soup = BeautifulSoup(data,"html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text
        print(title.strip())
        f.write(title.strip() + "\n")

f.close()



                    