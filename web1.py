# web1.py
#웹 크롤링(데이터 수집)
from bs4 import BeautifulSoup

#문서를 읽어서 문자열 변수로 리턴(rt=reat text)
page = open("c:\\work\\test01.html","rt",encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

#print(soup.prettify())

#문서에 있는 모든 <p>태그를 검색
#print(soup.find_all("a"))

#첫번째 <p>태그 검색
#print(soup.find("p"))
#<p class='outer-text'> 스타일
print(soup.find_all("p",class_="outer-text"))

#문자열만 출력
for tag in soup.find_all("p"):
    #내부 컨텐츠만(.text)
    title = tag.text
    title = title.replace("\n","")
    title = title.replace("\t","")
    print(title.strip())

