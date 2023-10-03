import os, re

def help():
    os.system("cls")
    print("------ Телефонный справочник ------ ")
    print("=" * 26)
    print(" [1] --> Показать контакты")
    print(" [2] --> Добавить новый контакт")
    print(" [3] --> Поиск контакта")
    print(" [4] --> Изменить контакт")
    print(" [5] --> Удалить контатк")
    print(" [9] --> Показать команды")
    print("\n [0] --> Выход")
    input("--- нажмите любую кнопку ---") 
    os.system("cls")
    command = int(input("Введите нормер команды: "))

    if command == 1:
            show_contacts()
    elif command == 2:
            add_contact()
    elif command == 3:
            find_contact()
    elif command == 4:
            change_contact()
    elif command == 5:
            delete_contact()
    elif command == 9:
            help()
    elif command == 0:
        print("Спасибо, до свидания!")
        return


 
def phone_format(n):  # форматирование телефонного номера
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def print_data(data):  # Функция вывода телефонной книги в консоль
    with open('data.txt', 'r', encoding='utf-8') as f:
        phone_book = []
        split_line = "=" * 49
        print(split_line)
        print(" №  Фамилия        Имя          Номер телефона")
        print(split_line)
        person_id = 1

        for contact in data:
            last_name, name, phone = contact.rstrip().split(",")
            phone_book.append(
                {
                    "ID": person_id,
                    "Фамилия": last_name,
                    "Имя": name,
                    "Телефон": phone_format(phone),
                }
            )
            person_id += 1

        for contact in phone_book:
            person_id, last_name, name, phone = contact.values()
            print(f"{person_id:>2}. {last_name:<15} {name:<10} -- {phone:<15}")

        print(split_line)


def show_contacts():  # Функция открытия телефонной книги
        os.system("cls")
        phone_book = []
        with open('data.txt', "r", encoding="UTF-8") as f:
            data = sorted(f.readlines())
            print_data(data)
        input("\n--- нажмите любую кнопку ---")


def add_contact():  # Функция добавления нового контакта в телефонную книгу
    os.system("cls")
    with open('data.txt', "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите Фамилию контакта: ") + ","
        res += input("Введите Имя контакта: ") + ","
        res += input("Введите Телефонный номер контакта: ")

        file.write(res + "\n")

    input("\nКонтакт был успешно добавлен!\n--- нажмите любую кнопку ---")


def find_contact():  # Функция поиска контактов в телефонной книге
    os.system("cls")
    target = input("Введите Фамилию или имя или телефон для поиска: ")
    result = []
    with open("data.txt", "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        print_data(result)
    else:
        print(f"С такими данными контакта не обранужено '{target}'.")

    input("--- нажмите любую кнопку ---")


def change_contact():  # Функция изменения информации в контакте
    os.system("cls")
    phone_book = []
    with open("data.txt", "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        print_data(data)

        number_contact = int(
            input("Введите номер контакта для изменения или 0 для возврата в меню:\n ")
        )
        print(data[number_contact - 1].rstrip().split(","))
        if number_contact != 0:
            new_las_name = input("Введите новую Фамилию: ")
            new_name = input("Введите новое Имя: ")
            new_phone = input("Введите новый Номер: ")
            data[number_contact - 1] = (
                new_las_name + "," + new_name + "," + new_phone + "\n"
            )
            with open("data.txt", "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n--- нажмите любую кнопку ---")
        else:
            return


def delete_contact():  # Функция удаления контакта из телефонной книги
    os.system("cls")
    with open("data.txt", "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        print_data(data)

        number_contact = int(
            input("Input Number of Contact for deleting or 0 for return Main Menu: ")
        )
        if number_contact != 0:
            print(f"Deleting record: {data[number_contact-1].rstrip().split(',')}\n")
            data.pop(number_contact - 1)
            with open("data.txt", "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- нажмите любую кнопку ---")