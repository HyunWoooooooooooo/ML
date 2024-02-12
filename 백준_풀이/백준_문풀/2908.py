# 숫자 두개를 입력받는다. 정수는 뒤집을수 없으니까 문자열로 받은 후 뒤집고 뒤집은
# 걸 int로 비교한다. 뒤집는건 어떤식으로 뒤집을까 .reverse를 활용하자.

A,B = map(str,input().split())

reverseA = ''.join(reversed(A))
reverseB = ''.join(reversed(B))

if reverseA > reverseB:
    print(reverseA)
else:
    print(reverseB)