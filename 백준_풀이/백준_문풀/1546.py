N = int(input())
score =[]

score = list(map(int,input().split()))  #list로 감싸기 주의

std = max(score)
for i in range(N):
    score[i] = (score[i] / std) *100

temp = 0
for i in range(N):
    temp += score[i]

totalscroe = temp/N
print(totalscroe)
