python = "python is Amazing"
print(python.lower()) #lower=전부 소문자로 출력하는 함수
print(python.upper()) #upper=전부 대문자로 출력
print(python[0].isupper()) #변수python의 첫번째 값이 대문자 인가
print(len(python)) #빈칸도 count, 글자 갯수 count
print(python.replace("python", "java")) #python을 찾은 뒤에 java로 바꿔서 출력함

index = python.index("n") #변수 python에서 n의 위치를 찾고 출력해라
print(index)

index = python.index("n", index + 1)# python에서 n의 위치를 찾는데 전에 찾은 자리 이후부터 찾고 출력해라
print(index)

print(python.find("n"))
print(python.find("Java")) #python안에 java가 없기때문에 -1을 출력


#find와 index 차이점

python = "python is Amazing"
print(python.index("java"))
print("hi") #index쓰면 error뜨면서 프로그램 종료된다. 때문에 hi출력 x

python = "python is Amazing"
print(python.find("java"))
print("hi") # java를 찾지 못해도 프로그램 종료하지 않고 계속 진행한다.


print(python.count("n")) #python에서 n이 총 몇번 등장하는지 숫자 count