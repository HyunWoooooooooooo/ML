#일반 유닛(부모 클래스)
class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동. [속도 {2}]".format(self.name, location, self.speed))
 
        
#공격 유닛(자식클래스)
class AttackUnit(Unit):  #괄호 열고 상속받고싶은 class명 적기
    def __init__(self, name, hp,speed,damage):
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

#날 수 있는 기능을 가진 class
class Flyable: 
    def __init__(self,flying_speed):  #나는 속도
        self.flying_speed = flying_speed

    def fly(self,name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도] : {2}"\
              .format(name, location,self.flying_speed))
        

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): 
    #날수도 잇어야 하고 공격도 가능해야함/두개의 class로부터 상속
    def __init__(self, name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #0은 지상 speed
        Flyable.__init__(self,flying_speed)
        #AttakUnit, Flyable로부터 상속받은 후 초기화를 한것

    def move(self,location):  #move를 공중 유닛에도 추가함
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        

#벌쳐: 지상유닛,기동성이 좋음
vulture = AttackUnit("벌쳐",80, 10,20)  #변수 선언

#배틀크루져: 공중유닛, 체력 굿 공격 굿
battlecruiser = FlyableAttackUnit("배틀크루져",500,25,3 )  #변수 선언

vulture.move("11시")
# battlecruiser.fly("배틀 크루져","3시")
battlecruiser.move("3시")  #move는 방향만