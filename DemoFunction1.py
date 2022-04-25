# DemoFunction1.py
#함수정의
def setValue(newValue):
    print("값 출력:",newValue)

#호출
#중단점(Break Point)
retValue = setValue(5)
print(retValue)

#함수 정의
def swap(x,y):
    return

#호출
retValue = swap(5,6)
print(retValue)

#기본값이 있는 함수
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#가변인자 함수
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

#정의되지 않은 인자(필수,옵션)
def userURIBuilder(server,port,**user):
    strURL = "https://"+server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIBuilder("ycampus","80", id="kim", passwd="1234"))     
print(userURIBuilder("ycampus","80", id="kim", passwd="1234", name="mike"))

#람다 함수(이름이 없는 간단한 함수)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))







