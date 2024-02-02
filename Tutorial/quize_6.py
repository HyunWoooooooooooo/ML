def std_weight(height, gender):  #m단위
    if gender == "남자":
        return height**2*22
    else:
        return height**2*21
    

height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height/100, gender),2) #round함수 구조, 기능 파악=소주점 2자리에서 반올림, 반내림 수행
print("키 {}cm {}의 표준 체중은 {}kg입니다.".format(height, gender,weight))
