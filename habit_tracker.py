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

def add_goal():
    """Добавляет цель для привычки"""
    show_all_habits()
    
    try:
        habit_id = int(input("Введите ID привычки: "))
        target_streak = int(input("Введите целевое количество дней (серия): "))
        description = input("Введите описание цели: ")
        
        if target_streak <= 0:
            print("Ошибка: Целевое количество дней должно быть положительным!")
            return
        
        for habit in habits:
            if habit['id'] == habit_id:
                goal = {
                    'id': len(goals) + 1,
                    'habit_id': habit_id,
                    'habit_name': habit['name'],
                    'target_streak': target_streak,
                    'description': description,
                    'completed': False,
                    'current_progress': habit['current_streak'],
                    'created_date': '2024-01-01'
                }
                goals.append(goal)
                print(f"Цель для привычки '{habit['name']}' добавлена!")
                return
        
        print(f"Ошибка: Привычка с ID {habit_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_goals():
    """Показывает все цели"""
    if not goals:
        print("Нет активных целей!")
        return
    
    active_goals = [g for g in goals if not g['completed']]
    completed_goals = [g for g in goals if g['completed']]
    
    if active_goals:
        print("\nАктивные цели:")
        print("-" * 60)
        for goal in active_goals:
            progress_percent = (goal['current_progress'] / goal['target_streak']) * 100
            remaining = goal['target_streak'] - goal['current_progress']
            
            print(f"{goal['id']}. Привычка: {goal['habit_name']}")
            print(f"   Цель: {goal['description']}")
            print(f"   Прогресс: {goal['current_progress']}/{goal['target_streak']} дней")
            print(f"   Осталось: {remaining} дней | {progress_percent:.1f}%")
            print()
    
    if completed_goals:
        print("\nЗавершенные цели:")
        for goal in completed_goals:
            print(f"{goal['id']}. ✓ {goal['habit_name']} - {goal['description']}")

def check_goal_progress():
    """Проверяет и обновляет прогресс целей"""
    updated_goals = []
    
    for goal in goals:
        if not goal['completed']:
            # Находим текущую привычку
            for habit in habits:
                if habit['id'] == goal['habit_id']:
                    goal['current_progress'] = habit['current_streak']
                    
                    # Проверяем, достигнута ли цель
                    if habit['current_streak'] >= goal['target_streak']:
                        goal['completed'] = True
                        print(f"🎉 Поздравляем! Цель достигнута: {goal['description']}")
                        print(f"   Привычка: {goal['habit_name']}")
                        print(f"   Серия: {habit['current_streak']} дней")
                    
                    updated_goals.append(goal)
                    break
    
    if not updated_goals:
        print("Нет активных целей для проверки!")

def add_reward():
    """Добавляет награду за достижение цели"""
    reward_name = input("Введите название награды: ")
    description = input("Введите описание награды: ")
    
    if reward_name.strip():
        reward = {
            'id': len(rewards) + 1,
            'name': reward_name,
            'description': description,
            'unlocked': False,
            'unlock_date': None
        }
        rewards.append(reward)
        print(f"Награда '{reward_name}' добавлена!")
    else:
        print("Ошибка: Название награды не может быть пустым!")

def unlock_reward():
    """Разблокирует награду"""
    if not rewards:
        print("Нет доступных наград!")
        return
    
    locked_rewards = [r for r in rewards if not r['unlocked']]
    
    if not locked_rewards:
        print("Все награды уже разблокированы!")
        return
    
    print("\nДоступные для разблокировки награды:")
    for reward in locked_rewards:
        print(f"{reward['id']}. {reward['name']} - {reward['description']}")
    
    try:
        reward_id = int(input("Введите ID награды для разблокировки: "))
        
        for reward in rewards:
            if reward['id'] == reward_id and not reward['unlocked']:
                reward['unlocked'] = True
                reward['unlock_date'] = '2024-01-15'
                print(f"🎊 Награда '{reward['name']}' разблокирована!")
                return
        
        print(f"Ошибка: Награда с ID {reward_id} не найдена или уже разблокирована!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_rewards():
    """Показывает все награды"""
    if not rewards:
        print("Нет наград!")
        return
    
    unlocked_rewards = [r for r in rewards if r['unlocked']]
    locked_rewards = [r for r in rewards if not r['unlocked']]
    
    if unlocked_rewards:
        print("\nРазблокированные награды:")
        for reward in unlocked_rewards:
            print(f"🏆 {reward['name']} - {reward['description']}")
            print(f"   Получена: {reward['unlock_date']}")
            print()
    
    if locked_rewards:
        print("\nЗаблокированные награды:")
        for reward in locked_rewards:
            print(f"🔒 {reward['name']} - {reward['description']}")

def main():
    print("Добро пожаловать в трекер привычек!")
    
    # Тестовые данные
    habits.extend([
        {'id': 1, 'name': 'Утренняя зарядка', 'description': '15 минут упражнений', 
         'category': 'Спорт', 'frequency': 'daily', 'target_count': 1,
         'current_streak': 5, 'longest_streak': 10, 'total_completed': 25,
         'created_date': '2024-01-01'}
    ])
    
    # Демонстрация системы целей и наград
    add_goal()
    add_reward()
    show_goals()
    check_goal_progress()
    unlock_reward()
    show_rewards()

def create_routine():
    """Создает рутину из нескольких привычек"""
    routine_name = input("Введите название рутины: ")
    
    if not routine_name.strip():
        print("Ошибка: Название рутины не может быть пустым!")
        return
    
    show_all_habits()
    print("\nДобавьте привычки в рутину (введите ID через запятую):")
    habit_ids_input = input("ID привычек: ")
    
    try:
        habit_ids = [int(id_str.strip()) for id_str in habit_ids_input.split(',')]
        routine_habits = []
        
        for habit_id in habit_ids:
            for habit in habits:
                if habit['id'] == habit_id:
                    routine_habits.append({
                        'id': habit['id'],
                        'name': habit['name']
                    })
                    break
        
        if routine_habits:
            routine = {
                'id': len(routines) + 1,
                'name': routine_name,
                'habits': routine_habits,
                'time_of_day': 'morning',  # morning, afternoon, evening, custom
                'estimated_time': len(routine_habits) * 15,  # минут
                'enabled': True
            }
            routines.append(routine)
            print(f"Рутина '{routine_name}' создана!")
            print(f"Привычек в рутине: {len(routine_habits)}")
            print(f"Примерное время: {routine['estimated_time']} минут")
        else:
            print("Ошибка: Не удалось найти указанные привычки!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные ID!")

def show_routines():
    """Показывает все рутины"""
    if not routines:
        print("Нет созданных рутин!")
        return
    
    print("\nВсе рутины:")
    print("-" * 60)
    
    for routine in routines:
        status = "✅ ВКЛ" if routine['enabled'] else "❌ ВЫКЛ"
        print(f"{routine['id']}. {routine['name']} [{status}]")
        print(f"   Время: {routine['time_of_day']} | Приблизительно: {routine['estimated_time']} мин")
        print(f"   Привычки: {', '.join([h['name'] for h in routine['habits']])}")
        print()

def execute_routine():
    """Выполняет рутину"""
    show_routines()
    
    try:
        routine_id = int(input("Введите ID рутины для выполнения: "))
        
        for routine in routines:
            if routine['id'] == routine_id:
                if not routine['enabled']:
                    print(f"Рутина '{routine['name']}' отключена!")
                    return
                
                print(f"\nВыполнение рутины: {routine['name']}")
                print("-" * 40)
                
                completed_count = 0
                for habit_info in routine['habits']:
                    response = input(f"Выполнить '{habit_info['name']}'? (y/n): ").lower()
                    if response == 'y':
                        # Находим и отмечаем привычку
                        for habit in habits:
                            if habit['id'] == habit_info['id']:
                                habit['current_streak'] += 1
                                habit['total_completed'] += 1
                                completed_count += 1
                                break
                
                print(f"\nРутина выполнена! Завершено привычек: {completed_count}/{len(routine['habits'])}")
                return
        
        print(f"Ошибка: Рутина с ID {routine_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def add_reminder():
    """Добавляет напоминание для привычки"""
    show_all_habits()
    
    try:
        habit_id = int(input("Введите ID привычки: "))
        reminder_time = input("Время напоминания (например, 08:00): ")
        days = input("Дни недели (например, пн,вт,ср или 'daily'): ")
        
        for habit in habits:
            if habit['id'] == habit_id:
                reminder = {
                    'id': len(reminders) + 1,
                    'habit_id': habit_id,
                    'habit_name': habit['name'],
                    'time': reminder_time,
                    'days': days,
                    'enabled': True
                }
                reminders.append(reminder)
                print(f"Напоминание для '{habit['name']}' добавлено на {reminder_time}")
                return
        
        print(f"Ошибка: Привычка с ID {habit_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_todays_schedule():
    """Показывает расписание на сегодня"""
    if not habits and not routines:
        print("Нет активных привычек и рутин!")
        return
    
    print("\nРасписание на сегодня:")
    print("=" * 50)
    
    # Утренние привычки
    morning_habits = [h for h in habits if any(
        r['habit_id'] == h['id'] and r['time'].startswith('0') or r['time'].startswith('1') 
        for r in reminders if r['enabled']
    )]
    
    if morning_habits:
        print("\n🌅 Утро:")
        for habit in morning_habits:
            # Находим время напоминания
            habit_reminders = [r for r in reminders if r['habit_id'] == habit['id'] and r['enabled']]
            if habit_reminders:
                times = ', '.join([r['time'] for r in habit_reminders])
                print(f"   ⏰ {times} - {habit['name']}")
    
    # Дневные рутины
    day_routines = [r for r in routines if r['time_of_day'] == 'afternoon' and r['enabled']]
    if day_routines:
        print("\n🌞 День:")
        for routine in day_routines:
            print(f"   📋 {routine['name']} ({len(routine['habits'])} привычек, ~{routine['estimated_time']} мин)")
    
    # Вечерние привычки
    evening_habits = [h for h in habits if any(
        r['habit_id'] == h['id'] and (r['time'].startswith('1') and int(r['time'].split(':')[0]) >= 18 or 
                                      r['time'].startswith('2'))
        for r in reminders if r['enabled']
    )]
    
    if evening_habits:
        print("\n🌙 Вечер:")
        for habit in evening_habits:
            habit_reminders = [r for r in reminders if r['habit_id'] == habit['id'] and r['enabled']]
            if habit_reminders:
                times = ', '.join([r['time'] for r in habit_reminders])
                print(f"   ⏰ {times} - {habit['name']}")
    
    # Статистика дня
    today = '2024-01-15'
    today_completions = len([r for r in completion_history if r['date'] == today])
    print(f"\n📊 Статистика дня: {today_completions} привычек выполнено")

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
    
    # Демонстрация планирования
    create_routine()
    show_routines()
    execute_routine()
    add_reminder()
    show_todays_schedule()

def analyze_habit_patterns():
    """Анализирует patterns выполнения привычек"""
    if not completion_history:
        print("Недостаточно данных для анализа!")
        return
    
    # Анализ по дням недели
    days_of_week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    completions_by_day = {day: 0 for day in days_of_week}
    
    # Упрощенный анализ (в реальном приложении использовалась бы дата)
    for record in completion_history:
        # Для демонстрации используем случайное распределение
        import random
        day = random.choice(days_of_week)
        completions_by_day[day] += 1
    
    print("\nАнализ выполнения по дням недели:")
    print("-" * 40)
    
    for day in days_of_week:
        count = completions_by_day[day]
        print(f"{day}: {'█' * (count // 2)} {count}")

def show_consistency_analysis():
    """Анализирует последовательность выполнения"""
    if not habits:
        print("Нет данных для анализа!")
        return
    
    print("\nАнализ последовательности:")
    print("-" * 50)
    
    for habit in habits:
        if habit['total_completed'] > 0:
            consistency_score = (habit['current_streak'] / habit['longest_streak']) * 100 \
                                if habit['longest_streak'] > 0 else 0
            
            print(f"{habit['name']}:")
            print(f"   Текущая серия: {habit['current_streak']} дней")
            print(f"   Лучшая серия: {habit['longest_streak']} дней")
            print(f"   Последовательность: {consistency_score:.1f}%")
            
            if consistency_score >= 80:
                print("   🎯 Отличная последовательность!")
            elif consistency_score >= 50:
                print("   👍 Хорошая последовательность")
            else:
                print("   💪 Можно улучшить")
            print()

def generate_recommendations():
    """Генерирует рекомендации на основе анализа"""
    if not habits:
        print("Нет данных для рекомендаций!")
        return
    
    print("\nПерсональные рекомендации:")
    print("-" * 40)
    
    recommendations = []
    
    # Анализ низких серий
    low_streak_habits = [h for h in habits if h['current_streak'] < 3 and h['frequency'] == 'daily']
    if low_streak_habits:
        habit_names = ', '.join([h['name'] for h in low_streak_habits[:3]])
        recommendations.append(f"💪 Сфокусируйтесь на привычках с низкой серией: {habit_names}")
    
    # Анализ пропущенных привычек
    if completion_history:
        # Привычки, которые давно не выполнялись
        recent_days = 3
        recent_completions = set()
        for record in completion_history[-10:]:  # Последние 10 записей
            recent_completions.add(record['habit_id'])
        
        missed_habits = [h for h in habits if h['id'] not in recent_completions and h['frequency'] == 'daily']
        if missed_habits:
            habit_names = ', '.join([h['name'] for h in missed_habits[:2]])
            recommendations.append(f"⏰ Вернитесь к привычкам: {habit_names}")
    
    # Рекомендации по рутинам
    if not routines:
        recommendations.append("📋 Создайте утреннюю рутину для лучшей организованности")
    
    # Рекомендации по целям
    active_goals = [g for g in goals if not g['completed']]
    if not active_goals:
        recommendations.append("🎯 Установите новые цели для мотивации")
    else:
        nearly_completed = [g for g in active_goals if g['current_progress'] / g['target_streak'] >= 0.8]
        if nearly_completed:
            goal_names = ', '.join([g['habit_name'] for g in nearly_completed[:2]])
            recommendations.append(f"🔥 Почти у цели: {goal_names} - продолжайте в том же духе!")
    
    if not recommendations:
        recommendations.append("Ваши привычки выглядят отлично! Продолжайте в том же духе! 🌟")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")

def show_motivational_quotes():
    """Показывает мотивационные цитаты"""
    import random
    
    quotes = [
        "Привычка - это не то, что ты делаешь раз в месяц, а то, что ты делаешь каждый день.",
        "Успех - это сумма небольших усилий, повторяющихся изо дня в день.",
        "Не важно, как медленно ты продвигаешься, главное - не останавливайся.",
        "Лучшее время для посадки дерева было 20 лет назад. Следующий лучший момент - сегодня.",
        "Маленькие ежедневные улучшения со временем приводят к ошеломляющим результатам.",
        "Дисциплина - это выбор между тем, что ты хочешь сейчас, и тем, чего ты хочешь больше всего.",
        "Привычки определяют твое будущее больше, чем твои таланты."
    ]
    
    print("\n💭 Мотивация на сегодня:")
    print("-" * 50)
    print(f"\"{random.choice(quotes)}\"")
    print("-" * 50)

def show_weekly_report():
    """Генерирует недельный отчет"""
    if not completion_history:
        print("Недостаточно данных для отчета!")
        return
    
    # Статистика за неделю (упрощенная)
    weekly_completions = len([r for r in completion_history])
    active_days = len(set([r['date'] for r in completion_history]))
    
    print("\n📊 Недельный отчет:")
    print("=" * 50)
    print(f"Привычек выполнено: {weekly_completions}")
    print(f"Активных дней: {active_days}/7")
    
    if active_days > 0:
        daily_average = weekly_completions / active_days
        print(f"Среднее в день: {daily_average:.1f} привычек")
    
    # Самые успешные привычки
    if habits:
        top_habits = sorted(habits, key=lambda x: x['current_streak'], reverse=True)[:3]
        print("\n🏆 Топ-3 привычки этой недели:")
        for i, habit in enumerate(top_habits, 1):
            print(f"{i}. {habit['name']} - {habit['current_streak']} дней подряд")
    
    # Рекомендации на следующую неделю
    print("\n🎯 Цели на следующую неделю:")
    if len(habits) < 5:
        print("   • Добавьте 1-2 новые полезные привычки")
    
    low_streak_count = len([h for h in habits if h['current_streak'] < 3])
    if low_streak_count > 0:
        print(f"   • Укрепите {low_streak_count} привычек с низкой серией")

def main():
    print("Добро пожаловать в трекер привычек!")
    
    # Тестовые данные для анализа
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
    
    # Демонстрация аналитики
    analyze_habit_patterns()
    show_consistency_analysis()
    generate_recommendations()
    show_motivational_quotes()
    show_weekly_report()

if __name__ == "__main__":
    main()