sum = 0
num = input()
for i in range(len(num)):
    if num[i] in ['A' , 'B' , 'C']:
        sum = sum + 3
    elif num[i] in ['D' , 'E' , 'F']:
        sum = sum + 4
    elif num[i] in ['G' , 'H' , 'I']:
        sum = sum + 5
    elif num[i] in ['J' , 'K' , 'L']:
        sum = sum + 6
    elif num[i] in ['M' , 'N' , 'O']:
        sum = sum + 7
    elif num[i] in ['P' , 'Q' , 'R' , 'S']:
        sum = sum + 8
    elif num[i] in [ 'T' , 'U' , 'V']:
        sum = sum + 9
    elif num[i] in ['W' , 'X' , 'Y' , 'Z']:
        sum = sum + 10


print(sum)