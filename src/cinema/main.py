from collection import *
from movie import *
from enums import *


menu_items_col1 = [
                "1. Добавить фильм",
                "2. Удалить фильм",
                "3. Показать все фильмы",
                "4. Найти фильм по критериям",
                "5. Добавить коллекцию",
]

menu_items_col2 = [
                "6. Удалить коллекцию",
                "7. Показать список коллекций",
                "8. Показать конкретную коллекцию",
                "9. Добавить фильм в коллекцию",
                "10. Удалить фильм из коллекции",
]


def main_menu():
    """Выводит меню и запрашивает номер пункта меню"""
    while True:
        print("### Меню ###")
        max_len = max(len(menu_items_col1), len(menu_items_col2))
        for i in range(max_len):
            left = menu_items_col1[i] if i < len(menu_items_col1) else ""
            right = menu_items_col2[i] if i < len(menu_items_col2) else ""
            print(f"{left:<35}{right}")
        print("11. Выйти")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            delete_movie()
        elif choice == '3':
            show_list_all_movies()
        elif choice == '4':
            search_movies()
        elif choice == '5':
            create_collection()
        elif choice == '6':
            delete_collection()
        elif choice == '7':
            show_list_all_collections()
        elif choice == '8':
            show_collection()
        elif choice == '9':
            add_movie_into_collection()
        elif choice == '10':
            remove_movie_from_collection()
        elif choice == '11':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


main_menu()
