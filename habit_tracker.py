# habit_tracker.py
# Система учета привычек и формирования рутин
# Коммит 4: Отслеживание выполнения привычек

habits = []
categories = ['Здоровье', 'Спорт', 'Обучение', 'Работа', 'Личное', 'Другое']
completion_history = []  # История выполнения привычек

# ... (предыдущие функции add_habit, show_all_habits, show_habit_details, edit_habit)

def mark_habit_completed():
    """Отмечает привычку как выполненную на сегодня"""
    show_all_habits()
    
    try:
        habit_id = int(input("Введите ID выполненной привычки: "))
        
        for habit in habits:
            if habit['id'] == habit_id:
                # Проверяем, не выполнена ли уже сегодня
                today = '2024-01-15'  # Временная дата для демонстрации
                
                already_completed = any(
                    record['habit_id'] == habit_id and record['date'] == today 
                    for record in completion_history
                )
                
                if already_completed:
                    print(f"Привычка '{habit['name']}' уже выполнена сегодня!")
                    return
                
                # Обновляем статистику
                habit['current_streak'] += 1
                habit['total_completed'] += 1
                
                if habit['current_streak'] > habit['longest_streak']:
                    habit['longest_streak'] = habit['current_streak']
                
                # Добавляем запись в историю
                completion_record = {
                    'habit_id': habit_id,
                    'habit_name': habit['name'],
                    'date': today,
                    'timestamp': '10:00'  # Временное значение
                }
                completion_history.append(completion_record)
                
                print(f"Привычка '{habit['name']}' отмечена как выполненная!")
                print(f"Текущая серия: {habit['current_streak']} дней")
                return
        
        print(f"Ошибка: Привычка с ID {habit_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def mark_habit_missed():
    """Отмечает, что привычка была пропущена"""
    show_all_habits()
    
    try:
        habit_id = int(input("Введите ID пропущенной привычки: "))
        
        for habit in habits:
            if habit['id'] == habit_id:
                if habit['current_streak'] > 0:
                    print(f"Серия привычки '{habit['name']}' прервана на {habit['current_streak']} дней")
                    habit['current_streak'] = 0
                else:
                    print(f"Привычка '{habit['name']}' пропущена")
                return
        
        print(f"Ошибка: Привычка с ID {habit_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_today_habits():
    """Показывает привычки для выполнения сегодня"""
    if not habits:
        print("Нет привычек для отслеживания!")
        return
    
    today = '2024-01-15'
    completed_today = [
        record['habit_id'] for record in completion_history 
        if record['date'] == today
    ]
    
    print("\nПривычки на сегодня:")
    print("-" * 60)
    
    daily_habits = [h for h in habits if h['frequency'] == 'daily']
    
    for habit in daily_habits:
        status = "✅" if habit['id'] in completed_today else "⏳"
        print(f"{status} {habit['id']}. {habit['name']}")
        print(f"   Серия: {habit['current_streak']} дней | Всего: {habit['total_completed']} раз")
        print()

def show_completion_history():
    """Показывает историю выполнения привычек"""
    if not completion_history:
        print("История выполнения пуста!")
        return
    
    print("\nИстория выполнения привычек:")
    print("-" * 60)
    
    # Группируем по дате
    history_by_date = {}
    for record in completion_history:
        date = record['date']
        if date not in history_by_date:
            history_by_date[date] = []
        history_by_date[date].append(record['habit_name'])
    
    for date, habit_names in sorted(history_by_date.items(), reverse=True):
        print(f"{date}:")
        for habit_name in habit_names:
            print(f"   ✓ {habit_name}")
        print()

def main():
    print("Добро пожаловать в трекер привычек!")
    
    # Тестовые данные
    habits.extend([
        {'id': 1, 'name': 'Утренняя зарядка', 'description': '15 минут упражнений', 
         'category': 'Спорт', 'frequency': 'daily', 'target_count': 1,
         'current_streak': 5, 'longest_streak': 10, 'total_completed': 25,
         'created_date': '2024-01-01'},
        {'id': 2, 'name': 'Чтение книги', 'description': '30 минут чтения', 
         'category': 'Обучение', 'frequency': 'daily', 'target_count': 1,
         'current_streak': 12, 'longest_streak': 12, 'total_completed': 45,
         'created_date': '2024-01-01'}
    ])
    
    completion_history.extend([
        {'habit_id': 1, 'habit_name': 'Утренняя зарядка', 'date': '2024-01-14', 'timestamp': '08:00'},
        {'habit_id': 2, 'habit_name': 'Чтение книги', 'date': '2024-01-14', 'timestamp': '21:00'},
        {'habit_id': 1, 'habit_name': 'Утренняя зарядка', 'date': '2024-01-13', 'timestamp': '08:30'}
    ])
    
    # Демонстрация отслеживания
    mark_habit_completed()
    mark_habit_missed()
    show_today_habits()
    show_completion_history()

if __name__ == "__main__":
    main()