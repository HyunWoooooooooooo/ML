# #리스트 : 순서를 가지는 객채의 집합

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

subway = ["정민지", "정만지","정지민"] #0,1,2,순서임
print(subway)
print(subway[1])

# #민지가  몇 번째 칸에 타고 있는가

# print(subway.index("정민지"))

# #다음 칸에 김현우가 탔다,append는 맨 뒤에 추가함
# subway.append("김현우")
# print(subway)

# #김현우2를 정민지랑 정만지 사이에 넣는다
# subway.insert(1, "김현우2")
# print(subway)

# #지하철에 있는 사람을 뒤에서 한명씩 꺼냄
# print(subway.pop()) #=누가 나갔는지 보는 코드
# print(subway)  # 누가 남았는지 보는 코드


# #같은 이름의 사람이 몇명 있는지 확인
# subway.append("정민지")
# print(subway)
# print(subway.count("정민지"))

# #정렬도 가능
# num_list = [5, 4, 3, 2, 1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# #리스트는 자료형에 구애받지 않고 사용 가능하다.
# Mix_list =["정민지", 20, True]
# print(Mix_list)

# #리스트 합치기
# num_list.extend(Mix_list)

# python = "정민지"
# print(python.index("정민지"))

# python = "정민지"
# print(python.index"민")