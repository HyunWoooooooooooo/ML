total = int(input())
N = int(input())
sum = 0
for _ in range(N):
    a, b = map(int,input().split())
    sum = sum +(a * b)

if sum == total:
    print("Yes")
else:
    print("No")