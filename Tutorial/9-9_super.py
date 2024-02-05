#일반 유닛
class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0}이 {1} 방향으로 이동. [속도: {2}]"\
              .format(self.name, location, self.speed))
       #clas Unit과 AttackUnit의 공통부분에 상속을 사용한다.
        
class AttackUnit(Unit):  #괄호 열고 상속받고싶은 class명 적기
    def __init__(self, name, hp,speed, damage):
        # self.name = name
        # self.hp = hp  요 두줄을 아래 문장으로 대체
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0}: {1}방향으로 적군 공격 중. 공격력 {2}\
            ".format(self.name, location, self.damage))
        
        #name은 멤버변수의 값을 출력하고 location은 전달받은 값을 사용한다.

    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 채력은 {1}입니다.".format(self.name,self.hp))

        if self.hp <= 0:
            print("{0}: 파괴되었습니다".format(self.name))

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0}이 {1}방향으로 날아값니다.[속도 : {2}]"\
              .format(name,location,self.flying_speed))
        

#공중공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,0,hp,damage) #지상speed = 0
        Flyable.__init__(self,flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)


#벌쳐
vulture = AttackUnit("벌쳐",80, 10, 20)

#배틀 크루져
battlecruiser = FlyableAttackUnit("배틀크루져", 500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
#이러한 경우의 문제가 뭐냐 지상은 move함수 
#공중은 fly함수 즉 변수가 공중,지상인지를 확인해야함>메소드 오버라이등을 통해 move만으로 해결 가능하도록 만들자
#50번 줄을 통해 FlyAttack에도 move함수 추가해주기

battlecruiser.move("9시")

#건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
       # 방법1 :Unit.__init__(self, name, hp, 0)#건물 speed = 0
        super().__init__(name,hp,0) #방법2 /self,빼주기
        self.location = location