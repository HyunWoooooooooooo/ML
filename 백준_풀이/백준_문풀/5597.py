student = [0]*31 

#과제 낸 학생들 리스트에 적용
for i in range(1,29): #28명에 대한 입력 받기
    student_o = int(input())
    student[student_o] = 1  #과제를 한 학생은 1/ 안한 학생은 0

#안한 학생 출력하기

for i in range(1,31):
    if student[i] == 0:
        print(i)

