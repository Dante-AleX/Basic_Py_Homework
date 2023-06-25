# Программа банкомата

transaction_history = []

def display_menu():
    print("1. Проверить баланс")
    print("2. Снять деньги")
    print("3. Внести деньги")
    print("4. Посмотреть историю операций")
    print("5. Выйти")

def check_balance(balance):
    print("Ваш текущий баланс:", balance)
    print()

def withdraw(balance, amount):
    if amount > balance:
        print("Недостаточно средств на счете")
        print()
    else:
        balance -= amount
        transaction_history.append(f"Снятие: {amount}")
        print("Сумма", amount, "снята со счета")
        print()
    return balance

def deposit(balance, amount):
    balance += amount
    transaction_history.append(f"Пополнение: {amount}")
    print("Сумма", amount, "пополнена на счет")
    print()
    return balance

def show_transaction_history():
    if not transaction_history:
        print("История операций пуста")
        print()
    else:
        print("История операций:")
        for transaction in transaction_history:
            print(transaction)
            print()

def main():
    balance = 0

    while True:
        display_menu()
        choice = input("Выберите операцию (1-5): ")

        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            amount = float(input("Введите сумму для снятия: "))
            balance = withdraw(balance, amount)
        elif choice == '3':
            amount = float(input("Введите сумму для внесения: "))
            balance = deposit(balance, amount)
        elif choice == '4':
            show_transaction_history()
        elif choice == '5':
            print("Сеанс работы с банкоматом завершен")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
            print()

if __name__ == "__main__":
    main()
