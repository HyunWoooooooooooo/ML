#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 규칙1: naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 =>naver
# 규칙3: 남은 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 +"!"로 구성
# 생성된 비밀번호 : hav51!

# adr =  "http://naver.com"
# print("%s%d%d!", format("nav", "5","1"))


#답
url = "http://naver.com"
my_str = url.replace("http://", "") #url함수에서 "http://를 찾아서 빈칸으로 바꿔라"
print(my_str)
my_str1 = my_str[0: 3 ]
print(my_str1)
password = my_str1 + str(len(my_str1)) + str(my_str.count("e")) +"!"
print("{0}의 비밀 번호는 {1}입니다".format(url, password))

