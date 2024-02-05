class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        #self.변수이름 == 멤버변수
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp,self.damage))



#레이스 : 공중 유닛, 비행기, 클로킹       
wraith1 = Unit("레이스",80,5)   

print("유닛이름 : {0}, 공격력 : {1},".format(wraith1.name,wraith1.damage))
#멤버변수를 class외부에서 사용한 경우


#마인드 컨트롤
wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))
    #class내부엔 clocking이라는 변수 x 외부에서 변수 선언한 경우이다.
    #하지만 wraith1.clocking의 값은 False다. wraith1에는 clocking이 없기떄문