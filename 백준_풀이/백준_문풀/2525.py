hour, minute = map(int,input().split())
addmin = int(input())


hour = hour + (minute + addmin) // 60
minute =(minute + addmin) % 60

if hour>=24:
    hour = hour - 24

print("{0} {1}".format(hour,minute))