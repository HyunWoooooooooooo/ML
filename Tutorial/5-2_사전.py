# # #사전에서는 키에 대한 중복 안된다,
# cabinet = {3: "유재석", 100: "조세호"}  #key : "value"
# print(cabinet[3]) #key값을 넣어주면 된다.
# print(cabinet[100])   #사전에서 값을 가져오는 방식은 두가지가 있다. 1= [] 2= .get()

# print(cabinet.get(3))
# # print(cabinet[5]) #지정되지 않은 key값은 오류나고 프로그램 종료 (index와 같다)


# print(cabinet.get(5)) #find와 같다 none 출력하고 프로그램 계속 작동
# print("hi")

# none대신에 다른 값을 쓰고 싶다
# print(cabinet.get(5, "값 없음"))

# 사전 자료형 안에 특정 정보가 있는지 없는지 판단 하는 코드 가능
# print(3 in cabinet) #있다면 True, 없다면 False
# print(5 in cabinet) 

# cabinet = {"A-3": "유재석", "B-3" : "조세호"}
# print(cabinet["A-3"])
# print(cabinet["B-3"])

# #새 손님
# cabinet["A-3"] = "김종국" #유재석 빠지고 김종국 들어감 중복 x니까
# cabinet ["c-20"] = "정만지"  #cabinet에 c-20이라는 키를 만들고 그 키를 정만지에게 준다
# print(cabinet)  #이때 따옴표를 안쓰는 이유는 쓰면 그냥 문자열로 인식하고 cabinet출력해버려서

# #손님 갔다.
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())

# #value만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)