# finance_manager.py
# Система учета личных финансов с бюджетированием
# Коммит 10: Финальная версия с полной функциональностью

"""
СИСТЕМА УЧЕТА ЛИЧНЫХ ФИНАНСОВ

Комплексная система для управления личными финансами с функциями:
- Учет доходов и расходов
- Бюджетирование по категориям
- Цели сбережений
- Аналитика и отчеты
- Финансовые рекомендации

Автор: [Ваше имя]
Версия: 1.0
"""

transactions = []
balance = 0.0
categories = ['Еда', 'Транспорт', 'Развлечения', 'Здоровье', 'Одежда', 'Другое']
budgets = {}
savings_goals = []

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
            'date': '2024-01-01'
        }
        
        transactions.append(transaction)
        balance += amount
        print(f"Доход на сумму {amount:.2f} руб. добавлен!")
        
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
            print(f"Расход на сумму {amount:.2f} руб. добавлен в категорию '{category}'!")
        else:
            print("Ошибка: Неверный выбор категории!")
            
    except (ValueError, IndexError):
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_balance():
    """Показывает текущий баланс"""
    print(f"\nТекущий баланс: {balance:.2f} руб.")

# ... (все остальные функции: show_transactions, show_recent_transactions,
# show_financial_statistics, show_expenses_by_category, show_income_vs_expenses,
# set_budget, show_budget_status, check_budget_alerts, add_savings_goal,
# show_savings_goals, contribute_to_goal, show_financial_health,
# analyze_spending_patterns, generate_monthly_report, show_financial_tips)

def show_main_menu():
    """Показывает главное меню программы"""
    print("\n" + "="*50)
    print("       СИСТЕМА УЧЕТА ЛИЧНЫХ ФИНАНСОВ")
    print("="*50)
    print("1. Показать баланс")
    print("2. Добавить доход")
    print("3. Добавить расход")
    print("4. История операций")
    print("5. Финансовая статистика")
    print("6. Управление бюджетами")
    print("7. Цели сбережений")
    print("8. Анализ и отчеты")
    print("9. Финансовые советы")
    print("10. Выход")
    print("="*50)

def get_menu_choice():
    """Получает и проверяет выбор пользователя"""
    try:
        choice = int(input("\nВыберите действие (1-10): "))
        return choice
    except ValueError:
        print("Ошибка: Пожалуйста, введите число от 1 до 10!")
        return -1

def initialize_sample_data():
    """Инициализирует примеры данных для демонстрации"""
    sample_transactions = [
        {'id': 1, 'type': 'income', 'amount': 50000, 'description': 'Зарплата', 'category': 'Доход', 'date': '2024-01-01'},
        {'id': 2, 'type': 'expense', 'amount': 15000, 'description': 'Продукты', 'category': 'Еда', 'date': '2024-01-02'},
        {'id': 3, 'type': 'expense', 'amount': 5000, 'description': 'Бензин', 'category': 'Транспорт', 'date': '2024-01-02'},
        {'id': 4, 'type': 'expense', 'amount': 3000, 'description': 'Кино', 'category': 'Развлечения', 'date': '2024-01-03'}
    ]
    transactions.extend(sample_transactions)
    
    global balance
    balance = 27000  # Баланс после тестовых операций
    
    budgets['Еда'] = 20000
    budgets['Транспорт'] = 8000
    
    savings_goals.extend([
        {'id': 1, 'name': 'Новый ноутбук', 'target_amount': 80000, 'current_amount': 25000, 'created_date': '2024-01-01'}
    ])

def main():
    """Главная функция программы"""
    print("Добро пожаловать в систему учета личных финансов!")
    
    # Загружаем примеры данных (можно закомментировать)
    initialize_sample_data()
    
    # Главный цикл программы
    while True:
        show_main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            show_balance()
        elif choice == 2:
            add_income()
        elif choice == 3:
            add_expense()
        elif choice == 4:
            show_transactions()
            show_recent_transactions()
        elif choice == 5:
            show_financial_statistics()
            show_expenses_by_category()
            show_income_vs_expenses()
        elif choice == 6:
            show_budget_status()
            check_budget_alerts()
            set_budget()
        elif choice == 7:
            show_savings_goals()
            add_savings_goal()
            contribute_to_goal()
            show_financial_health()
        elif choice == 8:
            analyze_spending_patterns()
            generate_monthly_report()
        elif choice == 9:
            show_financial_tips()
        elif choice == 10:
            print("\nСпасибо за использование системы учета финансов!")
            print("До свидания!")
            break
        elif choice == -1:
            continue
        else:
            print("Ошибка: Неверный выбор! Пожалуйста, выберите от 1 до 10.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()