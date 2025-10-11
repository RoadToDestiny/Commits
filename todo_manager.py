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

if __name__ == "__main__":
    main()