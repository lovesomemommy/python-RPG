def limit(value):
    if value > 100:
        return 100
    if value < 0:
        return 0
    return value


def feed(pet):
    pet["сытость"] = limit(pet["сытость"] + 30)
    return f"{pet['имя']} съел кусок мяса. Ням!"


def play(pet):
    if pet["энергия"] < 20:
        return f"{pet['имя']} слишком устал, чтобы играть. Сначала уложи его спать."
    pet["настроение"] = limit(pet["настроение"] + 25)
    pet["энергия"] = limit(pet["энергия"] - 20)
    return f"{pet['имя']} гоняется за мячиком и радостно рычит!"


def sleep(pet):
    pet["энергия"] = limit(pet["энергия"] + 40)
    return f"{pet['имя']} свернулся клубком и поспал."


def time_passes(pet):
    pet["сытость"] = limit(pet["сытость"] - 10)
    pet["настроение"] = limit(pet["настроение"] - 5)


def get_state(pet):
    if pet["сытость"] < 30:
        return "голодный"
    if pet["энергия"] < 30:
        return "сонный"
    if pet["настроение"] < 30:
        return "грустный"
    return "довольный"


def print_status(pet):
    print(f"{pet['имя']} сейчас {get_state(pet)}")
    print(f"  сытость: {pet['сытость']}")
    print(f"  настроение: {pet['настроение']}")
    print(f"  энергия: {pet['энергия']}")


def main():
    name = input("Как назовёшь львёнка? ")
    if name == "":
        name = "Лео"

    pet = {"имя": name, "сытость": 50, "настроение": 50, "энергия": 50}
    print(f"Знакомься, это {name}!")

    while True:
        print()
        print("1 - покормить")
        print("2 - поиграть")
        print("3 - уложить спать")
        print("4 - посмотреть состояние")
        print("0 - выйти")
        command = input("Выбор: ")

        if command == "1":
            print(feed(pet))
        elif command == "2":
            print(play(pet))
        elif command == "3":
            print(sleep(pet))
        elif command == "4":
            print_status(pet)
            continue
        elif command == "0":
            print(f"Пока! {name} будет ждать тебя.")
            break
        else:
            print("Такой команды нет.")
            continue

        time_passes(pet)
        if pet["сытость"] == 0:
            print(f"{name} проголодался и убежал искать еду сам. Игра окончена.")
            break


if __name__ == "__main__":
    main()
