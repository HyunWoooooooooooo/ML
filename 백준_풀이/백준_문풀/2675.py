case = int(input())

for i in range(case):
    N,S = map(str,input().split())
    N=int(N)
    for j in range(len(S)):
        print(S[j]*N,end ='')
    print()
