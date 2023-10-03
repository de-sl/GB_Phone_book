from logger import *

def menu():  # Функция интерфейса главного меню
    print("------ Телефонный справочник ------ ")
    print("=" * 26)
    print(" [1] --> Показать контакты")
    print(" [2] --> Добавить новый контакт")
    print(" [3] --> Поиск контакта")
    print(" [4] --> Изменить контакт")
    print(" [5] --> Удалить контатк")
    print(" [9] --> Показать команды")
    print("\n [0] --> Выход")
    print("=" * 26)
    while True:
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


if __name__ == '__main__':
    menu()
