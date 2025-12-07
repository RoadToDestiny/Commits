# media_collection.py
# Система управления коллекцией фильмов и сериалов
# Коммит 2: Структура данных и добавление фильмов

# Глобальные переменные для хранения данных
movies = []
genres = ['Драма', 'Комедия', 'Боевик', 'Фантастика', 'Ужасы', 'Мультфильм', 'Документальный', 'Другое']

def add_movie():
    """Добавляет новый фильм в коллекцию"""
    title = input("Введите название фильма: ")
    director = input("Введите режиссера: ")
    
    if title.strip():
        movie = {
            'id': len(movies) + 1,
            'title': title,
            'director': director,
            'year': '',
            'genre': '',
            'duration': 0,
            'rating': 0.0,
            'watched': False,
            'added_date': '2024-01-01'
        }
        movies.append(movie)
        print(f"Фильм '{title}' добавлен в коллекцию!")
    else:
        print("Ошибка: Название фильма не может быть пустым!")

def main():
    print("Добро пожаловать в менеджер коллекции фильмов!")
    
    # Тестируем добавление фильмов
    add_movie()
    print(f"Всего фильмов: {len(movies)}")

if __name__ == "__main__":
    main()