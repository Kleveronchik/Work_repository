from decorator import Checker
try:
    checker = Checker()
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    operation = input("Select operation[/*-+]: ")
    checker.Calculate(f'{digit1}{operation}{digit2}')
except Exception as ex:
    print(ex)