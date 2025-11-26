# habit_tracker.py
# Система учета привычек и формирования рутин
# Коммит 10: Финальная версия с полной функциональностью

"""
ТРЕКЕР ПРИВЫЧЕК И РУТИН

Комплексная система для формирования и отслеживания привычек с функциями:
- Создание и управление привычками
- Отслеживание серий и прогресса
- Цели и система наград
- Планирование рутин и расписаний
- Аналитика и персонализированные рекомендации

Автор: [Ваше имя]
Версия: 1.0
"""

habits = []
categories = ['Здоровье', 'Спорт', 'Обучение', 'Работа', 'Личное', 'Другое']
completion_history = []
goals = []
rewards = []
routines = []
reminders = []

def add_habit():
    """Добавляет новую привычку"""
    name = input("Введите название привычки: ")
    description = input("Введите описание привычки: ")
    
    if name.strip():
        habit = {
            'id': len(habits) + 1,
            'name': name,
            'description': description,
            'category': '',
            'frequency': 'daily',
            'target_count': 1,
            'current_streak': 0,
            'longest_streak': 0,
            'total_completed': 0,
            'created_date': '2024-01-01'
        }
        habits.append(habit)
        print(f"Привычка '{name}' добавлена!")
    else:
        print("Ошибка: Название привычки не может быть пустым!")

def show_all_habits():
    """Показывает все привычки"""
    if not habits:
        print("Список привычек пуст!")
        return
    
    print("\nВсе привычки:")
    print("-" * 80)
    print(f"{'ID':<3} {'Название':<20} {'Категория':<12} {'Текущая серия':<15} {'Всего выполнено':<15}")
    print("-" * 80)
    
    for habit in habits:
        print(f"{habit['id']:<3} {habit['name']:<20} {habit['category']:<12} "
              f"{habit['current_streak']:<15} {habit['total_completed']:<15}")
    
    print("-" * 80)

# ... (все остальные функции: show_habit_details, edit_habit, mark_habit_completed,
# mark_habit_missed, show_today_habits, show_completion_history, show_habit_statistics,
# show_streak_leaderboard, show_category_statistics, show_personal_bests, add_goal,
# show_goals, check_goal_progress, add_reward, unlock_reward, show_rewards,
# create_routine, show_routines, execute_routine, add_reminder, show_todays_schedule,
# analyze_habit_patterns, show_consistency_analysis, generate_recommendations,
# show_motivational_quotes, show_weekly_report)

def show_main_menu():
    """Показывает главное меню программы"""
    print("\n" + "="*50)
    print("           ТРЕКЕР ПРИВЫЧЕК И РУТИН")
    print("="*50)
    print("1. Показать все привычки")
    print("2. Добавить привычку")
    print("3. Отметить выполнение")
    print("4. Статистика и аналитика")
    print("5. Цели и награды")
    print("6. Рутины и расписание")
    print("7. Рекомендации и отчеты")
    print("8. Выход")
    print("="*50)

def get_menu_choice():
    """Получает и проверяет выбор пользователя"""
    try:
        choice = int(input("\nВыберите действие (1-8): "))
        return choice
    except ValueError:
        print("Ошибка: Пожалуйста, введите число от 1 до 8!")
        return -1

def initialize_sample_data():
    """Инициализирует примеры данных для демонстрации"""
    sample_habits = [
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
    ]
    habits.extend(sample_habits)
    
    completion_history.extend([
        {'habit_id': 1, 'habit_name': 'Утренняя зарядка', 'date': '2024-01-14', 'timestamp': '08:00'},
        {'habit_id': 2, 'habit_name': 'Чтение книги', 'date': '2024-01-14', 'timestamp': '21:00'},
        {'habit_id': 1, 'habit_name': 'Утренняя зарядка', 'date': '2024-01-13', 'timestamp': '08:30'}
    ])
    
    goals.extend([
        {'id': 1, 'habit_id': 1, 'habit_name': 'Утренняя зарядка',
         'target_streak': 21, 'description': '21 день зарядки подряд',
         'completed': False, 'current_progress': 5, 'created_date': '2024-01-01'}
    ])
    
    rewards.extend([
        {'id': 1, 'name': 'Вечер кино', 'description': 'Посмотреть любимый фильм',
         'unlocked': False, 'unlock_date': None}
    ])
    
    routines.extend([
        {'id': 1, 'name': 'Утренняя рутина', 'habits': [
            {'id': 1, 'name': 'Утренняя зарядка'}
        ], 'time_of_day': 'morning', 'estimated_time': 15, 'enabled': True}
    ])

def main():
    """Главная функция программы"""
    print("Добро пожаловать в трекер привычек!")
    
    # Загружаем примеры данных (можно закомментировать)
    initialize_sample_data()
    
    # Главный цикл программы
    while True:
        show_main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            show_all_habits()
        elif choice == 2:
            add_habit()
            edit_habit()
        elif choice == 3:
            show_today_habits()
            mark_habit_completed()
            mark_habit_missed()
            show_completion_history()
        elif choice == 4:
            show_habit_statistics()
            show_streak_leaderboard()
            show_category_statistics()
            show_personal_bests()
        elif choice == 5:
            show_goals()
            add_goal()
            check_goal_progress()
            show_rewards()
            add_reward()
            unlock_reward()
        elif choice == 6:
            show_routines()
            create_routine()
            execute_routine()
            add_reminder()
            show_todays_schedule()
        elif choice == 7:
            generate_recommendations()
            show_consistency_analysis()
            analyze_habit_patterns()
            show_motivational_quotes()
            show_weekly_report()
        elif choice == 8:
            print("\nСпасибо за использование трекера привычек!")
            print("Удачи в формировании полезных привычек! 💪")
            break
        elif choice == -1:
            continue
        else:
            print("Ошибка: Неверный выбор! Пожалуйста, выберите от 1 до 8.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()