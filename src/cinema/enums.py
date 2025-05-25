from enum import Enum


class Country(Enum):
    USA = "США"
    UK = "Великобритания"
    JAPAN = "Япония"
    FRANCE = "Франция"
    GERMANY = "Германия"
    SOUTH_KOREA = "Южная Корея"
    RUSSIA = "Россия"
    CHINA = "Китай"
    ITALY = "Италия"
    INDIA = "Индия"
    OTHER = "Другая"
    UNKNOWN = "Неизвестно"


class Genre(Enum):
    DRAMA = "Драма"
    COMEDY = "Комедия"
    ACTION = "Боевик"
    THRILLER = "Триллер"
    HORROR = "Ужасы"
    ROMANCE = "Мелодрама"
    FANTASY = "Фэнтези"
    SCI_FI = "Научная фантастика"
    DOCUMENTARY = "Документальный"
    ANIMATION = "Мультфильм"
    OTHER = "Другой"
    UNKNOWN = "Неизвестно"
