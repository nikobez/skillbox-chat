#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Основы ООП, класс, объект, метод и атрибут
#


class Client:
    age: int
    login: str

    def show_info(self):
        print(f"Login: {self.login}, Age: {self.age}")

    def is_age_valid(self, normal=18):
        return self.age >= normal


john = Client()
john.age = 18
john.login = "john"

artur = Client()
artur.age = 20
artur.login = "Arty"

# print(john.age, artur.age)

john.show_info()
artur.show_info()

if artur.is_age_valid():
    print("OK")
