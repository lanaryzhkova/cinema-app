from enums import Country, Genre


class Movie:
    def __init__(self, title: str, year: int, country: Country, genre: Genre) -> None:
        self.title = title
        self.year = year
        self.country = country
        self.genre = genre
        print(f'Фильм {self.title} добавлен!')

    def __str__(self) -> str:
        return f"{self.title} ({self.year}, {self.country.value}, {self.genre.value})"


# Словарь фильмов
movies: dict[str, Movie] = {}


def add_movie() -> Movie:
    print('### Добавление фильма ###')

    title = input('Введите название: ')
    year = input_year()
    country = choose_from_list(list(Country), "Выберите страну:")
    genre = choose_from_list(list(Genre), "Выберите жанр:")

    movie = Movie(title, year, country, genre)
    movies[movie.title] = movie

    return movie


def delete_movie() -> None:
    print('### Удаление фильма ###')

    if not movies:
        print("Список фильмов пуст.")
        return

    movies_list = list(movies.values())
    selected_movie = choose_from_list(movies_list, "Выберите фильм для удаления:")
    del movies[selected_movie.title]
    print(f'Фильм "{selected_movie.title}" удалён.')


def input_year() -> int:
    while True:
        try:
            return int(input('Введите год производства: '))
        except ValueError:
            print('Ошибка: нужно ввести число. Попробуйте снова.')


def choose_from_list(options: list[any], prompt: str) -> str:
    print(prompt)
    for i, option in enumerate(options, start=1):
        name = option.value if hasattr(option, 'value') else str(option)
        print(f"{i}. {name}")
    while True:
        choice = input("Введите номер: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(options):
                return options[index]
        print("Неверный ввод, попробуйте ещё раз.")


def show_list_all_movies() -> None:
    if not movies:
        print("Список фильмов пуст.")
        return
    else:
        print('Список фильмов:')
        for i, movie in enumerate(movies.values(), start=1):
            print(f'{i}. {movie}')


def search_movies():
    if not movies:
        print("Список фильмов пуст.")
        return

    print('### Поиск фильма по критериям ###')
    parameters = ["Название", "Год производства", "Страна", "Жанр"]
    result = []
    choice = choose_from_list(parameters, "Выберите параметр для поиска:")

    if choice == 'Название':
        query = input("Введите название: ").lower()
        result = [m for m in movies.values() if query in m.title.lower()]
    elif choice == 'Год производства':
        query = int(input("Введите год: "))
        result = [m for m in movies.values() if query == m.year]
    elif choice == 'Страна':
        query = input("Введите страну: ")
        result = [m for m in movies.values() if query in m.country.lower()]
    elif choice == 'Жанр':
        query = input("Введите жанр: ")
        result = [m for m in movies.values() if query in m.genre.lower()]
    if result:
        print("Найденные фильмы:")
        for movie in result:
            print(movie)
    else:
        print("Фильмы по заданному критерию не найдены.")

