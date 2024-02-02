print("1")
print("2")
print("3")
print("4")
print("5")  #이 짓거리 안하려고 만든게 반복문 for이다.

for waiting_number in [0, 1, 2, 3, 4]:
    print("대기번호:{0}".format(waiting_number))
 # 처음에는 0이 waiting_number로 들어가고 아래 문장을 출력한다 그리고1 그리고2 순으로 반복


for waiting_no in range(5):   #ragne는 단순 반복 횟수를 넣을떄 사용 또한 0이상 5미만 까지의 수만 가능
    print("대기변호 : {0}".format(waiting_no))

for no in range(1, 5): #시작점을 지정하고 싶을 때의 형태
    print("대기번호 :{}".format(no))  #소괄호에 0이 없어도 문제없이 출력됨

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{},커피가 준비 되었습니다".format(customer))   
# 변수를 문자열 사이에 넣는 방법에는 여러가지 방법이 있다. %s 를 활용하는 방법,
# 지금까지 한것 처럼 변수를 따로 지정해주는 방법, 그 다음으로 소괄호를 이용하는 방법
# 소괄호를 이용하는 방법은 문자열 뒤에 .format()이 붙게 된다. format의 괄호 안에는
# 소괄호 안에 들어갈 정보와 관련된 변수나 값을 직접적으로 써준다 (문자열 포맷 내용)