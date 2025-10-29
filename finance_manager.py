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

transactions = []
balance = 10000.0  # Начальный баланс для тестирования
categories = ['Еда', 'Транспорт', 'Развлечения', 'Здоровье', 'Одежда', 'Другое']

def add_income():
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
            'date': '2024-01-01'
        }
        
        transactions.append(transaction)
        balance += amount
        print(f"Доход на сумму {amount} руб. добавлен!")
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректную сумму!")

def add_expense():
    """Добавляет расход с выбором категории"""
    global balance
    
    try:
        amount = float(input("Введите сумму расхода: "))
        description = input("Введите описание: ")
        
        if amount <= 0:
            print("Ошибка: Сумма расхода должна быть положительной!")
            return
        
        if amount > balance:
            print("Ошибка: Недостаточно средств на балансе!")
            return
        
        print("\nКатегории расходов:")
        for i, category in enumerate(categories, 1):
            print(f"   {i}. {category}")
        
        category_choice = int(input("Выберите категорию (номер): ")) - 1
        
        if 0 <= category_choice < len(categories):
            category = categories[category_choice]
            
            transaction = {
                'id': len(transactions) + 1,
                'type': 'expense',
                'amount': amount,
                'description': description,
                'category': category,
                'date': '2024-01-01'
            }
            
            transactions.append(transaction)
            balance -= amount
            print(f"Расход на сумму {amount} руб. добавлен в категорию '{category}'!")
        else:
            print("Ошибка: Неверный выбор категории!")
            
    except (ValueError, IndexError):
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_balance():
    """Показывает текущий баланс"""
    print(f"\nТекущий баланс: {balance:.2f} руб.")

def main():
    print("Добро пожаловать в систему учета личных финансов!")
    
    # Тестируем функции
    show_balance()
    add_income()
    add_expense()
    show_balance()    