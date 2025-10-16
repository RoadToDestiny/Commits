# todo_manager.py
# Система управления задачами
# Коммит 10: Финальная версия с полной функциональностью

"""
МЕНЕДЖЕР ЗАДАЧ (To-Do List)

Расширенная система управления задачами с функциями:
- Добавление, редактирование, удаление задач
- Категории и приоритеты
- Поиск и фильтрация
- Статистика и аналитика
- Интуитивное меню

Автор: [Ваше имя]
Версия: 1.0
"""

tasks = []
categories = ['Работа', 'Учеба', 'Личное', 'Здоровье', 'Другое']
priorities = {'Низкий': 1, 'Средний': 2, 'Высокий': 3, 'Срочный': 4}

def add_task():
    """Добавляет новую задачу с категорией и приоритетом"""
    title = input("Введите название задачи: ")
    
    if not title.strip():
        print("Ошибка: Название задачи не может быть пустым!")
        return
    
    print("\nКатегории:")
    for i, category in enumerate(categories, 1):
        print(f"   {i}. {category}")
    
    print("\nПриоритеты:")
    for i, priority in enumerate(priorities.keys(), 1):
        print(f"   {i}. {priority}")
    
    try:
        category_choice = int(input("Выберите категорию (номер): ")) - 1
        priority_choice = int(input("Выберите приоритет (номер): ")) - 1
        
        if 0 <= category_choice < len(categories) and 0 <= priority_choice < len(priorities):
            category = categories[category_choice]
            priority_name = list(priorities.keys())[priority_choice]
            priority_value = priorities[priority_name]
            
            task = {
                'id': len(tasks) + 1,
                'title': title,
                'category': category,
                'priority': priority_name,
                'priority_value': priority_value,
                'completed': False,
                'created_at': '2024-01-01'
            }
            tasks.append(task)
            print(f"Задача '{title}' добавлена!")
        else:
            print("Ошибка: Неверный выбор!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите числа!")

def show_tasks():
    """Показывает все задачи с деталями"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("\nВсе задачи:")
    print("-" * 60)
    
    for task in tasks:
        status = "[X]" if task['completed'] else "[ ]"
        priority_symbol = "!!!" if task['priority'] == 'Срочный' else \
                         "!!" if task['priority'] == 'Высокий' else \
                         "!" if task['priority'] == 'Средний' else ""
        
        print(f"{task['id']:2d}. {status} {priority_symbol:3} [{task['category']:8}] {task['title']}")
    
    print("-" * 60)
    print(f"Всего задач: {len(tasks)}")

# ... (все остальные функции: complete_task, delete_task, search_tasks, 
# filter_tasks_by_status, show_statistics, show_priority_analysis)

def show_main_menu():
    """Показывает главное меню программы"""
    print("\n" + "="*50)
    print("           МЕНЕДЖЕР ЗАДАЧ")
    print("="*50)
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу")
    print("5. Поиск задач")
    print("6. Фильтр по статусу")
    print("7. Статистика")
    print("8. Анализ приоритетов")
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
    """Инициализирует примеры задач для демонстрации"""
    sample_tasks = [
        {'id': 1, 'title': 'Изучить Python', 'category': 'Учеба', 'priority': 'Высокий', 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Сделать домашнее задание', 'category': 'Учеба', 'priority': 'Средний', 'completed': True, 'created_at': '2024-01-02'},
        {'id': 3, 'title': 'Купить продукты', 'category': 'Личное', 'priority': 'Низкий', 'completed': False, 'created_at': '2024-01-02'},
        {'id': 4, 'title': 'Подготовить отчет', 'category': 'Работа', 'priority': 'Срочный', 'completed': True, 'created_at': '2024-01-03'}
    ]
    tasks.extend(sample_tasks)

def main():
    """Главная функция программы"""
    print("Добро пожаловать в менеджер задач!")
    
    # Загружаем примеры данных (можно закомментировать)
    initialize_sample_data()
    
    # Главный цикл программы
    while True:
        show_main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            show_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            search_tasks()
        elif choice == 6:
            filter_tasks_by_status()
        elif choice == 7:
            show_statistics()
        elif choice == 8:
            show_priority_analysis()
        elif choice == 9:
            print("\nСпасибо за использование менеджера задач!")
            print("До свидания!")
            break
        elif choice == -1:
            continue
        else:
            print("Ошибка: Неверный выбор! Пожалуйста, выберите от 1 до 9.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()