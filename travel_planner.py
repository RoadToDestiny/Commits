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

def add_attraction():
    """Добавляет достопримечательность"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        name = input("Введите название достопримечательности: ")
        description = input("Введите описание: ")
        
        if not name.strip():
            print("Ошибка: Название не может быть пустым!")
            return
        
        for trip in trips:
            if trip['id'] == trip_id:
                attraction = {
                    'id': len(attractions) + 1,
                    'trip_id': trip_id,
                    'trip_destination': trip['destination'],
                    'name': name,
                    'description': description,
                    'visit_date': '',
                    'estimated_cost': 0.0,
                    'priority': 'medium',  # high, medium, low
                    'visited': False
                }
                attractions.append(attraction)
                print(f"Достопримечательность '{name}' добавлена к поездке в '{trip['destination']}'!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_trip_attractions():
    """Показывает достопримечательности поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        trip_attractions = [a for a in attractions if a['trip_id'] == trip_id]
        
        if not trip_attractions:
            print("Для этой поездки нет достопримечательностей!")
            return
        
        print(f"\nДостопримечательности поездки:")
        print("-" * 60)
        
        for attraction in trip_attractions:
            status = "✅" if attraction['visited'] else "⏳"
            priority = "‼️" if attraction['priority'] == 'high' else \
                      "❗" if attraction['priority'] == 'medium' else ""
            
            print(f"{attraction['id']}. {status} {priority} {attraction['name']}")
            print(f"   Описание: {attraction['description']}")
            print(f"   Дата посещения: {attraction['visit_date'] or 'Не назначена'}")
            print(f"   Стоимость: {attraction['estimated_cost']:.2f}")
            print()

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def create_itinerary():
    """Создает маршрут для поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        day_number = int(input("Введите номер дня: "))
        
        for trip in trips:
            if trip['id'] == trip_id:
                print(f"\nСоздание маршрута для дня {day_number} поездки в '{trip['destination']}'")
                
                # Показываем доступные достопримечательности
                trip_attractions = [a for a in attractions if a['trip_id'] == trip_id and not a['visited']]
                
                if not trip_attractions:
                    print("Нет доступных достопримечательностей!")
                    return
                
                print("Доступные достопримечательности:")
                for attraction in trip_attractions:
                    print(f"{attraction['id']}. {attraction['name']}")
                
                attraction_ids_input = input("Введите ID достопримечательностей через запятую: ")
                attraction_ids = [int(id_str.strip()) for id_str in attraction_ids_input.split(',')]
                
                selected_attractions = []
                for attr_id in attraction_ids:
                    for attraction in trip_attractions:
                        if attraction['id'] == attr_id:
                            selected_attractions.append(attraction['name'])
                            break
                
                notes = input("Введите заметки для этого дня: ")
                
                itinerary = {
                    'id': len(itineraries) + 1,
                    'trip_id': trip_id,
                    'day_number': day_number,
                    'date': '',
                    'attractions': selected_attractions,
                    'notes': notes,
                    'estimated_cost': 0.0
                }
                itineraries.append(itinerary)
                print(f"Маршрут для дня {day_number} создан!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_trip_itinerary():
    """Показывает маршрут поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        trip_itineraries = sorted([i for i in itineraries if i['trip_id'] == trip_id], 
                                 key=lambda x: x['day_number'])
        
        if not trip_itineraries:
            print("Для этой поездки нет маршрута!")
            return
        
        for trip in trips:
            if trip['id'] == trip_id:
                print(f"\nМаршрут поездки в '{trip['destination']}':")
                print("=" * 60)
                
                for itinerary in trip_itineraries:
                    print(f"\nДень {itinerary['day_number']}:")
                    if itinerary['date']:
                        print(f"   Дата: {itinerary['date']}")
                    print(f"   Достопримечательности: {', '.join(itinerary['attractions'])}")
                    if itinerary['notes']:
                        print(f"   Заметки: {itinerary['notes']}")
                    print(f"   Примерная стоимость: {itinerary['estimated_cost']:.2f}")
                
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
         'status': 'planned', 'travelers': ['Анна', 'Иван']}
    ])
    
    # Демонстрация планирования
    add_attraction()
    show_trip_attractions()
    create_itinerary()
    show_trip_itinerary()

