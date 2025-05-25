from typing import Iterator
from movie import Movie
from movie import choose_from_list


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

    def __iter__(self) -> Iterator[Movie]:
        return MovieIterator(list(self.movies.values()))


class MovieIterator:
    def __init__(self, movies_list: list[Movie]):
        self._movies = movies_list
        self._index = 0

    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        else:
            raise StopIteration

    def __iter__(self):
        return self


collections: dict[str, Collection] = {}


def create_collection() -> Collection:
    print('### Создание коллекции ###')

    title = input('Введите название: ')

    collection = Collection(title)
    collections[collection.title] = collection
    return collection


def delete_collection() -> None:
    print('### Удаление коллекции ###')

    if not collections:
        print("Список коллекций пуст.")
        return

    collections_list = list(collections.values())
    selected_collection = choose_from_list(collections_list, "Выберите коллекцию для удаления:")
    del collections[selected_collection.title]
    print(f'Коллекция "{selected_collection.title}" удалена.')


