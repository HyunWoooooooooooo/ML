menu = {"커피", "우유", "주스"} #>>중괄호니까 세트 표현이다 그래서 결과값 보면 순서가 정해지지 않았다.
print(menu)  #소괄호까지 출력되는 이유: 세트 포현은 중괄호를 포함한다. 세트의 시작과 세트의 끝을 의미한다.

print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu)) # 세트 = 중괄호, 리스트= 대괄호, 튜플 = 소괄호

menu = set(menu)
print(menu, type(menu))