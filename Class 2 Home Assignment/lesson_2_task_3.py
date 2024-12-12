import math


def square_area(side):  # set the func to calc the square area
    return side * side


square_side = float(input("Введите сторону квадрата: "))  # user unput

result = square_area(square_side)  # getting result

rounded_result = math.ceil(result)  # roundung the result

if result:
    print(f"Площадь квадрата: {result}")  # printing the result
