#일반 유닛(부모 클래스)
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
       #clas Unit과 AttackUnit의 공통부분에 상속을 사용한다.
        
#공격 유닛(자식클래스)
class AttackUnit(Unit):  #괄호 열고 상속받고싶은 class명 적기
    def __init__(self, name, hp, damage):
        # self.name = name
        # self.hp = hp  요 두줄을 아래 문장으로 대체
        Unit.__init__(self,name,hp)
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
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)
        #AttakUnit, Flyable로부터 상속받은 후 초기화를 한것

#발키리: 공중 공격 유닛, 한번에 14발 미사일 발사함

valkyrie = FlyableAttackUnit("발키리",200,6,5) #name, hp, damage, flying_speed 순서
valkyrie.fly(valkyrie.name,"3시")  #Flayble 안에 있는 fly함수 호출/Flayble은 name이 없어서 
    #별도의 이름을 추가해줌