#부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(    # 줄바꿈 연결\
            self.name, self.phoneNumber))

#자식 클래스
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        #self.name = name        
        #self.phoneNumber = phoneNumber
        #명시적으로 부모 클래스 생성자 호출 
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받아서 마음에 안들면 재정의 (Overisde)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(    # 줄바꿈 연결\
            self.name, self.phoneNumber))
        print("Info(Name:{0}, Phone Number: {1}, subject Number: {2}, studentID Number: {3})".format(    # 줄바꿈 연결\
            self.name, self.phoneNumber,self.subject,self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
#print(p.__dict__)   #루트 클래스가 가지고 있는 멤버변수 
#print(s.__dict__)

p.printInfo()
s.printInfo()   #부모를 호출함. 




