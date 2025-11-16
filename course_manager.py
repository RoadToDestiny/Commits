# course_manager.py
# Система управления учебными курсами и прогрессом
# Коммит 10: Финальная версия с полной функциональностью

"""
СИСТЕМА УПРАВЛЕНИЯ УЧЕБНЫМИ КУРСАМИ

Комплексная система для управления процессом обучения с функциями:
- Учет курсов и прогресса
- Управление уроками и материалами
- Напоминания и дедлайны
- Статистика и аналитика
- Планирование обучения

Автор: [Ваше имя]
Версия: 1.0
"""

courses = []
categories = ['Программирование', 'Математика', 'Иностранные языки', 'Дизайн', 'Маркетинг', 'Другое']
reminders = []
notes = []
materials = []
study_goals = []

def add_course():
    """Добавляет новый учебный курс"""
    name = input("Введите название курса: ")
    description = input("Введите описание курса: ")
    
    if name.strip():
        course = {
            'id': len(courses) + 1,
            'name': name,
            'description': description,
            'category': '',
            'total_lessons': 0,
            'completed_lessons': 0,
            'status': 'active',
            'progress': 0.0
        }
        courses.append(course)
        print(f"Курс '{name}' добавлен!")
    else:
        print("Ошибка: Название курса не может быть пустым!")

def show_all_courses():
    """Показывает все курсы"""
    if not courses:
        print("Список курсов пуст!")
        return
    
    print("\nВсе курсы:")
    print("-" * 80)
    print(f"{'ID':<3} {'Название':<20} {'Категория':<15} {'Прогресс':<10} {'Статус':<10}")
    print("-" * 80)
    
    for course in courses:
        progress_percent = course['progress'] * 100
        print(f"{course['id']:<3} {course['name']:<20} {course['category']:<15} "
              f"{progress_percent:>6.1f}%   {course['status']:<10}")
    
    print("-" * 80)

# ... (все остальные функции: show_course_details, edit_course, add_lessons_to_course,
# mark_lesson_completed, update_course_status, show_learning_statistics, 
# show_progress_by_category, show_recent_progress, add_reminder, show_reminders,
# mark_reminder_completed, show_study_recommendations, add_note, show_notes,
# add_material, show_materials, mark_material_completed, show_course_resources,
# add_study_goal, show_study_goals, mark_goal_completed, create_study_plan,
# show_learning_insights)

def show_main_menu():
    """Показывает главное меню программы"""
    print("\n" + "="*50)
    print("       СИСТЕМА УПРАВЛЕНИЯ УЧЕБНЫМИ КУРСАМИ")
    print("="*50)
    print("1. Показать все курсы")
    print("2. Добавить курс")
    print("3. Редактировать курс")
    print("4. Управление уроками")
    print("5. Статистика обучения")
    print("6. Напоминания")
    print("7. Заметки и материалы")
    print("8. Цели и планирование")
    print("9. Выход")
    print("="*50)

def get_menu_choice():
    """Получает и проверяет выбор пользователя"""
    try:
        choice = int(input("\nВыберите действие (1-9): "))
        return choice
    except ValueError:
        print("Ошибка: Пожалуйста, введите число от 1 до 9!")
        return -1

def initialize_sample_data():
    """Инициализирует примеры данных для демонстрации"""
    sample_courses = [
        {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы программирования на Python', 
         'category': 'Программирование', 'total_lessons': 10, 'completed_lessons': 3, 
         'status': 'active', 'progress': 0.3},
        {'id': 2, 'name': 'Английский язык', 'description': 'Курс английского для IT', 
         'category': 'Иностранные языки', 'total_lessons': 20, 'completed_lessons': 15, 
         'status': 'active', 'progress': 0.75},
        {'id': 3, 'name': 'Веб-дизайн', 'description': 'Основы веб-дизайна', 
         'category': 'Дизайн', 'total_lessons': 15, 'completed_lessons': 15, 
         'status': 'completed', 'progress': 1.0}
    ]
    courses.extend(sample_courses)
    
    reminders.extend([
        {'id': 1, 'course_id': 1, 'course_name': 'Python для начинающих', 
         'text': 'Завершить первые 5 уроков', 'deadline': '2024-01-20', 'completed': False}
    ])
    
    study_goals.extend([
        {'id': 1, 'name': 'Завершить курс Python', 'target_date': '2024-02-01', 
         'priority': 'high', 'completed': False, 'created_date': '2024-01-01'}
    ])
    
    notes.extend([
        {'id': 1, 'course_id': 1, 'course_name': 'Python для начинающих', 
         'text': 'Важно: изучить списки и словари', 'lesson_number': '3', 'created_date': '2024-01-01'}
    ])

def main():
    """Главная функция программы"""
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Загружаем примеры данных (можно закомментировать)
    initialize_sample_data()
    
    # Главный цикл программы
    while True:
        show_main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            show_all_courses()
        elif choice == 2:
            add_course()
        elif choice == 3:
            edit_course()
            show_all_courses()
        elif choice == 4:
            add_lessons_to_course()
            mark_lesson_completed()
            update_course_status()
        elif choice == 5:
            show_learning_statistics()
            show_progress_by_category()
            show_recent_progress()
        elif choice == 6:
            show_reminders()
            add_reminder()
            mark_reminder_completed()
            show_study_recommendations()
        elif choice == 7:
            show_notes()
            show_materials()
            add_note()
            add_material()
            mark_material_completed()
        elif choice == 8:
            show_study_goals()
            add_study_goal()
            mark_goal_completed()
            create_study_plan()
            show_learning_insights()
        elif choice == 9:
            print("\nСпасибо за использование системы управления курсами!")
            print("Успехов в обучении! 🎓")
            break
        elif choice == -1:
            continue
        else:
            print("Ошибка: Неверный выбор! Пожалуйста, выберите от 1 до 9.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
    