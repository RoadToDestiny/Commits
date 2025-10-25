# library_manager.py
# Система учета книг в домашней библиотеке
# Коммит 1: Базовая структура проекта

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    print("Система находится в разработке...")

if __name__ == "__main__":
    main()

# Глобальный список для хранения книг
books = []

def add_book():
    """Добавляет новую книгу в библиотеку"""
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    
    if title.strip() and author.strip():
        book = {
            'id': len(books) + 1,
            'title': title,
            'author': author,
            'year': '',
            'genre': '',
            'read': False
        }
        books.append(book)
        print(f"Книга '{title}' добавлена в библиотеку!")
    else:
        print("Ошибка: Название и автор не могут быть пустыми!")

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Тестируем добавление книг
    add_book()
    print(f"Всего книг в библиотеке: {len(books)}")

def show_all_books():
    """Показывает все книги в библиотеке"""
    if not books:
        print("Библиотека пуста!")
        return
    
    print("\nВсе книги в библиотеке:")
    print("-" * 60)
    
    for book in books:
        status = "Прочитана" if book['read'] else "Не прочитана"
        print(f"{book['id']}. '{book['title']}' - {book['author']} [{status}]")
    
    print("-" * 60)

def show_book_details(book_id):
    """Показывает детальную информацию о книге"""
    for book in books:
        if book['id'] == book_id:
            print(f"\nДетали книги #{book_id}:")
            print(f"   Название: {book['title']}")
            print(f"   Автор: {book['author']}")
            print(f"   Год: {book['year'] or 'Не указан'}")
            print(f"   Жанр: {book['genre'] or 'Не указан'}")
            print(f"   Статус: {'Прочитана' if book['read'] else 'Не прочитана'}")
            return
    
    print(f"Ошибка: Книга с ID {book_id} не найдена!")

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Добавляем тестовые книги
    books.extend([
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': False}
    ])
    
    show_all_books()
    show_book_details(1)

