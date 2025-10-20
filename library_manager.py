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