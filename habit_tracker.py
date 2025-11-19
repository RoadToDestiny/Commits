# habit_tracker.py
# Система учета привычек и формирования рутин
# Коммит 3: Просмотр и управление привычками

habits = []
categories = ['Здоровье', 'Спорт', 'Обучение', 'Работа', 'Личное', 'Другое']

def add_habit():
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

def show_habit_details(habit_id):
    """Показывает детальную информацию о привычке"""
    for habit in habits:
        if habit['id'] == habit_id:
            print(f"\nДетали привычки #{habit_id}:")
            print(f"   Название: {habit['name']}")
            print(f"   Описание: {habit['description']}")
            print(f"   Категория: {habit['category']}")
            print(f"   Частота: {habit['frequency']}")
            print(f"   Цель: {habit['target_count']} раз в {habit['frequency']}")
            print(f"   Текущая серия: {habit['current_streak']} дней")
            print(f"   Лучшая серия: {habit['longest_streak']} дней")
            print(f"   Всего выполнено: {habit['total_completed']} раз")
            print(f"   Создана: {habit['created_date']}")
            return
    
    print(f"Ошибка: Привычка с ID {habit_id} не найдена!")

def edit_habit():
    """Редактирует информацию о привычке"""
    show_all_habits()
    
    try:
        habit_id = int(input("Введите ID привычки для редактирования: "))
        
        for habit in habits:
            if habit['id'] == habit_id:
                print(f"\nРедактирование привычки: '{habit['name']}'")
                habit['name'] = input(f"Новое название [{habit['name']}]: ") or habit['name']
                habit['description'] = input(f"Новое описание [{habit['description']}]: ") or habit['description']
                
                print("\nКатегории:")
                for i, category in enumerate(categories, 1):
                    print(f"   {i}. {category}")
                
                category_choice = input(f"Новая категория [{habit['category']}]: ")
                if category_choice.isdigit():
                    choice = int(category_choice) - 1
                    if 0 <= choice < len(categories):
                        habit['category'] = categories[choice]
                
                print("\nЧастота выполнения:")
                print("   1. daily - ежедневно")
                print("   2. weekly - еженедельно")
                print("   3. monthly - ежемесячно")
                
                freq_choice = input(f"Новая частота [{habit['frequency']}]: ")
                if freq_choice == '1':
                    habit['frequency'] = 'daily'
                elif freq_choice == '2':
                    habit['frequency'] = 'weekly'
                elif freq_choice == '3':
                    habit['frequency'] = 'monthly'
                
                print("Привычка успешно обновлена!")
                return
        
        print(f"Ошибка: Привычка с ID {habit_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в трекер привычек!")
    
    # Добавляем тестовые привычки
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
    
    # Демонстрация новых функций
    show_all_habits()
    show_habit_details(1)
    edit_habit()

if __name__ == "__main__":
    main()