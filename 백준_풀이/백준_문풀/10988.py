#순행 방향과 역행 방향이 같으면 펠린드롬이다.
A=input()
if A == str(reversed(A)):
    print(1)
else:
    print(0)