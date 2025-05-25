from movie import Movie


class Collection:
    def __init__(self, title: str) -> None:
        self.title = title
        self.movies: Dict[str, Movie] = {}
        print(f'Коллекция {self.title} создана!')

    def add_movie(self, movie: Movie) -> None:
        if movie.title in self.movies:
            print(f'Фильм "{movie.title}" уже есть в коллекции.')
        else:
            self.movies[movie.title] = movie
            print(f'Фильм "{movie.title}" добавлен в коллекцию "{self.title}".')

    def remove_movie(self, title: str) -> None:
        if title in self.movies:
            del self.movies[title]
            print(f'Фильм "{title}" удалён из коллекции "{self.title}".')
        else:
            print(f'Фильм "{title}" не найден в коллекции "{self.title}".')

    def list_movies(self) -> None:
        if not self.movies:
            print(f'Коллекция "{self.title}" пуста.')
        else:
            print(f'Фильмы в коллекции "{self.title}":')
            for movie in self.movies.values():
                print(f"- {movie}")
