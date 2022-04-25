# class1.py
#1)클래스를 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
#3)메스드 호출
p1.print()

p2 = Person()
#멤버변수
p2.name = "전우치"
#멤버 메서드 호출
p2.print()

#런타임(실행중)-디자인타임(코딩)
Person.title = "New title"
print(p1.title)
print(p2.title)
print(Person.title)



        