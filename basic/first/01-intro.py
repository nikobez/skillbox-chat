#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Примеры базового синтаксиса и работа с типами данных
#  Числа, строки, списки, булево значение
#

simple = 10  # int

# result = simple + 10
# result = simple - 10
# result = simple / 10
# result = simple * 10

a = 1 / 1
b = 1 // 2
c = 5 % 2

print(a, b, c)

floating_number = 5 / 2  # float

number = float(10)
print(number)
print(type(number))

name = "John"
balance = 50
price = 999

print(balance > price)  # > < >= <= == !=

print(name)
print("-" * 40)

print(name.upper())
