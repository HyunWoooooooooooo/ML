name = '룽지'
animal = '강아지'   # 1번 줄과 2번줄은 문자열이라서 '' 사용
age = 4            # 3번줄은 숫자열이라서 ''사용x
hobby = '산책'
is_adult = age >= 3 #어른 이기 위해서는 3살 이상이여야 한다. 


print('민지집', animal ,'의 이름은', name ,'이예요')
# 문장을 쉼표로 연결해주면 정수형을 str로 감싸서 문자열로 바꿔주는 과정 생략 가능하다.
print( name , '는' , age , '살이며,' , hobby , '을 아주 좋아해요') 
print( name ,"어른일까요?" ,is_adult)
