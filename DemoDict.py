from cgitb import reset


a={1,2,3}
b=list(a)
print(type(b))
print(b)
b.append(4)
print(b)


#함수 정의
def calc(a,b):
    return a+b, a*b


#함수 호출
result = calc(3,4)
print(result[0])
print(result[1])

#한번에 입력
args = (5,6)
print(calc(*args))

#딕셔너리(dict)
device = {"아이폰":5, "아이패드":10, "윈도우":20}
#입력
device["맥북"] = 15
print(device)
print(device["아이폰"])
#수정
device["아이폰"] = 6
#삭제
del device["윈도우"]
print(device)

#반복구문
for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)    



