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






if __name__ == "__main__":
    main()