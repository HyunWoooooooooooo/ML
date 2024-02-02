# def open_account():
#     print("새로운 계좌가 생성되었습니다.") #이상태로 실행해도 아무거도 실행x, 
#                                         # 함수는 정의만 하는거지 별도의 호출이 없으면 실행하지 않는다
     
def open_account():
    print("새로운 계좌가 생성되었습니다.")
    open_account()           #이렇게 까지 해줘야 출력된다.