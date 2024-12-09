list = []  # made a list

for i in range(1, 101):  # set a cond for range from 1 to 101
    if i % 15 == 0:
        list.append("FizzBuzz")
    elif i % 3 == 0:
        list.append('Fizz')
    elif i % 5 == 0:
        list.append('Buzz')
    else: list.append(i)  # the last cond for the rest of numbers

print(list)  # printing the result
