# absent =[2, 5] #결석한 학생들에게는 책을 안읽히고 온 학생들에게만 책을 읽히는 기능
# for student in range(1, 11):
#     if student in absent:
#         continue  #(그냥 건너뛰는것)
#     print("{}, 책을 일거봐".format(student))

    #해석해보자. 결석 한 학생은 2번 5번 학생이다.
    # 1번부터 10번까지 무언가를 반복해라
    # 반복 행위는 만약 학생들이 absent 변수내에 있다면 즉 결석 학생이라면
    # continue해라
    # 아니면 반복문 탈출하고 5번줄 출력하게 된다
    
absent =[2, 5] #결석한 학생들에게는 책을 안읽히고 온 학생들에게만 책을 읽히는 기능
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue  #(그냥 건너뛰는것)
    elif student in no_book: #in뒤에는 단일 숫자 못온다 그래서 nobook을 list로
        print("오늘 수업 여기까지, {}는 교무실로 따라와".format(no_book))
        break
    print("{}, 책을 읽어봐".format(student))

    #continue만나면 더이상 진행 하지 않고 다음 range로 넘어가는데 break는 만나면 바로
    #반복문을 탈출 한다.