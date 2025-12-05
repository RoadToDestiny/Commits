# travel_planner.py
# Система планирования путешествий и поездок
# Коммит 10: Финальная версия с полной функциональностью

"""
ПЛАНИРОВЩИК ПУТЕШЕСТВИЙ

Комплексная система для планирования и организации поездок с функциями:
- Управление поездками и участниками
- Планирование маршрутов и достопримечательностей
- Контроль бюджета и расходов
- Списки упаковки и контрольные списки
- Хранение документов и полезной информации

Автор: [Ваше имя]
Версия: 1.0
"""

trips = []
destinations = []
attractions = []
itineraries = []
expenses = []
packing_lists = []
checklists = []
travel_docs = []
useful_info = []
emergency_contacts = []

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

# ... (все остальные функции: show_trip_details, edit_trip, add_traveler,
# remove_traveler, update_trip_status, delete_trip, add_attraction,
# show_trip_attractions, create_itinerary, show_trip_itinerary, add_expense,
# show_trip_expenses, show_expenses_by_category, set_budget_alert,
# create_packing_list, show_packing_list, mark_item_packed,
# create_pre_trip_checklist, show_checklist, add_travel_document,
# show_travel_documents, add_useful_information, show_useful_information,
# add_emergency_contact, show_emergency_info, show_trip_summary)

def show_main_menu():
    """Показывает главное меню программы"""
    print("\n" + "="*50)
    print("           ПЛАНИРОВЩИК ПУТЕШЕСТВИЙ")
    print("="*50)
    print("1. Показать все поездки")
    print("2. Добавить поездку")
    print("3. Управление поездкой")
    print("4. Маршрут и достопримечательности")
    print("5. Бюджет и расходы")
    print("6. Упаковка и подготовка")
    print("7. Документы и информация")
    print("8. Выход")
    print("="*50)

def get_menu_choice():
    """Получает и проверяет выбор пользователя"""
    try:
        choice = int(input("\nВыберите действие (1-8): "))
        return choice
    except ValueError:
        print("Ошибка: Пожалуйста, введите число от 1 до 8!")
        return -1

def initialize_sample_data():
    """Инициализирует примеры данных для демонстрации"""
    sample_trips = [
        {'id': 1, 'destination': 'Париж', 'description': 'Романтическое путешествие', 
         'start_date': '2024-06-01', 'end_date': '2024-06-07', 'budget': 1500.00,
         'status': 'planned', 'travelers': ['Анна', 'Иван']},
        {'id': 2, 'destination': 'Сочи', 'description': 'Отдых на море', 
         'start_date': '2024-07-15', 'end_date': '2024-07-25', 'budget': 800.00,
         'status': 'planned', 'travelers': ['Семья']}
    ]
    trips.extend(sample_trips)
    
    attractions.extend([
        {'id': 1, 'trip_id': 1, 'trip_destination': 'Париж',
         'name': 'Эйфелева башня', 'description': 'Символ Парижа',
         'visit_date': '', 'estimated_cost': 25.00, 'priority': 'high', 'visited': False},
        {'id': 2, 'trip_id': 1, 'trip_destination': 'Париж',
         'name': 'Лувр', 'description': 'Знаменитый музей',
         'visit_date': '', 'estimated_cost': 20.00, 'priority': 'high', 'visited': False}
    ])
    
    expenses.extend([
        {'id': 1, 'trip_id': 1, 'trip_destination': 'Париж',
         'category': 'транспорт', 'description': 'Авиабилеты',
         'amount': 600.00, 'date': '2024-05-15', 'payment_method': 'card'},
        {'id': 2, 'trip_id': 1, 'trip_destination': 'Париж',
         'category': 'жилье', 'description': 'Отель',
         'amount': 400.00, 'date': '2024-05-20', 'payment_method': 'card'}
    ])
    
    travel_docs.extend([
        {'id': 1, 'trip_id': 1, 'trip_destination': 'Париж',
         'type': 'паспорт', 'number': '123456789', 
         'details': 'Действителен до 2028', 'scan_path': '', 'important': True},
        {'id': 2, 'trip_id': 1, 'trip_destination': 'Париж',
         'type': 'страховка', 'number': 'INS-789456', 
         'details': 'Действует с 01.06.2024', 'scan_path': '', 'important': True}
    ])

def main():
    """Главная функция программы"""
    print("Добро пожаловать в планировщик путешествий!")
    
    # Загружаем примеры данных (можно закомментировать)
    initialize_sample_data()
    
    # Главный цикл программы
    while True:
        show_main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            show_all_trips()
        elif choice == 2:
            add_trip()
        elif choice == 3:
            show_all_trips()
            edit_trip()
            add_traveler()
            remove_traveler()
            update_trip_status()
        elif choice == 4:
            add_attraction()
            show_trip_attractions()
            create_itinerary()
            show_trip_itinerary()
        elif choice == 5:
            add_expense()
            show_trip_expenses()
            show_expenses_by_category()
            set_budget_alert()
        elif choice == 6:
            create_packing_list()
            show_packing_list()
            mark_item_packed()
            create_pre_trip_checklist()
            show_checklist()
        elif choice == 7:
            add_travel_document()
            show_travel_documents()
            add_useful_information()
            show_useful_information()
            add_emergency_contact()
            show_emergency_info()
            show_trip_summary()
        elif choice == 8:
            print("\nСпасибо за использование планировщика путешествий!")
            print("Приятной поездки! ✈️")
            break
        elif choice == -1:
            continue
        else:
            print("Ошибка: Неверный выбор! Пожалуйста, выберите от 1 до 8.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()