N,M = map(int,input().split())

basket = [0]*(N+1)  #N개 바구니 생성 

for i in range(1,N+1): #바구니에 해당 번호 공 넣기
    basket[i] = i

for _ in range(M): #공 M번 바꾸기
    i,j = map(int,input().split())
    basket[i], basket[j] = basket[j], basket[i]

basket = basket[1:]  #슬라이싱,0번 index삭제된 새로운 list가 basket에 할당
for i in range(N): #
    print(basket[i],end = ' ')