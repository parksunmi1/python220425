# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식으로 검색
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,11):
        #클리앙의 중고장터 주소 
        #data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        
        #오늘의 유머
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n) 
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지면 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

#<td class="subject"><a href="/board/view.php?table=">창가의 멍뭉이</a>
     
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        title = item.text
                        print(title.strip())
                        #<a class='list_subject'><span>text</span><span>text</span>
                        #span = item.contents[1]
                        #span2 = span.nextSibling.nextSibling
                        #title = span2.text 
                        #if (re.search('아이폰', title)):
                        #        print(title.strip())
                        #        print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
