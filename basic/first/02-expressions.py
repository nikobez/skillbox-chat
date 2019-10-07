#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Условные и циклические конструкции языка
#

age = int(input("Введите ваш возвраст: "))

if age < 18:
    print("Пока")
else:
    print("Привет")

logins = ["John", "Artur"]

print(logins[0])
print(logins[1])

for temp_login in logins:
    print(temp_login)

user_login = input("Введите логин: ")

for temp_login in logins:
    if user_login == temp_login:
        print("OK")

if user_login in logins:
    print("OK")
else:
    print("NOT OK")

counter = 0

while counter < 5:
    print(counter)
    # counter = counter + 1
    counter += 1  # counter++
