try:
    print("한자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    
    if num1 >=10 or num2 >=10:
        raise ValueError
    print("{0}/{1} = {2}".format(num1,num2, int(num1//num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")

    #의도적으로 두자리 숫자를 입력하면 raise ValueError를 타고 except로 내려와서 print문을
    #출력할 수 있다
    