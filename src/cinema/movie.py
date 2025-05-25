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

