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

def add_traveler():
    """Добавляет участника к поездке"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        traveler_name = input("Введите имя участника: ")
        
        if not traveler_name.strip():
            print("Ошибка: Имя участника не может быть пустым!")
            return
        
        for trip in trips:
            if trip['id'] == trip_id:
                if traveler_name not in trip['travelers']:
                    trip['travelers'].append(traveler_name)
                    print(f"Участник '{traveler_name}' добавлен к поездке в '{trip['destination']}'!")
                else:
                    print(f"Участник '{traveler_name}' уже в списке!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def remove_traveler():
    """Удаляет участника из поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        for trip in trips:
            if trip['id'] == trip_id:
                if not trip['travelers']:
                    print(f"В поездке в '{trip['destination']}' нет участников!")
                    return
                
                print(f"Участники поездки в '{trip['destination']}':")
                for i, traveler in enumerate(trip['travelers'], 1):
                    print(f"   {i}. {traveler}")
                
                traveler_choice = int(input("Введите номер участника для удаления: ")) - 1
                
                if 0 <= traveler_choice < len(trip['travelers']):
                    removed_traveler = trip['travelers'].pop(traveler_choice)
                    print(f"Участник '{removed_traveler}' удален из поездки!")
                else:
                    print("Ошибка: Неверный номер участника!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def update_trip_status():
    """Обновляет статус поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        print("\nДоступные статусы:")
        print("1. planned - запланирована")
        print("2. in_progress - в процессе")
        print("3. completed - завершена")
        print("4. cancelled - отменена")
        
        status_choice = int(input("Выберите статус (1-4): "))
        
        status_map = {
            1: 'planned',
            2: 'in_progress', 
            3: 'completed',
            4: 'cancelled'
        }
        
        if status_choice in status_map:
            for trip in trips:
                if trip['id'] == trip_id:
                    old_status = trip['status']
                    trip['status'] = status_map[status_choice]
                    print(f"Статус поездки в '{trip['destination']}' изменен: "
                          f"{old_status} -> {trip['status']}")
                    return
            
            print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
        else:
            print("Ошибка: Неверный выбор статуса!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def delete_trip():
    """Удаляет поездку"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки для удаления: "))
        
        for i, trip in enumerate(trips):
            if trip['id'] == trip_id:
                destination = trip['destination']
                trips.pop(i)
                print(f"Поездка в '{destination}' удалена!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в планировщик путешествий!")
    
    # Тестовые данные
    trips.extend([
        {'id': 1, 'destination': 'Париж', 'description': 'Романтическое путешествие', 
         'start_date': '2024-06-01', 'end_date': '2024-06-07', 'budget': 1500.00,
         'status': 'planned', 'travelers': ['Анна']}
    ])
    
    # Демонстрация управления участниками и статусами
    add_traveler()
    remove_traveler()
    update_trip_status()
    delete_trip()
    show_all_trips()

if __name__ == "__main__":
    main()