N,M = map(int,input().split())
basket = [0] * (N+1)  #N+1칸의 리스트 생성

for _ in range(M):
    x,y,i = map(int,input().split())
    for j in range(x,y+1):
        basket[j] = i

for i in range(1,len(basket)):
    print(basket[i],end = ' ')