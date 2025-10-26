# library_manager.py
# Система учета книг в домашней библиотеке
# Коммит 10: Финальная версия с полной функциональностью

"""
СИСТЕМА УЧЕТА ДОМАШНЕЙ БИБЛИОТЕКИ

Расширенная система для учета личной библиотеки с функциями:
- Учет книг с полной информацией
- Поиск и фильтрация
- Статистика и аналитика
- Рейтинги и отзывы
- Рекомендательная система

Автор: [Ваше имя]
Версия: 1.0
"""

books = []

def add_book():
    """Добавляет новую книгу в библиотеку"""
    print("\nДобавление новой книги:")
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания (необязательно): ")
    genre = input("Введите жанр (необязательно): ")
    
    if title.strip() and author.strip():
        book = {
            'id': len(books) + 1,
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': False
        }
        books.append(book)
        print(f"Книга '{title}' добавлена в библиотеку!")
    else:
        print("Ошибка: Название и автор не могут быть пустыми!")

def show_all_books():
    """Показывает все книги в библиотеке"""
    if not books:
        print("Библиотека пуста!")
        return
    
    print("\nВсе книги в библиотеке:")
    print("-" * 70)
    
    for book in books:
        status = "[ПРОЧИТАНА]" if book['read'] else "[НЕ ПРОЧИТАНА]"
        rating = f" Рейтинг: {book['rating']}/5" if 'rating' in book else ""
        print(f"{book['id']:2d}. '{book['title']}' - {book['author']} {status}{rating}")
    
    print("-" * 70)
    print(f"Всего книг: {len(books)}")

# ... (все остальные функции: edit_book, mark_as_read, delete_book, search_books,
# filter_books, show_statistics, show_reading_progress, add_rating, add_review,
# show_rated_books, get_recommendations, show_random_book, show_reading_challenge)

def show_main_menu():
    """Показывает главное меню программы"""
    print("\n" + "="*50)
    print("       СИСТЕМА УЧЕТА ДОМАШНЕЙ БИБЛИОТЕКИ")
    print("="*50)
    print("1. Показать все книги")
    print("2. Добавить книгу")
    print("3. Редактировать книгу")
    print("4. Удалить книгу")
    print("5. Отметить как прочитанную")
    print("6. Поиск книг")
    print("7. Фильтр книг")
    print("8. Статистика")
    print("9. Рейтинги и отзывы")
    print("10. Рекомендации")
    print("11. Выход")
    print("="*50)

def get_menu_choice():
    """Получает и проверяет выбор пользователя"""
    try:
        choice = int(input("\nВыберите действие (1-11): "))
        return choice
    except ValueError:
        print("Ошибка: Пожалуйста, введите число от 1 до 11!")
        return -1

def initialize_sample_data():
    """Инициализирует примеры книг для демонстрации"""
    sample_books = [
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True, 'rating': 5, 'review': 'Шедевр мировой литературы'},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': True, 'rating': 4},
        {'id': 3, 'title': 'Скотный двор', 'author': 'Джордж Оруэлл', 'year': '1945', 'genre': 'Сатира', 'read': False},
        {'id': 4, 'title': 'Преступление и наказание', 'author': 'Федор Достоевский', 'year': '1866', 'genre': 'Роман', 'read': False},
        {'id': 5, 'title': 'Война и мир', 'author': 'Лев Толстой', 'year': '1869', 'genre': 'Роман', 'read': False}
    ]
    books.extend(sample_books)

def main():
    """Главная функция программы"""
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Загружаем примеры данных (можно закомментировать)
    initialize_sample_data()
    
    # Главный цикл программы
    while True:
        show_main_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            show_all_books()
        elif choice == 2:
            add_book()
        elif choice == 3:
            edit_book()
        elif choice == 4:
            delete_book()
        elif choice == 5:
            mark_as_read()
        elif choice == 6:
            search_books()
        elif choice == 7:
            filter_books()
        elif choice == 8:
            show_statistics()
            show_reading_progress()
        elif choice == 9:
            show_rated_books()
            add_rating()
            add_review()
        elif choice == 10:
            get_recommendations()
            show_random_book()
            show_reading_challenge()
        elif choice == 11:
            print("\nСпасибо за использование системы учета библиотеки!")
            print("До свидания!")
            break
        elif choice == -1:
            continue
        else:
            print("Ошибка: Неверный выбор! Пожалуйста, выберите от 1 до 11.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()