# finance_tracker.py
# Персональный помощник для учета финансов

BALANCE = 1000.0
HISTORY = []

def show_balance():
    print(f"\n=== Ваш текущий баланс: {BALANCE:.2f} руб. ===")

def add_income():
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










def main():
    print("Добро пожаловать в персональный финансовый помощник!")
    
    # Добавляем тестовые данные
    HISTORY.append("Доход: +5000.00 руб.")
    HISTORY.append("Расход: -1500.00 руб.")
    
    # Тестируем новые функции
    show_history()
    show_balance()

if __name__ == "__main__":
    main()