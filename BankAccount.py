# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #이름변경(외부에서는 다른이름으로 접근)
        self.__id = id      # __ 클래스안에서 privete 멤버변수로 사용함.  숨기고 싶을때 __로 사용
        self.__name = name 
        self.__balance = balance   #생성자 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#외부에서는 _클래스명__변수명(백도어) 접근할수 있다. 
print(account1.BankAccount__balance) 
print(account1)    #객체를 출력해
