#10개 입력받고 나머지 구한뒤 서로 다른 나머지가 몇개인지.
num = []
for i in range(10):
    A = int(input())
    if A%42 not in num:
        num.append(A%42)
print(len(num))
