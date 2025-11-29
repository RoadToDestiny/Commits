# travel_planner.py
# Система планирования путешествий и поездок
# Коммит 3: Просмотр и управление поездками

trips = []
destinations = []

def add_trip():
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
            'status': 'planned',
            'travelers': []
        }
        trips.append(trip)
        print(f"Поездка в '{destination}' добавлена!")
    else:
        print("Ошибка: Пункт назначения не может быть пустым!")

def show_all_trips():
    """Показывает все поездки"""
    if not trips:
        print("Список поездок пуст!")
        return
    
    print("\nВсе поездки:")
    print("-" * 80)
    print(f"{'ID':<3} {'Направление':<20} {'Даты':<20} {'Бюджет':<12} {'Статус':<12}")
    print("-" * 80)
    
    for trip in trips:
        dates = f"{trip['start_date']} - {trip['end_date']}" if trip['start_date'] else "Даты не установлены"
        print(f"{trip['id']:<3} {trip['destination']:<20} {dates:<20} "
              f"{trip['budget']:<12.2f} {trip['status']:<12}")
    
    print("-" * 80)

def show_trip_details(trip_id):
    """Показывает детальную информацию о поездке"""
    for trip in trips:
        if trip['id'] == trip_id:
            print(f"\nДетали поездки #{trip_id}:")
            print(f"   Направление: {trip['destination']}")
            print(f"   Описание: {trip['description']}")
            print(f"   Даты: {trip['start_date']} - {trip['end_date']}")
            print(f"   Бюджет: {trip['budget']:.2f}")
            print(f"   Статус: {trip['status']}")
            print(f"   Путешественники: {', '.join(trip['travelers']) if trip['travelers'] else 'Нет'}")
            return
    
    print(f"Ошибка: Поездка с ID {trip_id} не найдена!")

def edit_trip():
    """Редактирует информацию о поездке"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки для редактирования: "))
        
        for trip in trips:
            if trip['id'] == trip_id:
                print(f"\nРедактирование поездки: '{trip['destination']}'")
                trip['destination'] = input(f"Новое направление [{trip['destination']}]: ") or trip['destination']
                trip['description'] = input(f"Новое описание [{trip['description']}]: ") or trip['description']
                trip['start_date'] = input(f"Дата начала (ГГГГ-ММ-ДД) [{trip['start_date']}]: ") or trip['start_date']
                trip['end_date'] = input(f"Дата окончания (ГГГГ-ММ-ДД) [{trip['end_date']}]: ") or trip['end_date']
                
                try:
                    budget_str = input(f"Бюджет [{trip['budget']}]: ")
                    if budget_str:
                        trip['budget'] = float(budget_str)
                except ValueError:
                    print("Ошибка: Бюджет должен быть числом!")
                
                print("Поездка успешно обновлена!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в планировщик путешествий!")
    
    # Добавляем тестовые поездки
    trips.extend([
        {'id': 1, 'destination': 'Париж', 'description': 'Романтическое путешествие', 
         'start_date': '2024-06-01', 'end_date': '2024-06-07', 'budget': 1500.00,
         'status': 'planned', 'travelers': ['Анна', 'Иван']},
        {'id': 2, 'destination': 'Сочи', 'description': 'Отдых на море', 
         'start_date': '2024-07-15', 'end_date': '2024-07-25', 'budget': 800.00,
         'status': 'planned', 'travelers': ['Семья']}
    ])
    
    # Демонстрация новых функций
    show_all_trips()
    show_trip_details(1)
    edit_trip()

if __name__ == "__main__":
    main()