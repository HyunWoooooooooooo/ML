N = int(input())

numlist = list(map(int,input().split()))

numlist.sort()

min = numlist[0]
max = numlist[-1]

print("{0} {1}".format(min,max))