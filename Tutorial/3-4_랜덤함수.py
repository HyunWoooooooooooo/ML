
from random import *
print(random())  #0.0이상 1.0미만의 임의의 값 생성 하는 코드
print(random() *10) #0.0이상 ~10.0미만의 임의의 값 생성
print(int(random() *10)) # 정소 출력할려면 랜덤을 int로 감싼다,
print(int(random() *10))
print(int(random() *10))
print(int(random() *10) +1) #1~10이하의 임의의값 생성
print(int(random() *10) +1)
print(int(random() *10) +1)
print(int(random() *10) +1)
print(int(random() *10) +1)

#로또 번호 생성 코드(1부터 45이하의 값 생성)
for x in range(2):
    print(int(random()*45)+1) 

print(randrange(1, 45)) #1~ 44이하의 임의의 값 생성, 끝의 수 포함x
print(randrange(1, 46)) #1~ 45이하의 임의의 값 생성

print(randint(1,45)) #1~ 45이하의 값 생성, 끝의 수 포함o

for x in range(10):
    print(int(random()))

for x in range(20):
    print(int(random() *10) +1)