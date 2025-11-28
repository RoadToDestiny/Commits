# travel_planner.py
# Система планирования путешествий и поездок
# Коммит 2: Структура данных и добавление поездок

# Глобальные переменные для хранения данных
trips = []
destinations = []

def add_trip():
    """Добавляет новую поездку"""
    destination = input("Введите пункт назначения: ")
    description = input("Введите описание поездки: ")
    
    if destination.strip():
        trip = {
            'id': len(trips) + 1,
            'destination': destination,
            'description': description,
            'start_date': '',
            'end_date': '',
            'budget': 0.0,
            'status': 'planned',  # planned, in_progress, completed, cancelled
            'travelers': []
        }
        trips.append(trip)
        print(f"Поездка в '{destination}' добавлена!")
    else:
        print("Ошибка: Пункт назначения не может быть пустым!")

def main():
    print("Добро пожаловать в планировщик путешествий!")
    
    # Тестируем добавление поездок
    add_trip()
    print(f"Всего поездок: {len(trips)}")

if __name__ == "__main__":
    main()