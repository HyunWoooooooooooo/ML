# 문자열을 쭉 입력 받고, 이전의 문자와 지금 입력받은 문자를 확인한다. 
# 이때 시작과 끝을 별도의 조건으로 구분지어줘야 index 오류가 안난다.
# 만약 같다면 count를 1을 올린다. 만약 다르다면 count를 2를 올린다. 


# times = int(input())
# count = 0

# for i in range(times):
#     word = input()
#     for i in word:#i가 마지막일때는 전의 알파벳이랑 비교
#         if i == len(word):  #요쪽 논리 더 생각해보기
#             if word[i-1] == word[i]:
#                 count = count
#             else:
#                 count += 1
#         else: #i가 마지막이 아닐 때
#             if word[i] == word[i+1]:  #i가 마지막일때 도 따로 구분 지어줘야 함
#                 count +=1
#             else:
#                 count +=2
#     print(count)


# 그냥 지금 들어온거랑 지금까지 들어온거를 전부 비교해서 같은게 있으면 그룹
# 이 아니다. 그런데 이게 연속되면 또 그룹이다 만 조건문으로 규정 한다면?

times = int(input())
err = []

for i in range(times):
    word = input()
    for j in word:
        


        


