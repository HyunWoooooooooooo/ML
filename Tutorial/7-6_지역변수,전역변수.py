# gun = 10
# #전역변수:모든 코드에 영향을 미치는것이 가능한 변수
# #지역변수:블럭 내의 코드에만 영향을 미치는 것이 가능한 변수
# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총  : {}".format(gun))

# print("전체 총 : {}".format(gun)) # 10출력
# chekckpoint(2) #2명이 경계 근무를 나간다. 18출력
# print("남은 총 : {}".format(gun)) # 10출력


gun = 10
def checkpoint(soldiers):
    global gun = 20     #이 문장의 의미는 전역공간에 있는 gun을 사용하겠다는 의미이다. 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {}".format(gun))
    return gun




print("전체 총 : {}".format(gun))     #밖에 잇는 10으로 부터 값 생성함
# checkpoint(2)             #함수 내에 있는 20으로부터 값을 생성함
gun = checkpoint_return(gun,2)
print("남은 총: {}".format(gun)) #이때의 gun은 return함수의 반환값임

#전역변수를 많이 사용하면 코드 관리가 힘들어짐

