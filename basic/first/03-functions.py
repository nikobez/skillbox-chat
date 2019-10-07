#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Работа с функциями, аргументы и возвращаемое значение
#


def check_age(value):
    if value < 18:
        print("NOT OK")
    else:
        print("OK")


check_age(17)
check_age(18)
check_age(20)
check_age(10)

a = sum([1, 2, 3, 4, 5])


def say_hello(name="Guest"):
    return f"Hello, {name}"


first = say_hello("John")
second = say_hello("Artur")
third = say_hello()

print(first, second, third)
