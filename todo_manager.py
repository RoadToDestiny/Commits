# todo_manager.py
# Система управления задачами
# Коммит 1: Базовая структура проекта

def main():
    print("Добро пожаловать в менеджер задач!")
    print("Система находится в разработке...")

# Глобальный список для хранения задач
tasks = []

def add_task():
    """Добавляет новую задачу в список"""
    title = input("Введите название задачи: ")
    
    if title.strip():  # Проверяем, что строка не пустая
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'completed': False,
            'created_at': '2024-01-01'  # Временная дата
        }
        tasks.append(task)
        print(f"Задача '{title}' добавлена!")
    else:
        print("Название задачи не может быть пустым!")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Тестируем добавление задач
    add_task()
    print(f"Всего задач: {len(tasks)}")

tasks = []

def add_task():
    title = input("Введите название задачи: ")
    if title.strip():
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'completed': False,
            'created_at': '2024-01-01'
        }
        tasks.append(task)
        print(f"Задача '{title}' добавлена!")
    else:
        print("Название задачи не может быть пустым!")

def show_tasks():
    """Показывает все задачи"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("\n Ваши задачи:")
    print("-" * 40)
    
    for task in tasks:
        status = "good" if task['completed'] else "wait"
        print(f"{task['id']}. {status} {task['title']}")
    
    print("-" * 40)

def show_task_details(task_id):
    """Показывает детальную информацию о задаче"""
    for task in tasks:
        if task['id'] == task_id:
            print(f"\n Детали задачи #{task_id}:")
            print(f"   Название: {task['title']}")
            print(f"   Статус: {'Выполнена' if task['completed'] else 'В процессе'}")
            print(f"   Создана: {task['created_at']}")
            return
    
    print(f"Задача с ID {task_id} не найдена!")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Добавляем тестовые задачи
    tasks.extend([
        {'id': 1, 'title': 'Изучить Python', 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Сделать домашнее задание', 'completed': True, 'created_at': '2024-01-02'}
    ])
    
    show_tasks()
    show_task_details(1)

def complete_task():
    """Отмечает задачу как выполненную"""
    show_tasks()
    
    try:
        task_id = int(input("Введите ID задачи для отметки: "))
        
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Задача '{task['title']}' отмечена как выполненная!")
                return
        
        print(f"Ошибка: Задача с ID {task_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def delete_task():
    """Удаляет задачу из списка"""
    show_tasks()
    
    try:
        task_id = int(input("Введите ID задачи для удаления: "))
        
        for i, task in enumerate(tasks):
            if task['id'] == task_id:
                deleted_title = task['title']
                tasks.pop(i)
                print(f"Задача '{deleted_title}' удалена!")
                return
        
        print(f"Ошибка: Задача с ID {task_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Тестовые данные
    tasks.extend([
        {'id': 1, 'title': 'Изучить Python', 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Сделать домашнее задание', 'completed': True, 'created_at': '2024-01-02'}
    ])
    
    # Демонстрация новых функций
    show_tasks()
    complete_task()
    delete_task()
    show_tasks()

def add_task_with_category():
    """Добавляет задачу с выбором категории"""
    title = input("Введите название задачи: ")
    
    if not title.strip():
        print("Ошибка: Название задачи не может быть пустым!")
        return
    
    print("\nДоступные категории:")
    for i, category in enumerate(categories, 1):
        print(f"   {i}. {category}")
    
    try:
        category_choice = int(input("Выберите категорию (номер): ")) - 1
        
        if 0 <= category_choice < len(categories):
            task = {
                'id': len(tasks) + 1,
                'title': title,
                'category': categories[category_choice],
                'completed': False,
                'created_at': '2024-01-01'
            }
            tasks.append(task)
            print(f"Задача '{title}' добавлена в категорию '{categories[category_choice]}'!")
        else:
            print("Ошибка: Неверный выбор категории!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите число!")

def show_tasks_by_category():
    """Показывает задачи по категориям"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    for category in categories:
        category_tasks = [task for task in tasks if task.get('category') == category]
        
        if category_tasks:
            print(f"\nКатегория '{category}':")
            for task in category_tasks:
                status = "[X]" if task['completed'] else "[ ]"
                print(f"   {task['id']}. {status} {task['title']}")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Тестовые данные с категориями
    tasks.extend([
        {'id': 1, 'title': 'Изучить Python', 'category': 'Учеба', 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Подготовить отчет', 'category': 'Работа', 'completed': True, 'created_at': '2024-01-02'}
    ])
    
    # Демонстрация работы с категориями
    add_task_with_category()
    show_tasks_by_category()

def add_task_with_priority():
    """Добавляет задачу с приоритетом"""
    title = input("Введите название задачи: ")
    
    if not title.strip():
        print("Ошибка: Название задачи не может быть пустым!")
        return
    
    print("\nДоступные приоритеты:")
    for i, priority in enumerate(priorities.keys(), 1):
        print(f"   {i}. {priority}")
    
    try:
        priority_choice = int(input("Выберите приоритет (номер): ")) - 1
        priority_list = list(priorities.keys())
        
        if 0 <= priority_choice < len(priority_list):
            priority = priority_list[priority_choice]
            
            task = {
                'id': len(tasks) + 1,
                'title': title,
                'category': 'Другое',  # Упрощаем для демонстрации
                'priority': priority,
                'priority_value': priorities[priority],
                'completed': False,
                'created_at': '2024-01-01'
            }
            tasks.append(task)
            print(f"Задача '{title}' добавлена с приоритетом '{priority}'!")
        else:
            print("Ошибка: Неверный выбор приоритета!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите число!")

def show_tasks_sorted_by_priority():
    """Показывает задачи, отсортированные по приоритету"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    sorted_tasks = sorted(tasks, key=lambda x: x.get('priority_value', 0), reverse=True)
    
    print("\nЗадачи по приоритету:")
    print("-" * 50)
    
    for task in sorted_tasks:
        status = "[X]" if task['completed'] else "[ ]"
        priority_symbol = "!!!" if task.get('priority') == 'Срочный' else \
                         "!!" if task.get('priority') == 'Высокий' else \
                         "!" if task.get('priority') == 'Средний' else ""
        
        print(f"{task['id']}. {status} {priority_symbol:3} {task['title']}")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Тестовые данные с приоритетами
    tasks.extend([
        {'id': 1, 'title': 'Изучить Python', 'category': 'Учеба', 'priority': 'Высокий', 'priority_value': 3, 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Купить молоко', 'category': 'Личное', 'priority': 'Низкий', 'priority_value': 1, 'completed': False, 'created_at': '2024-01-02'},
        {'id': 3, 'title': 'Срочный звонок', 'category': 'Работа', 'priority': 'Срочный', 'priority_value': 4, 'completed': False, 'created_at': '2024-01-02'}
    ])
    
    # Демонстрация приоритетов
    add_task_with_priority()
    show_tasks_sorted_by_priority()

def search_tasks():
    """Ищет задачи по ключевому слову"""
    keyword = input("Введите ключевое слово для поиска: ").lower()
    
    if not keyword.strip():
        print("Ошибка: Введите ключевое слово для поиска!")
        return
    
    found_tasks = [task for task in tasks if keyword in task['title'].lower()]
    
    if found_tasks:
        print(f"\nНайдено задач: {len(found_tasks)}")
        for task in found_tasks:
            status = "[X]" if task['completed'] else "[ ]"
            print(f"   {task['id']}. {status} {task['title']}")
    else:
        print("Задачи не найдены!")

def filter_tasks_by_status():
    """Фильтрует задачи по статусу выполнения"""
    print("\nФильтр по статусу:")
    print("1. Все задачи")
    print("2. Только активные")
    print("3. Только выполненные")
    
    try:
        choice = int(input("Выберите вариант: "))
        
        if choice == 1:
            show_tasks()
        elif choice == 2:
            active_tasks = [task for task in tasks if not task['completed']]
            if active_tasks:
                print("\nАктивные задачи:")
                for task in active_tasks:
                    print(f"   {task['id']}. {task['title']}")
            else:
                print("Нет активных задач!")
        elif choice == 3:
            completed_tasks = [task for task in tasks if task['completed']]
            if completed_tasks:
                print("\nВыполненные задачи:")
                for task in completed_tasks:
                    print(f"   {task['id']}. {task['title']}")
            else:
                print("Нет выполненных задач!")
        else:
            print("Ошибка: Неверный выбор!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите число!")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Тестовые данные
    tasks.extend([
        {'id': 1, 'title': 'Изучить Python', 'category': 'Учеба', 'priority': 'Высокий', 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Сделать домашнее задание', 'category': 'Учеба', 'priority': 'Средний', 'completed': True, 'created_at': '2024-01-02'},
        {'id': 3, 'title': 'Купить продукты', 'category': 'Личное', 'priority': 'Низкий', 'completed': False, 'created_at': '2024-01-02'}
    ])
    
    # Демонстрация поиска и фильтрации
    search_tasks()
    filter_tasks_by_status()

def show_statistics():
    """Показывает статистику по задачам"""
    if not tasks:
        print("Нет данных для статистики!")
        return
    
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task['completed']])
    active_tasks = total_tasks - completed_tasks
    completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    
    print("\nСтатистика задач:")
    print("-" * 30)
    print(f"Всего задач: {total_tasks}")
    print(f"Выполнено: {completed_tasks}")
    print(f"Активных: {active_tasks}")
    print(f"Процент выполнения: {completion_rate:.1f}%")
    
    # Статистика по категориям
    print("\nСтатистика по категориям:")
    for category in categories:
        category_tasks = [task for task in tasks if task.get('category') == category]
        if category_tasks:
            completed_in_category = len([task for task in category_tasks if task['completed']])
            print(f"   {category}: {len(category_tasks)} задач ({completed_in_category} выполнено)")

def show_priority_analysis():
    """Анализ приоритетов задач"""
    if not tasks:
        print("Нет данных для анализа!")
        return
    
    print("\nАнализ приоритетов:")
    
    for priority_name, priority_value in priorities.items():
        priority_tasks = [task for task in tasks if task.get('priority_value') == priority_value]
        completed_priority = len([task for task in priority_tasks if task['completed']])
        
        if priority_tasks:
            completion_rate = (completed_priority / len(priority_tasks)) * 100
            symbol = "!!!" if priority_name == 'Срочный' else \
                    "!!" if priority_name == 'Высокий' else \
                    "!" if priority_name == 'Средний' else ""
            
            print(f"   {symbol} {priority_name}: {len(priority_tasks)} задач ({completion_rate:.1f}% выполнено)")

def main():
    print("Добро пожаловать в менеджер задач!")
    
    # Тестовые данные для статистики
    tasks.extend([
        {'id': 1, 'title': 'Изучить Python', 'category': 'Учеба', 'priority': 'Высокий', 'completed': False, 'created_at': '2024-01-01'},
        {'id': 2, 'title': 'Сделать ДЗ', 'category': 'Учеба', 'priority': 'Средний', 'completed': True, 'created_at': '2024-01-02'},
        {'id': 3, 'title': 'Купить продукты', 'category': 'Личное', 'priority': 'Низкий', 'completed': False, 'created_at': '2024-01-02'},
        {'id': 4, 'title': 'Срочный отчет', 'category': 'Работа', 'priority': 'Срочный', 'completed': True, 'created_at': '2024-01-02'}
    ])
    
    # Демонстрация статистики
    show_statistics()
    show_priority_analysis()

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
    print("Добро пожаловать в менеджер задач!")
    
    # Загружаем примеры данных
    initialize_sample_data()
    
    # Демонстрируем меню
    show_main_menu()
    choice = get_menu_choice()
    print(f"Вы выбрали: {choice}")

if __name__ == "__main__":
    main()