# course_manager.py
# Система управления учебными курсами и прогрессом
# Коммит 1: Базовая структура проекта

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    print("Система находится в разработке...")

# Глобальные переменные для хранения данных
courses = []
categories = ['Программирование', 'Математика', 'Иностранные языки', 'Дизайн', 'Маркетинг', 'Другое']

def add_course():
    """Добавляет новый учебный курс"""
    name = input("Введите название курса: ")
    description = input("Введите описание курса: ")
    
    if name.strip():
        course = {
            'id': len(courses) + 1,
            'name': name,
            'description': description,
            'category': '',
            'total_lessons': 0,
            'completed_lessons': 0,
            'status': 'active',  # active, completed, paused
            'progress': 0.0
        }
        courses.append(course)
        print(f"Курс '{name}' добавлен!")
    else:
        print("Ошибка: Название курса не может быть пустым!")

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Тестируем добавление курсов
    add_course()
    print(f"Всего курсов: {len(courses)}")

def add_course():
    """Добавляет новый учебный курс"""
    name = input("Введите название курса: ")
    description = input("Введите описание курса: ")
    
    if name.strip():
        course = {
            'id': len(courses) + 1,
            'name': name,
            'description': description,
            'category': '',
            'total_lessons': 0,
            'completed_lessons': 0,
            'status': 'active',  # active, completed, paused
            'progress': 0.0
        }
        courses.append(course)
        print(f"Курс '{name}' добавлен!")
    else:
        print("Ошибка: Название курса не может быть пустым!")

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Тестируем добавление курсов
    add_course()
    print(f"Всего курсов: {len(courses)}")

def show_all_courses():
    """Показывает все курсы"""
    if not courses:
        print("Список курсов пуст!")
        return
    
    print("\nВсе курсы:")
    print("-" * 80)
    print(f"{'ID':<3} {'Название':<20} {'Категория':<15} {'Прогресс':<10} {'Статус':<10}")
    print("-" * 80)
    
    for course in courses:
        progress_percent = course['progress'] * 100
        print(f"{course['id']:<3} {course['name']:<20} {course['category']:<15} "
              f"{progress_percent:>6.1f}%   {course['status']:<10}")
    
    print("-" * 80)

def show_course_details(course_id):
    """Показывает детальную информацию о курсе"""
    for course in courses:
        if course['id'] == course_id:
            progress_percent = course['progress'] * 100
            print(f"\nДетали курса #{course_id}:")
            print(f"   Название: {course['name']}")
            print(f"   Описание: {course['description']}")
            print(f"   Категория: {course['category']}")
            print(f"   Уроков: {course['completed_lessons']}/{course['total_lessons']}")
            print(f"   Прогресс: {progress_percent:.1f}%")
            print(f"   Статус: {course['status']}")
            return
    
    print(f"Ошибка: Курс с ID {course_id} не найден!")

def edit_course():
    """Редактирует информацию о курсе"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса для редактирования: "))
        
        for course in courses:
            if course['id'] == course_id:
                print(f"\nРедактирование курса: '{course['name']}'")
                course['name'] = input(f"Новое название [{course['name']}]: ") or course['name']
                course['description'] = input(f"Новое описание [{course['description']}]: ") or course['description']
                
                print("\nКатегории:")
                for i, category in enumerate(categories, 1):
                    print(f"   {i}. {category}")
                
                category_choice = input(f"Новая категория [{course['category']}]: ")
                if category_choice.isdigit():
                    choice = int(category_choice) - 1
                    if 0 <= choice < len(categories):
                        course['category'] = categories[choice]
                
                print("Курс успешно обновлен!")
                return
        
        print(f"Ошибка: Курс с ID {course_id} не найден!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Добавляем тестовые курсы
    courses.extend([
        {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы программирования на Python', 
         'category': 'Программирование', 'total_lessons': 10, 'completed_lessons': 3, 
         'status': 'active', 'progress': 0.3},
        {'id': 2, 'name': 'Английский язык', 'description': 'Курс английского для IT', 
         'category': 'Иностранные языки', 'total_lessons': 20, 'completed_lessons': 15, 
         'status': 'active', 'progress': 0.75}
    ])
    
    # Демонстрация новых функций
    show_all_courses()
    show_course_details(1)
    edit_course()

def add_lessons_to_course():
    """Добавляет уроки к курсу"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса: "))
        lessons_count = int(input("Введите количество уроков в курсе: "))
        
        if lessons_count <= 0:
            print("Ошибка: Количество уроков должно быть положительным!")
            return
        
        for course in courses:
            if course['id'] == course_id:
                course['total_lessons'] = lessons_count
                course['progress'] = course['completed_lessons'] / lessons_count if lessons_count > 0 else 0
                print(f"К курсу '{course['name']}' добавлено {lessons_count} уроков!")
                return
        
        print(f"Ошибка: Курс с ID {course_id} не найден!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные числа!")

