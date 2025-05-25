def choose_from_list(options: list[any], prompt: str) -> str:
    """Выводит список опций и описание выбора, принимает номер опции """
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
