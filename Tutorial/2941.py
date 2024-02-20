word = input()

i = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for j in i:
    word = word.replace(j, '*')


print(len(word))