def edit_book():
    """Редактирует информацию о книге"""
    show_all_books()
    
    try:
        book_id = int(input("Введите ID книги для редактирования: "))
        
        for book in books:
            if book['id'] == book_id:
                print(f"\nРедактирование книги: '{book['title']}'")
                book['title'] = input(f"Новое название [{book['title']}]: ") or book['title']
                book['author'] = input(f"Новый автор [{book['author']}]: ") or book['author']
                book['year'] = input(f"Год издания [{book['year']}]: ") or book['year']
                book['genre'] = input(f"Жанр [{book['genre']}]: ") or book['genre']
                
                print("Книга успешно обновлена!")
                return
        
        print(f"Ошибка: Книга с ID {book_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def mark_as_read():
    """Отмечает книгу как прочитанную"""
    show_all_books()
    
    try:
        book_id = int(input("Введите ID прочитанной книги: "))
        
        for book in books:
            if book['id'] == book_id:
                book['read'] = True
                print(f"Книга '{book['title']}' отмечена как прочитанная!")
                return
        
        print(f"Ошибка: Книга с ID {book_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def delete_book():
    """Удаляет книгу из библиотеки"""
    show_all_books()
    
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        
        for i, book in enumerate(books):
            if book['id'] == book_id:
                deleted_title = book['title']
                books.pop(i)
                print(f"Книга '{deleted_title}' удалена из библиотеки!")
                return
        
        print(f"Ошибка: Книга с ID {book_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Тестовые данные
    books.extend([
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': False}
    ])
    
    # Демонстрация новых функций
    edit_book()
    mark_as_read()
    delete_book()
    show_all_books()

def search_books():
    """Ищет книги по различным критериям"""
    print("\nПоиск книг:")
    print("1. По названию")
    print("2. По автору")
    print("3. По жанру")
    
    try:
        choice = int(input("Выберите критерий поиска: "))
        keyword = input("Введите ключевое слово: ").lower()
        
        found_books = []
        
        if choice == 1:
            found_books = [book for book in books if keyword in book['title'].lower()]
        elif choice == 2:
            found_books = [book for book in books if keyword in book['author'].lower()]
        elif choice == 3:
            found_books = [book for book in books if book['genre'] and keyword in book['genre'].lower()]
        else:
            print("Ошибка: Неверный выбор!")
            return
        
        if found_books:
            print(f"\nНайдено книг: {len(found_books)}")
            for book in found_books:
                status = "Прочитана" if book['read'] else "Не прочитана"
                print(f"   {book['id']}. '{book['title']}' - {book['author']} [{status}]")
        else:
            print("Книги не найдены!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите число!")

def filter_books():
    """Фильтрует книги по различным критериям"""
    print("\nФильтр книг:")
    print("1. Все книги")
    print("2. Только прочитанные")
    print("3. Только непрочитанные")
    print("4. По автору")
    
    try:
        choice = int(input("Выберите вариант фильтра: "))
        
        if choice == 1:
            show_all_books()
        elif choice == 2:
            read_books = [book for book in books if book['read']]
            if read_books:
                print("\nПрочитанные книги:")
                for book in read_books:
                    print(f"   {book['id']}. '{book['title']}' - {book['author']}")
            else:
                print("Нет прочитанных книг!")
        elif choice == 3:
            unread_books = [book for book in books if not book['read']]
            if unread_books:
                print("\nНепрочитанные книги:")
                for book in unread_books:
                    print(f"   {book['id']}. '{book['title']}' - {book['author']}")
            else:
                print("Все книги прочитаны!")
        elif choice == 4:
            author = input("Введите имя автора: ").lower()
            author_books = [book for book in books if author in book['author'].lower()]
            if author_books:
                print(f"\nКниги автора:")
                for book in author_books:
                    status = "Прочитана" if book['read'] else "Не прочитана"
                    print(f"   {book['id']}. '{book['title']}' [{status}]")
            else:
                print("Книги этого автора не найдены!")
        else:
            print("Ошибка: Неверный выбор!")
            
    except ValueError:
        print("Ошибка: Пожалуйста, введите число!")

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Тестовые данные
    books.extend([
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': False},
        {'id': 3, 'title': 'Скотный двор', 'author': 'Джордж Оруэлл', 'year': '1945', 'genre': 'Сатира', 'read': True}
    ])
    
    # Демонстрация поиска и фильтрации
    search_books()
    filter_books()    

def show_statistics():
    """Показывает статистику библиотеки"""
    if not books:
        print("Библиотека пуста! Нет данных для статистики.")
        return
    
    total_books = len(books)
    read_books = len([book for book in books if book['read']])
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print("\nСтатистика библиотеки:")
    print("-" * 30)
    print(f"Всего книг: {total_books}")
    print(f"Прочитано: {read_books}")
    print(f"Не прочитано: {unread_books}")
    print(f"Процент прочитанных: {read_percentage:.1f}%")
    
    # Статистика по авторам
    authors = {}
    for book in books:
        author = book['author']
        if author in authors:
            authors[author] += 1
        else:
            authors[author] = 1
    
    if authors:
        print(f"\nКниг по авторам:")
        for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
            print(f"   {author}: {count} книг")
    
    # Статистика по жанрам
    genres = {}
    for book in books:
        genre = book['genre']
        if genre:
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
    
    if genres:
        print(f"\nКниг по жанрам:")
        for genre, count in sorted(genres.items(), key=lambda x: x[1], reverse=True):
            print(f"   {genre}: {count} книг")

def show_reading_progress():
    """Показывает прогресс чтения"""
    if not books:
        print("Библиотека пуста!")
        return
    
    read_books = [book for book in books if book['read']]
    unread_books = [book for book in books if not book['read']]
    
    print("\nПрогресс чтения:")
    print("-" * 40)
    
    if read_books:
        print("Прочитанные книги:")
        for book in read_books[:5]:  # Показываем только первые 5
            print(f"   ✓ '{book['title']}' - {book['author']}")
        if len(read_books) > 5:
            print(f"   ... и еще {len(read_books) - 5} книг")
    
    if unread_books:
        print("\nСледующие для чтения:")
        for book in unread_books[:5]:  # Показываем только первые 5
            print(f"   ○ '{book['title']}' - {book['author']}")
        if len(unread_books) > 5:
            print(f"   ... и еще {len(unread_books) - 5} книг")

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Тестовые данные для статистики
    books.extend([
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': False},
        {'id': 3, 'title': 'Скотный двор', 'author': 'Джордж Оруэлл', 'year': '1945', 'genre': 'Сатира', 'read': True},
        {'id': 4, 'title': 'Преступление и наказание', 'author': 'Федор Достоевский', 'year': '1866', 'genre': 'Роман', 'read': False}
    ])
    
    # Демонстрация статистики
    show_statistics()
    show_reading_progress()

def add_rating():
    """Добавляет или изменяет рейтинг книги"""
    show_all_books()
    
    try:
        book_id = int(input("Введите ID книги для оценки: "))
        
        for book in books:
            if book['id'] == book_id:
                try:
                    rating = int(input("Введите рейтинг (1-5): "))
                    if 1 <= rating <= 5:
                        book['rating'] = rating
                        print(f"Рейтинг {rating}/5 добавлен для книги '{book['title']}'!")
                    else:
                        print("Ошибка: Рейтинг должен быть от 1 до 5!")
                except ValueError:
                    print("Ошибка: Пожалуйста, введите число!")
                return
        
        print(f"Ошибка: Книга с ID {book_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def add_review():
    """Добавляет или изменяет отзыв о книге"""
    show_all_books()
    
    try:
        book_id = int(input("Введите ID книги для отзыва: "))
        
        for book in books:
            if book['id'] == book_id:
                review = input("Введите ваш отзыв: ")
                if review.strip():
                    book['review'] = review
                    print(f"Отзыв добавлен для книги '{book['title']}'!")
                else:
                    print("Ошибка: Отзыв не может быть пустым!")
                return
        
        print(f"Ошибка: Книга с ID {book_id} не найдена!")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID!")

def show_rated_books():
    """Показывает книги с рейтингами"""
    rated_books = [book for book in books if 'rating' in book]
    
    if not rated_books:
        print("Нет книг с рейтингами!")
        return
    
    print("\nКниги с рейтингами:")
    print("-" * 50)
    
    for book in sorted(rated_books, key=lambda x: x['rating'], reverse=True):
        stars = "★" * book['rating'] + "☆" * (5 - book['rating'])
        print(f"{book['id']}. '{book['title']}' - {book['author']}")
        print(f"   Рейтинг: {stars} ({book['rating']}/5)")
        
        if 'review' in book:
            print(f"   Отзыв: {book['review']}")
        print()

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Тестовые данные с рейтингами
    books.extend([
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True, 'rating': 5, 'review': 'Шедевр мировой литературы'},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': True, 'rating': 4},
        {'id': 3, 'title': 'Скотный двор', 'author': 'Джордж Оруэлл', 'year': '1945', 'genre': 'Сатира', 'read': True, 'rating': 4},
        {'id': 4, 'title': 'Преступление и наказание', 'author': 'Федор Достоевский', 'year': '1866', 'genre': 'Роман', 'read': False}
    ])
    
    # Демонстрация рейтингов и отзывов
    add_rating()
    add_review()
    show_rated_books()    

def get_recommendations():
    """Предлагает рекомендации для чтения"""
    if not books:
        print("Библиотека пуста! Нет данных для рекомендаций.")
        return
    
    # Рекомендации на основе жанров прочитанных книг
    read_books = [book for book in books if book['read'] and book.get('rating', 0) >= 4]
    
    if not read_books:
        print("Рекомендуем начать с классики:")
        classic_books = [book for book in books if not book['read']]
        for book in classic_books[:3]:
            print(f"   ○ '{book['title']}' - {book['author']}")
        return
    
    # Находим любимые жанры
    favorite_genres = {}
    for book in read_books:
        genre = book.get('genre', '')
        if genre:
            favorite_genres[genre] = favorite_genres.get(genre, 0) + 1
    
    if favorite_genres:
        top_genre = max(favorite_genres, key=favorite_genres.get)
        print(f"\nОсновываясь на ваших предпочтениях (любимый жанр: {top_genre}):")
        
        # Рекомендуем книги того же жанра
        recommended_books = [book for book in books if not book['read'] and book.get('genre') == top_genre]
        
        if recommended_books:
            for book in recommended_books[:3]:
                print(f"   ○ '{book['title']}' - {book['author']}")
        else:
            print("   К сожалению, в библиотеке нет непрочитанных книг этого жанра.")
    
    # Рекомендации на основе авторов
    favorite_authors = {}
    for book in read_books:
        author = book['author']
        favorite_authors[author] = favorite_authors.get(author, 0) + 1
    
    if favorite_authors:
        top_author = max(favorite_authors, key=favorite_authors.get)
        print(f"\nПохожие книги автора {top_author}:")
        
        author_books = [book for book in books if not book['read'] and book['author'] == top_author]
        
        if author_books:
            for book in author_books[:2]:
                print(f"   ○ '{book['title']}' - {book['author']}")
        else:
            print("   Вы уже прочитали все книги этого автора в библиотеке.")

def show_random_book():
    """Показывает случайную книгу для чтения"""
    if not books:
        print("Библиотека пуста!")
        return
    
    import random
    unread_books = [book for book in books if not book['read']]
    
    if unread_books:
        random_book = random.choice(unread_books)
        print("\nСлучайная книга для чтения:")
        print("-" * 40)
        print(f"   '{random_book['title']}'")
        print(f"   Автор: {random_book['author']}")
        print(f"   Жанр: {random_book.get('genre', 'Не указан')}")
        print(f"   Год: {random_book.get('year', 'Не указан')}")
    else:
        print("Поздравляем! Вы прочитали все книги в библиотеке!")

def show_reading_challenge():
    """Показывает прогресс по чтению"""
    if not books:
        print("Библиотека пуста!")
        return
    
    total_books = len(books)
    read_books = len([book for book in books if book['read']])
    
    print("\nЧитательский вызов:")
    print("-" * 30)
    print(f"Прочитано книг: {read_books}/{total_books}")
    
    if read_books < total_books:
        progress = (read_books / total_books) * 100
        print(f"Прогресс: {progress:.1f}%")
        print(f"Осталось прочитать: {total_books - read_books} книг")
        
        # Предлагаем цель
        if progress < 50:
            print("Цель: прочитать половину библиотеки!")
        elif progress < 75:
            print("Цель: прочитать 75% библиотеки!")
        else:
            print("Цель: завершить чтение всей библиотеки!")
    else:
        print("Поздравляем! Вы завершили чтение всей библиотеки!")

def main():
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Тестовые данные
    books.extend([
        {'id': 1, 'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1966', 'genre': 'Роман', 'read': True, 'rating': 5},
        {'id': 2, 'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1949', 'genre': 'Антиутопия', 'read': True, 'rating': 4},
        {'id': 3, 'title': 'Скотный двор', 'author': 'Джордж Оруэлл', 'year': '1945', 'genre': 'Сатира', 'read': False},
        {'id': 4, 'title': 'Преступление и наказание', 'author': 'Федор Достоевский', 'year': '1866', 'genre': 'Роман', 'read': False},
        {'id': 5, 'title': 'Братья Карамазовы', 'author': 'Федор Достоевский', 'year': '1880', 'genre': 'Роман', 'read': False}
    ])
    
    # Демонстрация рекомендаций
    get_recommendations()
    show_random_book()
    show_reading_challenge()    

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
    print("Добро пожаловать в систему учета домашней библиотеки!")
    
    # Загружаем примеры данных
    initialize_sample_data()
    
    # Демонстрируем меню
    show_main_menu()
    choice = get_menu_choice()
    print(f"Вы выбрали: {choice}")    