weather ="비"
if 조건 :      #위 조건에 만족하면 아래 실행문을 실행
    실행 명령문

weather = ""
if weather == "비":
    print("우산을 챙기세요")
elif weather == "맑음":
    print("양산을 챙기세요")
else:
    print("준비물이 필요 없어요")  #else가 굳이 없어도 된다. 없다면 만족 
                                 #조건이 없다면 아무것도 출력되지 않는다

#위 프로그램 진행 순서 > 조건을 if문과 비교하고 맞다면 바로 빠져나온다.그리고 if문 
#다음의 코드를 실행시킨다.
    
weather = "비"
if weather == "맑음":
    print("우산을 챙기세요")  #조건이 안맞기 때문에 아무것도 실행되지 않는다.


weather = input("오늘 날씨는 어때요?") #사용자의 입력을 받는 문장
#오늘 날씨는 어떄요? 라는 문장이 출력후 유저의 입력을 기다리다가 유저의 입력을 weather에 저장한다
if weather == "비":
    print("우산을 챙기세요")
elif weather == "맑음":
    print("양산을 챙기세요")
else:
    print("준비물이 필요 없어요")


weather = input("오늘 날씨는 어때요?") #사용자의 입력을 받는 문장
#오늘 날씨는 어떄요? 라는 문장이 출력후 유저의 입력을 기다리다가 유저의 입력을 weather에 저장한다
if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "맑음":
    print("양산을 챙기세요")
else:
    print("준비물이 필요 없어요")


temp = int(input("기온은 어때요?"))  #int로 감싸주는 이유 input은 문자열로 받는다, 
#하지만 보통 온도는 숫자기 때문에 문자열을 숫자로 바꿔주는 int로 감싸야 한다.
if 30<= temp:
    print("너무 덥죠")
elif 10<= temp and temp < 30 :  #10도 이상이면서 30도 미만일때만 실행문 출력
    print("날씨가 좋죠?")
elif 0 <= temp and temp < 10 :
    print("날씨가 많이 춥죠")
else :
    print("너무 추우니까 나가지 마세요")