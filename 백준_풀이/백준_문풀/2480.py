a,b,c = map(int, input().split())

if a==b==c:
    print("{}".format(10000+a*1000))
elif a==b:
    print("{}".format(1000+a*100))
elif b==c:
    print("{}".format(1000+b*100))
elif c==a:
    print("{}".format(1000+c*100))
else:
    if a> b and a> c:
        print("{}".format(a*100))
    elif b>c and b>a:
        print("{}".format(b*100))
    else:
        print("{}".format(c*100))



