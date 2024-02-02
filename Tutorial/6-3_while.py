# customer = "토르"
# index = 5
# # while 조건:  #while은 특정 조건을 만족 할때까지 반복하라는 의미이다.
# while index >= 1:
#     print("{},커피가 준비 되었습니다. {}번 남았어요".format(customer, index))
    
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

#     #     print문 아주 중요/ 종류가 다른 변수 두개를 지정하고 그 두 변수를 format에 한번에 넣기 가능
#     # 앞의 소괄호 안에 1, 0 순으로 넣으면 바꿔서 출력하는 것도 가능
#     # -=이것도 앞에서 배웠다.1을 빼고 그 값을 index에 대입한다는 의미

# customer = "아이언맨"
# index = 1
# while True:
#     print("{},커피가 준비 되었습니다. 호출 {}회".format(customer, index))
#     index += 1  #계속해서 반복하는 걸 무한 루프라고 한다. ctrl+c면 종료
# index +=1이 뒤에 오는 이유는 index가 1인 값을 출력 한 후 하나씩 올라갈거니까 gpt참조
    
customer = "토르"
person = "unknown"

while person != customer : #person이 customer이랑 다를때 실행
    print("{}, 커피가 준비 되었습니다".format(customer))
    person = input("이름이 어떻게 되세요?")

#해석을 해보자구요. customer은 토르고 person은 unkown이다. person과 customer가 다를때
    # print문을 실행하는데 토르 커피가 준비되었습니다. 를 출력한 후에 
    # 이름이 어떻게 되세요? 를 유저에게 받고 그걸 person에 넣는다 while 조건에 맞는 답이 입력되면
    #while문을 탈출하게 된다,