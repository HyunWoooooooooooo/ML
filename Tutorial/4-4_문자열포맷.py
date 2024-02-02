print("a" + "b")
print("a","b")

# 방법1
print("나는 %d살입니다." % 20) #d=정수를 의미
print("나는 %s을 좋아해요." %"파이썬") #문자열(string)의 약자 s
print("Apple은 %c로 시작해요." %"A") #c는 케릭터라서 한글자만 받겠다를 의미

print("나는 %s살 입니다." %20)

print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간") )

# 방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간") )
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간") )
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간") )

# 방법3{color
print("나는 {age}살 이며, {color}색을 좋아해요".format(age = 20, color = "빨강"))

# 방법4
age = 20
color = "빨간"
print(f"나는 {age}이며, {color}색을 좋아해요.")