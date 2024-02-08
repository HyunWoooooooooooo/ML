class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    
    if num1 >=10 or num2 >=10:
        raise BigNumberError("입력값 : {0},{1}".format(num1, num2))
    print("{0}/{1} = {2}".format(num1,num2, int(num1//num2)))
except ValueError: #사실상 의미 없음
    print("잘못된 값을 입력하였습니다.")
except BigNumberError as err: #BigNumberError를 타고 except로 내려옴
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")
    print(err)

finally:
    print("게산기를 이용해주셔서 감사합니다.") #계산기가 정상 or비정상 일때 모두 실행됨