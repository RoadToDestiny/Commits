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