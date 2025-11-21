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

def show_habit_statistics():
    """Показывает статистику по привычкам"""
    if not habits:
        print("Нет данных для статистики!")
        return
    
    total_habits = len(habits)
    active_habits = len([h for h in habits if h['current_streak'] > 0])
    total_completions = sum(h['total_completed'] for h in habits)
    total_streak_days = sum(h['current_streak'] for h in habits)
    
    print("\nСтатистика привычек:")
    print("-" * 40)
    print(f"Всего привычек: {total_habits}")
    print(f"Активных привычек: {active_habits}")
    print(f"Всего выполнено раз: {total_completions}")
    print(f"Текущих дней в сериях: {total_streak_days}")
    
    if total_habits > 0:
        success_rate = (active_habits / total_habits) * 100
        print(f"Успешность: {success_rate:.1f}%")

def show_streak_leaderboard():
    """Показывает таблицу лидеров по сериям"""
    if not habits:
        print("Нет данных для таблицы лидеров!")
        return
    
    # Сортируем по текущей серии (по убыванию)
    sorted_habits = sorted(habits, key=lambda x: x['current_streak'], reverse=True)
    
    print("\nТаблица лидеров (текущие серии):")
    print("-" * 60)
    print(f"{'Место':<6} {'Привычка':<20} {'Серия':<10} {'Лучшая серия':<15}")
    print("-" * 60)
    
    for i, habit in enumerate(sorted_habits[:10], 1):  # Только топ-10
        if habit['current_streak'] > 0:
            print(f"{i:<6} {habit['name']:<20} {habit['current_streak']:<10} {habit['longest_streak']:<15}")
    
    print("-" * 60)

def show_category_statistics():
    """Показывает статистику по категориям"""
    category_stats = {}
    
    for habit in habits:
        category = habit['category']
        if category not in category_stats:
            category_stats[category] = {
                'count': 0,
                'total_streak': 0,
                'total_completed': 0
            }
        
        category_stats[category]['count'] += 1
        category_stats[category]['total_streak'] += habit['current_streak']
        category_stats[category]['total_completed'] += habit['total_completed']
    
    if not category_stats:
        print("Нет данных по категориям!")
        return
    
    print("\nСтатистика по категориям:")
    print("-" * 50)
    print(f"{'Категория':<15} {'Привычек':<10} {'Средняя серия':<15} {'Всего выполнено':<15}")
    print("-" * 50)
    
    for category, stats in category_stats.items():
        avg_streak = stats['total_streak'] / stats['count'] if stats['count'] > 0 else 0
        print(f"{category:<15} {stats['count']:<10} {avg_streak:<15.1f} {stats['total_completed']:<15}")

def show_personal_bests():
    """Показывает личные рекорды"""
    if not habits:
        print("Нет данных о рекордах!")
        return
    
    print("\nЛичные рекорды:")
    print("-" * 50)
    
    # Самая длинная серия
    best_streak_habit = max(habits, key=lambda x: x['longest_streak'])
    print(f"Самая длинная серия: {best_streak_habit['longest_streak']} дней")
    print(f"   Привычка: {best_streak_habit['name']}")
    
    # Наиболее последовательная привычка
    if completion_history:
        habit_completions = {}
        for record in completion_history:
            habit_id = record['habit_id']
            habit_completions[habit_id] = habit_completions.get(habit_id, 0) + 1
        
        if habit_completions:
            most_consistent_id = max(habit_completions, key=habit_completions.get)
            most_consistent_habit = next(h for h in habits if h['id'] == most_consistent_id)
            print(f"\nНаиболее последовательная привычка: {most_consistent_habit['name']}")
            print(f"   Всего выполнено: {habit_completions[most_consistent_id]} раз")
    
    # Текущая самая длинная активная серия
    active_habits_with_streak = [h for h in habits if h['current_streak'] > 0]
    if active_habits_with_streak:
        current_best = max(active_habits_with_streak, key=lambda x: x['current_streak'])
        print(f"\nТекущая самая длинная активная серия: {current_best['current_streak']} дней")
        print(f"   Привычка: {current_best['name']}")

def main():
    print("Добро пожаловать в трекер привычек!")
    
    # Тестовые данные для статистики
    habits.extend([
        {'id': 1, 'name': 'Утренняя зарядка', 'description': '15 минут упражнений', 
         'category': 'Спорт', 'frequency': 'daily', 'target_count': 1,
         'current_streak': 5, 'longest_streak': 10, 'total_completed': 25,
         'created_date': '2024-01-01'},
        {'id': 2, 'name': 'Чтение книги', 'description': '30 минут чтения', 
         'category': 'Обучение', 'frequency': 'daily', 'target_count': 1,
         'current_streak': 12, 'longest_streak': 12, 'total_completed': 45,
         'created_date': '2024-01-01'},
        {'id': 3, 'name': 'Медитация', 'description': '10 минут медитации', 
         'category': 'Здоровье', 'frequency': 'daily', 'target_count': 1,
         'current_streak': 0, 'longest_streak': 7, 'total_completed': 15,
         'created_date': '2024-01-01'}
    ])
    
    # Демонстрация статистики
    show_habit_statistics()
    show_streak_leaderboard()
    show_category_statistics()
    show_personal_bests()

if __name__ == "__main__":
    main()