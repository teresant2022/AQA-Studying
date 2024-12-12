def month_to_season(a):
    if a == 1 or a == 2 or a == 3:
        return ("Winter")
    if a == 3 or a == 4 or a == 5:
        return ("Spring")
    if a == 6 or a == 7 or a == 8:
        return ("Summer")
    if a == 9 or a == 10 or a == 11:
        return ("Fall")
    else:
        print("Укажите корректный номер месяца")


print(month_to_season(int(input('Введите номер месяца: '))))
