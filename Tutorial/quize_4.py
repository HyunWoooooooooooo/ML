# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨 3명은 커피 쿠폰을 받게 되니다.

# 조건1 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라 가정
# 조건2 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 radom모듈의 shuffle과 sample을 활용

# from random import *
# people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13, 14, 15, 16, 17, 18, 19, 20]
# select = sample(people, 4)
# print("--당첨자 발표--")
# print("치킨 당첨자:" +str(select[:1]))  #오류 발생/print구문 내에서 리스트와 문자열을 +로 바로 이을수 없다 따라서 str로 묶어줘야 한다,
# print("커피당첨자:"+str(select[1:]))    
# print("--축하합니다--")

from random import *  #코드 이해 시간 가지고 꼭 해보기 
users = range(1, 21) #1부터 20까지의 숫자를 생성
#print(type(suers)) > type이 list가 아니라 range가 나온다 그래서 list해줘야 함
users = list(users)
shuffle(users) #유저들을 무작위로 섞는다

winners = sample(users, 4) #유저중에서 무작위로 4명을 뽑는다
print("--당첨자 발표--")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피당첨자:{0}".format(winners[1:]))    
print("--축하합니다--")
