#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Основы ООП - конструктор, наследование, перегрузка, полиморфизм, инкапсуляция
#


class Client:
    age: int
    login: str

    def show_info(self):
        print(f"Login: {self.login}, Age: {self.age}")

    def is_age_valid(self, normal=18):
        return self.age >= normal

    def __init__(self, new_login, new_age):
        self.login = new_login
        self.age = new_age


class SuperClient(Client):
    _balance: int = 100  # protected

    def show_info(self):
        super().show_info()
        print(f"Balance: {self._balance}")

    def get_balance(self):
        return self._balance

    # def show_info(self):
    #     print(f"Login: {self.login}, Age: {self.age}, Balance: {self.balance}")


user1 = Client("John", 18)
user2 = Client("Artur", 20)

user1.is_age_valid()
user1.is_age_valid(30)

user3 = SuperClient("Peter", 30)

user1.show_info()  # show_info(user1)
user3.show_info()

user3._balance
print(user3.get_balance())
