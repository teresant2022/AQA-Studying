def is_year_leap(year):  # setting the func to differ leap Y from regular Y
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


year = int(input("Введите год для проверки: "))  # user's input of Y

result = is_year_leap(year)  # requesting the func
if result:
    print(f"год {year}: True")
else:
    print(f"год {year}: False")
