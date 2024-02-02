# 출석번호가 1,2,3,4앞에 100을 붙이기로 함->101,102...

students = [1, 2, 3, 4, 5]
students = [i + 100 for i in students]
#i 에다가 100을 더한 값을 students에 넣을건데 i는 students 안에 있다,/오른쪽에서 왼쪽으로 가는 순서
print(students)

# 학생들 이름을 길이로 변환
students = ["iron man","Thor","groot"]
students = len(students())  #len은 하나의 길이만 받을수있다 즉 리스트는 못받는다,=.
print(students)


students = ["iron man","Thor","groot"]
students = [len(i) for i in students]  #이렇게만 가능한게 len은 하나씩만 받을수 있다,그래서 리스트에서하나씩 받아오는 for문이 필요하다,
print(students)

#학생 이름을 대문자로 바꾸자
students = ["iron man","Thor","groot"]
students = [i.upper() for i in students]
print(students)
#students에 있는 정보를 하나씩 i에 넣고 그 i를 대문자로 만든후 students에 저장 이걸 반복
