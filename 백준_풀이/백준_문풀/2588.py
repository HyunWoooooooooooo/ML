num1 = int(input())

midnum = int(input())
a= midnum//100
b= (midnum%100)//10
c = (midnum%100)%10

print(num1*c)
print(num1*b)
print(num1*a)
print((num1*c) + (num1*b*10) +(num1*a*100))
################################################

A = int(input())
B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))

