# # set = 집합,뭔가 알고리즘에서 잘 써먹을 거 같음
# #중복x, 순서x
my_set = {1,2,3,3,3}
print(my_set)  #1, 2, 3만 출력됨, 중복 허용 안하기 떄문

java = {"정민지", "정만지", "정지만"}
python = set(["정민지", "김헌우", "김우현"])

#집합의 성질을 활용해 교집합 구해보기
print(java & python)
print(java.intersection(python))

#합집합 구하기 (java or python), 역슬래쉬 활용
print(java | python)
java.union(python) #이때 정해진 순서없이 나열됨

#차집합 (자바는 하지만 파이썬은 못하는 사람들)
print(java - python)
print(java.difference(python))

#python할줄 아는 사람이 늘어났다
python.add("김우헌")
print(python)

#java를 까먹었다
java.remove("정민지")
print(java)

# java.del("정민지") #del은 인덱스가 순서대로 저장되는 경우에만 사용이 가능한데 세트는 순서가 없어서 사용 불가하다
# print(java) 
