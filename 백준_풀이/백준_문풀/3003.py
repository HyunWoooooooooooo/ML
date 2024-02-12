#1 1 2 2 2 8인 리스트를 만들고

std = ['1','1','2','2','2','8']
A = list(input().split())

for i in range(6):
    if int(A[i]) == int(std[i]):
        print(0,end = ' ')

    elif int(A[i]) < int(std[i]):
        print(int(std [i]) - int(A[i]), end = ' ')

    elif int(A[i]) > int(std[i]):
        print(int(std[i]) - int(A[i]), end = ' ')
