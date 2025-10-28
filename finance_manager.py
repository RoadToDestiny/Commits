# finance_manager.py
# Система учета личных финансов с бюджетированием
# Коммит 1: Базовая структура проекта

def main():
    print("Добро пожаловать в систему учета личных финансов!")
    print("Система находится в разработке...")

if __name__ == "__main__":
    main()

# Глобальные переменные для хранения данных
transactions = []
balance = 0.0
categories = ['Еда', 'Транспорт', 'Развлечения', 'Здоровье', 'Одежда', 'Другое']

def add_income():
    """Добавляет доход"""
    global balance
    
    try:
        amount = float(input("Введите сумму дохода: "))
        description = input("Введите описание: ")
        
        if amount <= 0:
            print("Ошибка: Сумма дохода должна быть положительной!")
            return
        
        transaction = {
            'id': len(transactions) + 1,
            'type': 'income',
            'amount': amount,
            'description': description,
            'category': 'Доход',
            'date': '2024-01-01'  # Временная дата
        }
        
        transactions.append(transaction)
        balance += amount
        print(f"Доход на сумму {amount} руб. добавлен!")
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректную сумму!")

def main():
    print("Добро пожаловать в систему учета личных финансов!")
    
    # Тестируем добавление дохода
    add_income()
    print(f"Текущий баланс: {balance} руб.")
    print(f"Всего операций: {len(transactions)}")