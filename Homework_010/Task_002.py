# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.


class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def display_menu(self):
        print("1. Проверить баланс")
        print("2. Снять деньги")
        print("3. Внести деньги")
        print("4. Посмотреть историю операций")
        print("5. Выйти")

    def check_balance(self):
        print("Ваш текущий баланс:", self.balance)
        print()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете")
            print()
        else:
            self.balance -= amount
            self.transaction_history.append(f"Снятие: {amount}")
            print("Сумма", amount, "снята со счета")
            print()

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Пополнение: {amount}")
        print("Сумма", amount, "пополнена на счет")
        print()

    def show_transaction_history(self):
        if not self.transaction_history:
            print("История операций пуста")
            print()
        else:
            print("История операций:")
            for transaction in self.transaction_history:
                print(transaction)
            print()

    def main(self):
        while True:
            self.display_menu()
            choice = input("Выберите операцию (1-5): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Введите сумму для снятия: "))
                self.withdraw(amount)
            elif choice == '3':
                amount = float(input("Введите сумму для внесения: "))
                self.deposit(amount)
            elif choice == '4':
                self.show_transaction_history()
            elif choice == '5':
                print("Сеанс работы с банкоматом завершен")
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")
                print()


if __name__ == "__main__":
    atm = ATM()
    atm.main()
