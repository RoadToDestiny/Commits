# finance_tracker.py
# Персональный помощник для учета финансов
# Коммит 10: Финальная версия с улучшениями и документацией

"""
ПЕРСОНАЛЬНЫЙ ФИНАНСОВЫЙ ПОМОЩНИК

Это консольное приложение для учета личных финансов.
Функциональность:
- Учет доходов и расходов
- Просмотр истории операций  
- Финансовый анализ
- Очистка истории

Автор: [Ваше имя]
Версия: 1.0
"""

# Глобальные переменные для хранения данных
BALANCE = 0.0
HISTORY = []

def show_balance():
    """Показывает текущий баланс пользователя"""
    print(f"\n=== Ваш текущий баланс: {BALANCE:.2f} руб. ===")

def add_income():
    """Добавляет доход к балансу"""
    global BALANCE, HISTORY
    try:
        amount = float(input("Введите сумму дохода: "))
        if amount <= 0:
            print("Ошибка: Сумма дохода должна быть положительной!")
            return
        BALANCE += amount
        HISTORY.append(f"Доход: +{amount:.2f} руб.")
        print(f"✅ Доход в размере {amount:.2f} руб. успешно добавлен!")
    except ValueError:
        print("Ошибка! Пожалуйста, введите числовое значение.")

def add_expense():
    """Добавляет расход к балансу"""
    global BALANCE, HISTORY
    try:
        amount = float(input("Введите сумму расхода: "))
        if amount <= 0:
            print("Ошибка: Сумма расхода должна быть положительной!")
            return
        if amount > BALANCE:
            print("Ошибка: Недостаточно средств на балансе!")
            return
        BALANCE -= amount
        HISTORY.append(f"Расход: -{amount:.2f} руб.")
        print(f"✅ Расход в размере {amount:.2f} руб. успешно добавлен!")
    except ValueError:
        print("Ошибка! Пожалуйста, введите числовое значение.")

def show_history():
    """Показывает всю историю финансовых операций"""
    print("\n=== История операций ===")
    if not HISTORY:
        print("История операций пуста.")
    else:
        for i, operation in enumerate(HISTORY, 1):
            print(f"{i}. {operation}")
    print("=======================")

def clear_history():
    """Очищает всю историю операций"""
    global HISTORY
    confirm = input("Вы уверены, что хотите очистить историю? (да/нет): ")
    if confirm.lower() == 'да':
        HISTORY.clear()
        print("История операций очищена!")
    else:
        print("Очистка истории отменена.")

def show_financial_analysis():
    """Показывает простой финансовый анализ"""
    if not HISTORY:
        print("Недостаточно данных для анализа.")
        return
    
    total_income = 0
    total_expenses = 0
    
    for operation in HISTORY:
        if operation.startswith("Доход:"):
            amount_str = operation.split("+")[1].split(" ")[0]
            total_income += float(amount_str)
        elif operation.startswith("Расход:"):
            amount_str = operation.split("-")[1].split(" ")[0]
            total_expenses += float(amount_str)
    
    print("\n=== Финансовый анализ ===")
    print(f"Всего доходов: {total_income:.2f} руб.")
    print(f"Всего расходов: {total_expenses:.2f} руб.")
    print(f"Чистая прибыль: {total_income - total_expenses:.2f} руб.")
    
    if total_income > 0:
        expense_percentage = (total_expenses / total_income) * 100
        print(f"Расходы составляют {expense_percentage:.1f}% от доходов")
    
    print("=========================")

def show_menu():
    """Отображает главное меню программы"""
    print("\n" + "="*50)
    print("        ПЕРСОНАЛЬНЫЙ ФИНАНСОВЫЙ ПОМОЩНИК")
    print("="*50)
    print("1. Показать баланс")
    print("2. Добавить доход")
    print("3. Добавить расход")
    print("4. Показать историю операций")
    print("5. Очистить историю")
    print("6. Финансовый анализ")
    print("7. Выход")
    print("="*50)

def get_user_choice():
    """Запрашивает и проверяет выбор пользователя"""
    try:
        choice = int(input("\nВыберите действие (1-7): "))
        return choice
    except ValueError:
        print("Ошибка! Пожалуйста, введите число от 1 до 7.")
        return -1

def initialize_sample_data():
    """Инициализирует пример начальных данных"""
    global BALANCE, HISTORY
    sample_operations = [
        ("Доход: +5000.00 руб.", 5000),
        ("Расход: -1500.00 руб.", -1500),
        ("Доход: +3000.00 руб.", 3000),
        ("Расход: -800.00 руб.", -800)
    ]
    for operation, amount in sample_operations:
        HISTORY.append(operation)
        BALANCE += amount
    print("Загружены примеры данных для демонстрации.")

def main():
    """Главная функция программы"""
    print("Добро пожаловать в персональный финансовый помощник!")
    
    # Раскомментируйте следующую строку для загрузки тестовых данных
    # initialize_sample_data()
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 1:
            show_balance()
        elif choice == 2:
            add_income()
        elif choice == 3:
            add_expense()
        elif choice == 4:
            show_history()
        elif choice == 5:
            clear_history()
        elif choice == 6:
            show_financial_analysis()
        elif choice == 7:
            print("\n Спасибо за использование финансового помощника!")
            print("До свидания!")
            break
        elif choice == -1:
            continue
        else:
            print("Неверный выбор! Пожалуйста, выберите действие от 1 до 7.")
        
        input("\n Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()