def mark_lesson_completed():
    """Отмечает урок как завершенный"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса: "))
        
        for course in courses:
            if course['id'] == course_id:
                if course['total_lessons'] == 0:
                    print("Ошибка: Сначала добавьте уроки к курсу!")
                    return
                
                course['completed_lessons'] += 1
                course['progress'] = course['completed_lessons'] / course['total_lessons']
                
                # Проверяем, завершен ли курс
                if course['completed_lessons'] >= course['total_lessons']:
                    course['status'] = 'completed'
                    print(f"Поздравляем! Курс '{course['name']}' завершен!")
                else:
                    print(f"Урок отмечен как завершенный! Прогресс: {course['progress']*100:.1f}%")
                return
        
        print(f"Ошибка: Курс с ID {course_id} не найден!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def update_course_status():
    """Обновляет статус курса"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса: "))
        
        print("\nДоступные статусы:")
        print("1. active - активный")
        print("2. completed - завершенный")
        print("3. paused - приостановлен")
        
        status_choice = int(input("Выберите статус (1-3): "))
        
        status_map = {1: 'active', 2: 'completed', 3: 'paused'}
        
        if status_choice in status_map:
            for course in courses:
                if course['id'] == course_id:
                    course['status'] = status_map[status_choice]
                    print(f"Статус курса '{course['name']}' изменен на '{status_map[status_choice]}'")
                    return
            
            print(f"Ошибка: Курс с ID {course_id} не найден!")
        else:
            print("Ошибка: Неверный выбор статуса!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Тестовые данные
    courses.extend([
        {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы программирования на Python', 
         'category': 'Программирование', 'total_lessons': 10, 'completed_lessons': 3, 
         'status': 'active', 'progress': 0.3}
    ])
    
    # Демонстрация управления уроками
    add_lessons_to_course()
    mark_lesson_completed()
    update_course_status()
    show_all_courses()

def show_learning_statistics():
    """Показывает статистику обучения"""
    if not courses:
        print("Нет данных для статистики!")
        return
    
    total_courses = len(courses)
    completed_courses = len([c for c in courses if c['status'] == 'completed'])
    active_courses = len([c for c in courses if c['status'] == 'active'])
    paused_courses = len([c for c in courses if c['status'] == 'paused'])
    
    total_lessons = sum(c['total_lessons'] for c in courses)
    completed_lessons = sum(c['completed_lessons'] for c in courses)
    
    print("\nСтатистика обучения:")
    print("-" * 40)
    print(f"Всего курсов: {total_courses}")
    print(f"Завершено курсов: {completed_courses}")
    print(f"Активных курсов: {active_courses}")
    print(f"Приостановленных курсов: {paused_courses}")
    print(f"Всего уроков: {total_lessons}")
    print(f"Завершено уроков: {completed_lessons}")
    
    if total_lessons > 0:
        overall_progress = (completed_lessons / total_lessons) * 100
        print(f"Общий прогресс: {overall_progress:.1f}%")

def show_progress_by_category():
    """Показывает прогресс по категориям"""
    if not courses:
        print("Нет данных для анализа!")
        return
    
    category_stats = {}
    
    for course in courses:
        category = course['category']
        if category not in category_stats:
            category_stats[category] = {
                'courses': 0,
                'completed_courses': 0,
                'total_lessons': 0,
                'completed_lessons': 0
            }
        
        category_stats[category]['courses'] += 1
        category_stats[category]['total_lessons'] += course['total_lessons']
        category_stats[category]['completed_lessons'] += course['completed_lessons']
        
        if course['status'] == 'completed':
            category_stats[category]['completed_courses'] += 1
    
    print("\nПрогресс по категориям:")
    print("-" * 60)
    print(f"{'Категория':<20} {'Курсы':<8} {'Завершено':<10} {'Уроки':<8} {'Прогресс':<10}")
    print("-" * 60)
    
    for category, stats in category_stats.items():
        if stats['total_lessons'] > 0:
            progress = (stats['completed_lessons'] / stats['total_lessons']) * 100
        else:
            progress = 0
        
        print(f"{category:<20} {stats['courses']:<8} {stats['completed_courses']:<10} "
              f"{stats['completed_lessons']}/{stats['total_lessons']:<8} {progress:>6.1f}%")

def show_recent_progress():
    """Показывает недавний прогресс"""
    active_courses = [c for c in courses if c['status'] == 'active']
    
    if not active_courses:
        print("Нет активных курсов!")
        return
    
    print("\nАктивные курсы (прогресс):")
    print("-" * 50)
    
    for course in active_courses:
        progress_percent = course['progress'] * 100
        remaining_lessons = course['total_lessons'] - course['completed_lessons']
        
        print(f"{course['name']}")
        print(f"   Прогресс: {progress_percent:.1f}% ({course['completed_lessons']}/{course['total_lessons']} уроков)")
        print(f"   Осталось уроков: {remaining_lessons}")
        print()

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Тестовые данные для статистики
    courses.extend([
        {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы программирования на Python', 
         'category': 'Программирование', 'total_lessons': 10, 'completed_lessons': 3, 
         'status': 'active', 'progress': 0.3},
        {'id': 2, 'name': 'Английский язык', 'description': 'Курс английского для IT', 
         'category': 'Иностранные языки', 'total_lessons': 20, 'completed_lessons': 15, 
         'status': 'active', 'progress': 0.75},
        {'id': 3, 'name': 'Веб-дизайн', 'description': 'Основы веб-дизайна', 
         'category': 'Дизайн', 'total_lessons': 15, 'completed_lessons': 15, 
         'status': 'completed', 'progress': 1.0}
    ])
    
    # Демонстрация статистики
    show_learning_statistics()
    show_progress_by_category()
    show_recent_progress()

def add_reminder():
    """Добавляет напоминание для курса"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса: "))
        reminder_text = input("Введите текст напоминания: ")
        deadline = input("Введите дедлайн (ГГГГ-ММ-ДД): ")
        
        if not reminder_text.strip():
            print("Ошибка: Текст напоминания не может быть пустым!")
            return
        
        for course in courses:
            if course['id'] == course_id:
                reminder = {
                    'id': len(reminders) + 1,
                    'course_id': course_id,
                    'course_name': course['name'],
                    'text': reminder_text,
                    'deadline': deadline,
                    'completed': False
                }
                reminders.append(reminder)
                print(f"Напоминание для курса '{course['name']}' добавлено!")
                return
        
        print(f"Ошибка: Курс с ID {course_id} не найден!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_reminders():
    """Показывает все напоминания"""
    if not reminders:
        print("Нет активных напоминаний!")
        return
    
    active_reminders = [r for r in reminders if not r['completed']]
    completed_reminders = [r for r in reminders if r['completed']]
    
    if active_reminders:
        print("\nАктивные напоминания:")
        print("-" * 60)
        for reminder in active_reminders:
            status = "ПРОСРОЧЕНО" if is_overdue(reminder['deadline']) else "АКТИВНО"
            print(f"{reminder['id']}. Курс: {reminder['course_name']}")
            print(f"   Напоминание: {reminder['text']}")
            print(f"   Дедлайн: {reminder['deadline']} [{status}]")
            print()
    
    if completed_reminders:
        print("\nЗавершенные напоминания:")
        for reminder in completed_reminders:
            print(f"{reminder['id']}. {reminder['course_name']} - {reminder['text']}")

def mark_reminder_completed():
    """Отмечает напоминание как выполненное"""
    show_reminders()
    
    try:
        reminder_id = int(input("Введите ID напоминания для завершения: "))
        
        for reminder in reminders:
            if reminder['id'] == reminder_id and not reminder['completed']:
                reminder['completed'] = True
                print(f"Напоминание '{reminder['text']}' отмечено как выполненное!")
                return
        
        print(f"Ошибка: Напоминание с ID {reminder_id} не найдено или уже завершено!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def is_overdue(deadline):
    """Проверяет, просрочен ли дедлайн"""
    # Упрощенная проверка (в реальном приложении использовалась бы datetime)
    return deadline < '2024-01-15'  # Пример текущей даты

def show_study_recommendations():
    """Показывает рекомендации по обучению"""
    if not courses:
        print("Нет данных для рекомендаций!")
        return
    
    # Рекомендации на основе прогресса
    low_progress_courses = [c for c in courses if c['status'] == 'active' and c['progress'] < 0.3]
    almost_completed_courses = [c for c in courses if c['status'] == 'active' and c['progress'] > 0.7]
    
    print("\nРекомендации по обучению:")
    print("-" * 40)
    
    if low_progress_courses:
        print("Курсы с низким прогрессом (рекомендуется уделить внимание):")
        for course in low_progress_courses:
            print(f"   • {course['name']} ({course['progress']*100:.1f}%)")
    
    if almost_completed_courses:
        print("\nКурсы, близкие к завершению (можно закончить в ближайшее время):")
        for course in almost_completed_courses:
            remaining = course['total_lessons'] - course['completed_lessons']
            print(f"   • {course['name']} (осталось {remaining} уроков)")
    
    # Рекомендации по напоминаниям
    active_reminders = [r for r in reminders if not r['completed']]
    overdue_reminders = [r for r in active_reminders if is_overdue(r['deadline'])]
    
    if overdue_reminders:
        print("\nПРОСРОЧЕННЫЕ НАПОМИНАНИЯ:")
        for reminder in overdue_reminders:
            print(f"   ⚠ {reminder['course_name']}: {reminder['text']}")

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Тестовые данные
    courses.extend([
        {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы программирования на Python', 
         'category': 'Программирование', 'total_lessons': 10, 'completed_lessons': 2, 
         'status': 'active', 'progress': 0.2}
    ])
    
    reminders.extend([
        {'id': 1, 'course_id': 1, 'course_name': 'Python для начинающих', 
         'text': 'Завершить первые 5 уроков', 'deadline': '2024-01-10', 'completed': False},
        {'id': 2, 'course_id': 1, 'course_name': 'Python для начинающих', 
         'text': 'Сделать практическое задание', 'deadline': '2024-01-20', 'completed': False}
    ])
    
    # Демонстрация системы напоминаний
    add_reminder()
    show_reminders()
    mark_reminder_completed()
    show_study_recommendations()

def add_note():
    """Добавляет заметку к курсу"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса: "))
        note_text = input("Введите текст заметки: ")
        lesson_number = input("Введите номер урока (необязательно): ")
        
        if not note_text.strip():
            print("Ошибка: Текст заметки не может быть пустым!")
            return
        
        for course in courses:
            if course['id'] == course_id:
                note = {
                    'id': len(notes) + 1,
                    'course_id': course_id,
                    'course_name': course['name'],
                    'text': note_text,
                    'lesson_number': lesson_number,
                    'created_date': '2024-01-01'
                }
                notes.append(note)
                print(f"Заметка для курса '{course['name']}' добавлена!")
                return
        
        print(f"Ошибка: Курс с ID {course_id} не найден!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_notes():
    """Показывает все заметки"""
    if not notes:
        print("Нет заметок!")
        return
    
    print("\nВсе заметки:")
    print("-" * 60)
    
    for note in notes:
        lesson_info = f" (Урок {note['lesson_number']})" if note['lesson_number'] else ""
        print(f"{note['id']}. Курс: {note['course_name']}{lesson_info}")
        print(f"   Заметка: {note['text']}")
        print(f"   Дата: {note['created_date']}")
        print()

def add_material():
    """Добавляет учебный материал"""
    show_all_courses()
    
    try:
        course_id = int(input("Введите ID курса: "))
        material_type = input("Тип материала (книга, статья, видео, ссылка): ")
        title = input("Название материала: ")
        description = input("Описание: ")
        url = input("Ссылка (необязательно): ")
        
        if not title.strip():
            print("Ошибка: Название материала не может быть пустым!")
            return
        
        for course in courses:
            if course['id'] == course_id:
                material = {
                    'id': len(materials) + 1,
                    'course_id': course_id,
                    'course_name': course['name'],
                    'type': material_type,
                    'title': title,
                    'description': description,
                    'url': url,
                    'completed': False
                }
                materials.append(material)
                print(f"Материал '{title}' добавлен к курсу '{course['name']}'!")
                return
        
        print(f"Ошибка: Курс с ID {course_id} не найден!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные данные!")

def show_materials():
    """Показывает все учебные материалы"""
    if not materials:
        print("Нет учебных материалов!")
        return
    
    print("\nУчебные материалы:")
    print("-" * 70)
    
    for material in materials:
        status = "[ПРОЧИТАНО]" if material['completed'] else "[НЕ ПРОЧИТАНО]"
        print(f"{material['id']}. Курс: {material['course_name']}")
        print(f"   {material['type'].upper()}: {material['title']} {status}")
        print(f"   Описание: {material['description']}")
        if material['url']:
            print(f"   Ссылка: {material['url']}")
        print()

def mark_material_completed():
    """Отмечает материал как изученный"""
    show_materials()
    
    try:
        material_id = int(input("Введите ID материала для отметки: "))
        
        for material in materials:
            if material['id'] == material_id and not material['completed']:
                material['completed'] = True
                print(f"Материал '{material['title']}' отмечен как изученный!")
                return
        
        print(f"Ошибка: Материал с ID {material_id} не найден или уже изучен!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_course_resources(course_id):
    """Показывает все ресурсы курса (заметки и материалы)"""
    course_notes = [n for n in notes if n['course_id'] == course_id]
    course_materials = [m for m in materials if m['course_id'] == course_id]
    
    if not course_notes and not course_materials:
        print("Для этого курса нет ресурсов!")
        return
    
    for course in courses:
        if course['id'] == course_id:
            print(f"\nРесурсы курса: {course['name']}")
            
            if course_notes:
                print("\nЗаметки:")
                for note in course_notes:
                    lesson_info = f" (Урок {note['lesson_number']})" if note['lesson_number'] else ""
                    print(f"   • {note['text']}{lesson_info}")
            
            if course_materials:
                print("\nМатериалы:")
                for material in course_materials:
                    status = "✓" if material['completed'] else "○"
                    print(f"   {status} {material['type']}: {material['title']}")
            return
    
    print(f"Ошибка: Курс с ID {course_id} не найден!")

def main():
    print("Добро пожаловать в систему управления учебными курсами!")
    
    # Тестовые данные
    courses.extend([
        {'id': 1, 'name': 'Python для начинающих', 'description': 'Основы программирования на Python', 
         'category': 'Программирование', 'total_lessons': 10, 'completed_lessons': 3, 
         'status': 'active', 'progress': 0.3}
    ])
    
    # Демонстрация системы заметок и материалов
    add_note()
    add_material()
    show_notes()
    show_materials()
    mark_material_completed()
    show_course_resources(1)







if __name__ == "__main__":
    main()