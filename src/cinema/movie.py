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


def add_movie():
    print('### Добавление фильма ###')

    title = input('Введите название: ')
    year = input_year()
    country = choose_from_list(list(Country), "Выберите страну:")
    genre = choose_from_list(list(Genre), "Выберите жанр:")

    movie = Movie(title, year, country, genre)
    movies[movie.title] = movie


def delete_movie():
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


def choose_from_list(options: list[any], prompt: str) -> any:
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