def add_expense():
    """Добавляет расход к поездке"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        category = input("Категория расхода (транспорт, жилье, еда, развлечения, другое): ")
        description = input("Описание расхода: ")
        amount = float(input("Сумма расхода: "))
        
        if amount <= 0:
            print("Ошибка: Сумма должна быть положительной!")
            return
        
        for trip in trips:
            if trip['id'] == trip_id:
                expense = {
                    'id': len(expenses) + 1,
                    'trip_id': trip_id,
                    'trip_destination': trip['destination'],
                    'category': category,
                    'description': description,
                    'amount': amount,
                    'date': '',
                    'payment_method': 'cash'  # cash, card, other
                }
                expenses.append(expense)
                print(f"Расход '{description}' на сумму {amount:.2f} добавлен!")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_trip_expenses():
    """Показывает расходы поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        trip_expenses = [e for e in expenses if e['trip_id'] == trip_id]
        
        if not trip_expenses:
            print("Для этой поездки нет расходов!")
            return
        
        total_expenses = sum(e['amount'] for e in trip_expenses)
        
        print(f"\nРасходы поездки:")
        print("-" * 60)
        print(f"{'Категория':<15} {'Описание':<20} {'Сумма':<10} {'Дата':<12}")
        print("-" * 60)
        
        for expense in trip_expenses:
            print(f"{expense['category']:<15} {expense['description']:<20} "
                  f"{expense['amount']:<10.2f} {expense['date']:<12}")
        
        print("-" * 60)
        print(f"Всего расходов: {total_expenses:.2f}")
        
        # Сравнение с бюджетом
        for trip in trips:
            if trip['id'] == trip_id:
                budget = trip['budget']
                if budget > 0:
                    remaining = budget - total_expenses
                    percentage = (total_expenses / budget) * 100
                    
                    print(f"\nБюджет: {budget:.2f}")
                    print(f"Потрачено: {total_expenses:.2f} ({percentage:.1f}%)")
                    print(f"Осталось: {remaining:.2f}")
                    
                    if percentage > 80:
                        print("⚠ Внимание: Бюджет почти исчерпан!")
                break
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_expenses_by_category():
    """Показывает расходы по категориям"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        trip_expenses = [e for e in expenses if e['trip_id'] == trip_id]
        
        if not trip_expenses:
            print("Для этой поездки нет расходов!")
            return
        
        # Группируем по категориям
        expenses_by_category = {}
        for expense in trip_expenses:
            category = expense['category']
            if category in expenses_by_category:
                expenses_by_category[category] += expense['amount']
            else:
                expenses_by_category[category] = expense['amount']
        
        total_expenses = sum(expenses_by_category.values())
        
        print(f"\nРасходы по категориям:")
        print("-" * 40)
        
        for category, amount in sorted(expenses_by_category.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0
            print(f"{category:<15} {amount:>8.2f} ({percentage:>5.1f}%)")
        
        print("-" * 40)
        print(f"Всего: {total_expenses:>23.2f}")
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def set_budget_alert():
    """Устанавливает предупреждение о бюджете"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        for trip in trips:
            if trip['id'] == trip_id:
                if trip['budget'] <= 0:
                    print("Ошибка: Сначала установите бюджет для поездки!")
                    return
                
                threshold = float(input("Установите порог предупреждения (например, 80 для 80%): "))
                
                if 0 < threshold < 100:
                    trip_expenses = sum(e['amount'] for e in expenses if e['trip_id'] == trip_id)
                    percentage = (trip_expenses / trip['budget']) * 100
                    
                    print(f"\nТекущие расходы: {trip_expenses:.2f}")
                    print(f"Бюджет: {trip['budget']:.2f}")
                    print(f"Использовано: {percentage:.1f}%")
                    
                    if percentage >= threshold:
                        print(f"⚠ Предупреждение: Превышен порог в {threshold}%!")
                    else:
                        remaining_percent = threshold - percentage
                        print(f"До предупреждения осталось: {remaining_percent:.1f}%")
                else:
                    print("Ошибка: Порог должен быть между 1 и 99%")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def main():
    print("Добро пожаловать в планировщик путешествий!")
    
    # Тестовые данные
    trips.extend([
        {'id': 1, 'destination': 'Париж', 'description': 'Романтическое путешествие', 
         'start_date': '2024-06-01', 'end_date': '2024-06-07', 'budget': 1500.00,
         'status': 'planned', 'travelers': ['Анна', 'Иван']}
    ])
    
    expenses.extend([
        {'id': 1, 'trip_id': 1, 'trip_destination': 'Париж', 
         'category': 'транспорт', 'description': 'Авиабилеты', 
         'amount': 600.00, 'date': '2024-05-15', 'payment_method': 'card'},
        {'id': 2, 'trip_id': 1, 'trip_destination': 'Париж',
         'category': 'жилье', 'description': 'Отель', 
         'amount': 400.00, 'date': '2024-05-20', 'payment_method': 'card'}
    ])
    
    # Демонстрация управления бюджетом
    add_expense()
    show_trip_expenses()
    show_expenses_by_category()
    set_budget_alert()

