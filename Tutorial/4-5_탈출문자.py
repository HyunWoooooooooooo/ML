print("백문이 불여일견\n백견이 불여일타")
#\n = 줄바꿈

# 저는 "나도 코딩"입니다.
# print("저는 "나도 코딩"입니다.") # 저는,입니다를 문장으로 인식함 문법 오류
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.") #탈출문자/ 여기에서 \"가 한세트이며 의미는 큰 따옴표가 문자열이 일부임을 의미함
print("저는 \'나도 코딩\'입니다.")
# \", \'는 문장내에서 따옴표를 출력한다는 의미이다. 

# \\ : 문장내에서 하나의 \로 바뀐다.
# print("C:\Users\82103\Desktop\PYTHON> ") 
# 해당 코드는 오류가 발생한다. 
# # \뒤에 n이 와서 줄바꿈도 아니고. 따옴표도 오지 않았기 때문이다. 
# 따라서 오류를 안나게 하려면 \를 두개씩 써야한다.

print("C:\\Users\\82103\\Desktop\\PYTHON> ") 

# \r :커서를 맨앞으로 이동.
print("Red Apple\rpine") #Red 의 4자리가 pine으로 대치됨 따라서 pineApple이 출력

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")