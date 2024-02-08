from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}이 생성 되었습니다".format(name))

    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0}이 {1} 방향으로 이동. [속도: {2}]"\
              .format(self.name, location, self.speed))
      
        
    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 채력은 {1}입니다.".format(self.name,self.hp))

        if self.hp <= 0:
            print("{0}: 파괴되었습니다".format(self.name))


#공격 유닛        
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

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    #스팀팩 : 일정시간동안이동, 공격 속도 증가, 체력 10감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 스팀팩 사용 못합니다".fort(self.name))
#탱크
class tank(AttackUnit):
    #시즈모드: 탱크를 지상에 고정, 더 높은 파워로 공격, 이동불가
    seize_developed = False #시즈모두 개발 여부

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return     #아무것도 안하고 나간다.   
        
        #시즈모드가 아닐때 ->시즈모드로 변경
        if self.seize_developed == False:
            print("{0}:시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_developed = True

            #시즈모드 일때 ->시즈모드 해제
        else:
            print("{0}:시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode = False
    
        

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

#레이스
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False #클로킹 모드 해체 상태

    def clocking(self):
        if self. clocked == True: #클로킹 코드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else: #클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")  

def game_over():
    print("player : gg")         
    print("[player] 님이 게임에서 퇴장하셨습니다.")

# 모든 클래스 정의


#게임 시작
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성
t1 = tank()
t2 = tank()

#레이스 1기 생성
w1 = wraith()

#유닛 일괄 관리
attack_units = [] #리스트 생성
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

#공격모드 준비(마린 : 스탬팩 / 탱크:시즈모드 / 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):  #isinstance는 지금 만들어진 객체가 class의 인스턴스인지 확인하는 기능
 #만약 unit이 Marine class의 인스턴스라면
        unit.stimpack()
    elif isinstance(unit, tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 5~20사이의 공격 받음

#게임 종료
game_over()
