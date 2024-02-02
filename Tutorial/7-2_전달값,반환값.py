def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료 되었습니다. 잔액은 {}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: #잔액이 출금액 보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {}원 입니다.".format(balance - money))
        return balance - money  #이거 왜 하지
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다".format(balance))
        return balance
    
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission
    

balance = 0
balance = deposit(balance ,1000)  # 잔액은0 이고 입금 금액 1000을 balance에 넣는다.
balance = withdraw(balance, 2000) # 잔액 0원에 1000원을 넣었고 그 이후에 2000원을 출금하는 상황
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance,500)
#withdraw_night는 commission,balance - money - commission 이 값을 반환한다.
#그래서 commison을 commission으로 balance - money - commission 값을 balance로 재 할당하는 내용이다.
print("수수료는 {}원이며, 잔액은{}원입니다.".format(commission,balance))