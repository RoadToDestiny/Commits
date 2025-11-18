# habit_tracker.py
# Система учета привычек и формирования рутин
# Коммит 2: Структура данных и добавление привычек

# Глобальные переменные для хранения данных
habits = []
categories = ['Здоровье', 'Спорт', 'Обучение', 'Работа', 'Личное', 'Другое']

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
            'frequency': 'daily',  # daily, weekly, monthly
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

def main():
    print("Добро пожаловать в трекер привычек!")
    
    # Тестируем добавление привычек
    add_habit()
    print(f"Всего привычек: {len(habits)}")

if __name__ == "__main__":
  main()