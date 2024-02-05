#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
       #clas Unit과 AttackUnit의 공통부분에 상속을 사용한다.
        
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


#파이어뱃 : 공격 유닛
firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")

#공격 두번 받았다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

