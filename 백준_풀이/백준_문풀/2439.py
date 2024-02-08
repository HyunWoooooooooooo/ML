import sys
N = int(sys.stdin.readline())

for i in range(1,N+1):
    print("{0:>{1}}".format("*"*i,N))
    # print("{0:_>{1}}".format("*"*i,N))
