#단어에 포함된 알파벳은 처음 등장 위치 단어에 없으면 -1을 출력
S = input()

compare = 'abcdefghijklmnopqrstuvwxyz'

for i in compare:
    if i in S:
        print(S.index(i), end =' ')
    else:
        print(-1, end =' ')