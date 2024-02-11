N, M = map(int, input().split())

basket = [i for i in range(1, N+1)] #리스트 컴프리핸션?

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]  # 시작 인덱스 i부터 끝 인덱스 j까지의 바구니 선택
    temp.reverse()
    basket[i-1:j] = temp  # 선택된 바구니를 뒤집은 후 다시 할당

for i in range(N):
    print(basket[i], end=' ')  # 바구니 출력
