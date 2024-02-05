class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):  # Unit생성자 출력
class FlyableUnit(Flyable, Unit):  #Flayble생성자 출력
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit() #먼저 상속받는 Unit class가 출력됨


