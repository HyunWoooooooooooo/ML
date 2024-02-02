def profile(name, age, main_lang):
    print("이름: {} \t나이: {} \t주 사용언어:{}"\
          .format(name, age, main_lang)) #역슬러쉬 enter는 줄바꿈이다. 코드가 너무 긴 경우에 사용
    
profile("유재석", 20 , "파이썬")
profile("조세호", 14 , "자바")

#그런데 만약 얘들이 고등학교 같은 반이라면 나이를 별도 지정할 이유 x 같기 떄문
#예를 들어 같은 학교 같은 학년 같은 반 같은 수업을 듣는다 가정


def profile(name, age=17, main_lang="파이썬"):
    print("이름: {} \t나이: {} \t주 사용언어:{}"\
          .format(name, age, main_lang))
#age, main_lang에 대한 별도의 입력을 안받으면 기본값을 출력함

profile("유재석")
profile("조세호")