# demoRE.py

import re 

#print(dir(re))

result = re.search("[0-9]*th"," 35th")
print(result)
print(result.group())

#블럭으로 주석처리 : 선택후 ctrl + /
# result = re.match("[0-9]*th","35th")
# print(result)
# print(result.group())

print(bool(re.search("ap","this is apple"))) 
print(bool(re.match("ap","this is apple")))  

#우편번호,년도
result = re.search("\d{4}","올해는 2022년입니다.")
print(result.group())

result = re.search("\d{5}","우리 동네의 우편번호는 52100입니다.")
print(result.group())