def create_packing_list():
    """Создает список упаковки для поездки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        for trip in trips:
            if trip['id'] == trip_id:
                print(f"\nСоздание списка упаковки для поездки в '{trip['destination']}'")
                
                packing_list = {
                    'id': len(packing_lists) + 1,
                    'trip_id': trip_id,
                    'items': [],
                    'categories': ['одежда', 'обувь', 'гигиена', 'документы', 'электроника', 'другое']
                }
                
                print("Добавьте предметы для упаковки (введите 'готово' для завершения):")
                
                while True:
                    item_name = input("Название предмета: ")
                    if item_name.lower() == 'готово':
                        break
                    
                    print("Категории:")
                    for i, category in enumerate(packing_list['categories'], 1):
                        print(f"   {i}. {category}")
                    
                    try:
                        category_choice = int(input("Выберите категорию (номер): ")) - 1
                        if 0 <= category_choice < len(packing_list['categories']):
                            category = packing_list['categories'][category_choice]
                        else:
                            category = 'другое'
                    except ValueError:
                        category = 'другое'
                    
                    quantity = input("Количество (по умолчанию 1): ") or "1"
                    
                    try:
                        quantity_int = int(quantity)
                    except ValueError:
                        quantity_int = 1
                    
                    item = {
                        'name': item_name,
                        'category': category,
                        'quantity': quantity_int,
                        'packed': False
                    }
                    
                    packing_list['items'].append(item)
                
                packing_lists.append(packing_list)
                print(f"Список упаковки создан! Предметов: {len(packing_list['items'])}")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_packing_list():
    """Показывает список упаковки"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        packing_list = next((pl for pl in packing_lists if pl['trip_id'] == trip_id), None)
        
        if not packing_list or not packing_list['items']:
            print("Для этой поездки нет списка упаковки!")
            return
        
        print(f"\nСписок упаковки:")
        print("=" * 60)
        
        packed_count = sum(1 for item in packing_list['items'] if item['packed'])
        total_count = len(packing_list['items'])
        progress = (packed_count / total_count) * 100 if total_count > 0 else 0
        
        print(f"Прогресс упаковки: {packed_count}/{total_count} ({progress:.1f}%)")
        print("-" * 60)
        
        # Группируем по категориям
        items_by_category = {}
        for item in packing_list['items']:
            category = item['category']
            if category not in items_by_category:
                items_by_category[category] = []
            items_by_category[category].append(item)
        
        for category, items in items_by_category.items():
            print(f"\n{category.upper()}:")
            for item in items:
                status = "✅" if item['packed'] else "📦"
                print(f"   {status} {item['name']} x{item['quantity']}")
        
        print("-" * 60)
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def mark_item_packed():
    """Отмечает предмет как упакованный"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        packing_list = next((pl for pl in packing_lists if pl['trip_id'] == trip_id), None)
        
        if not packing_list or not packing_list['items']:
            print("Для этой поездки нет списка упаковки!")
            return
        
        print("Предметы для упаковки:")
        for i, item in enumerate(packing_list['items'], 1):
            status = "✅" if item['packed'] else "📦"
            print(f"{i}. {status} {item['name']} x{item['quantity']}")
        
        item_choice = int(input("Введите номер предмета для отметки: ")) - 1
        
        if 0 <= item_choice < len(packing_list['items']):
            item = packing_list['items'][item_choice]
            item['packed'] = not item['packed']
            status = "упакован" if item['packed'] else "не упакован"
            print(f"Предмет '{item['name']}' отмечен как {status}!")
        else:
            print("Ошибка: Неверный номер предмета!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def create_pre_trip_checklist():
    """Создает предпоездочный контрольный список"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        for trip in trips:
            if trip['id'] == trip_id:
                print(f"\nСоздание контрольного списка для поездки в '{trip['destination']}'")
                
                default_tasks = [
                    'Забронировать билеты',
                    'Забронировать жилье',
                    'Оформить страховку',
                    'Проверить паспорт/визу',
                    'Обменять валюту',
                    'Скачать карты',
                    'Уведомить банк о поездке',
                    'Загрузить развлечения'
                ]
                
                checklist = {
                    'id': len(checklists) + 1,
                    'trip_id': trip_id,
                    'tasks': [],
                    'completed': False
                }
                
                print("Добавьте задачи (введите 'готово' для завершения):")
                print("Или нажмите Enter для использования стандартных задач")
                
                use_default = input("Использовать стандартные задачи? (y/n): ").lower()
                
                if use_default == 'y':
                    for task in default_tasks:
                        checklist['tasks'].append({
                            'description': task,
                            'completed': False,
                            'due_date': ''
                        })
                else:
                    while True:
                        task_desc = input("Описание задачи: ")
                        if task_desc.lower() == 'готово':
                            break
                        
                        checklist['tasks'].append({
                            'description': task_desc,
                            'completed': False,
                            'due_date': ''
                        })
                
                checklists.append(checklist)
                print(f"Контрольный список создан! Задач: {len(checklist['tasks'])}")
                return
        
        print(f"Ошибка: Поездка с ID {trip_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_checklist():
    """Показывает контрольный список"""
    show_all_trips()
    
    try:
        trip_id = int(input("Введите ID поездки: "))
        
        checklist = next((cl for cl in checklists if cl['trip_id'] == trip_id), None)
        
        if not checklist or not checklist['tasks']:
            print("Для этой поездки нет контрольного списка!")
            return
        
        completed_tasks = sum(1 for task in checklist['tasks'] if task['completed'])
        total_tasks = len(checklist['tasks'])
        progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        
        print(f"\nКонтрольный список:")
        print("=" * 60)
        print(f"Прогресс: {completed_tasks}/{total_tasks} ({progress:.1f}%)")
        print("-" * 60)
        
        for i, task in enumerate(checklist['tasks'], 1):
            status = "✅" if task['completed'] else "⏳"
            print(f"{i}. {status} {task['description']}")
            if task['due_date']:
                print(f"   Срок: {task['due_date']}")
        
        print("-" * 60)
        
        if progress == 100:
            print("🎉 Все задачи выполнены! Готовы к поездке!")
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в планировщик путешествий!")
    
    # Тестовые данные
    trips.extend([
        {'id': 1, 'destination': 'Париж', 'description': 'Романтическое путешествие', 
         'start_date': '2024-06-01', 'end_date': '2024-06-07', 'budget': 1500.00,
         'status': 'planned', 'travelers': ['Анна', 'Иван']}
    ])
    
    # Демонстрация упаковки и чеклистов
    create_packing_list()
    show_packing_list()
    mark_item_packed()
    create_pre_trip_checklist()
    show_checklist()

if __name__ == "__main__":
    main()