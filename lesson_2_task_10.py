# Bank app.
# User puts on account X roubles for Y years with 10% annual interest rate.
# The money on account will be multiplied next year by the interest rate.
# Task: code a func which accepts X, Y arguements and$
# return a sum that the client shall have after Y years.

def account_calculation(X, Y):
    for _ in range(Y):
        X *= 1.1
    return round(X, 2)


intial_account_deposit = float(input("Введите сумму первоначального вклада: "))

years = int(input("Введите срок для вклада: "))

final_amount = account_calculation(intial_account_deposit, years)

print(f"Сумма на вкладе после {years} лет: {final_amount} рублей")
