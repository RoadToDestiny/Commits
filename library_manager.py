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