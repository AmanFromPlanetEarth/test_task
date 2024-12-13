from app.urls import *


print("Добро пожаловать в приложение 'Библиотека'")
print("В этом приложении вы можете посмотреть список всех книг и выбрать понравившуюся")

if __name__=='__main__':

    while True:
        command: str = input("Введите:\n1 - если хотите зайти как администратор\n"
                        "2 - как пользователь\n3 - выход\n")
        if command == '1':
            print("Вы попали в пользовательское меню администратора")
            print("Здесь вы можете добавлять книги в библиотеку\n"
                  "удалять книги\n"
                  "искать книгу\n"
                  "отображать список всех книг\n"
                  "и изменять статус")
            print("Команды:\n"
                  "add - добавить книгу\n"
                  "del - удалить книгу\n"
                  "find - поиск книги\n"
                  "all - отоброзить все книги\n"
                  "ch - изменить статус\n"
                  "ex - выход\n")
            admin_command = input("Введите команду: ")
            if admin_command.lower() == 'add':
                title: str = input("Введите название: ")
                author: str = input("Введите автора: ")
                year: int = int(input("Введите год издания книги: "))
                input("Нажмите 'Enter' чтобы продолжить")
                cr_book = createBook(title, author, year)
                print(cr_book)
                break
            if admin_command.lower() == 'del':
                id_book: int = int(input("Чтобы удалить книгу введите ее ID: "))
                input("Нажмите 'Enter' чтобы продолжить")
                deleteBook(id_book)
                break
            if admin_command.lower() == 'find':
                print("Здесь вы можете искать книгу по названию,"
                      "автору или по году издания\n")
                print("1 - по автору\n2 - по названию\n3 - по году издания\n")
                srch_book = input("Введите команду: ")
                if srch_book == '1':
                    author = input("Введите имя автора: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(author)
                    break
                if srch_book == '2':
                    title = input("Введите название книги: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(title)
                    break
                if srch_book == '3':
                    year = int(input("Введите год издания: "))
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(year)
                    break
                else:
                    print("Ошибка! Такой команды нет.")
                    break
            if admin_command.lower() == 'all':
                getAllBook()
                break
            if admin_command.lower() == 'ch':
                id_book: int = int(input("Введите ID книги: "))
                status: str = input("Введите статус: ")
                input("Нажмите 'Enter' чтобы продолжить")
                changeStatusBook(id_book, status)
                break
            if admin_command.lower() == 'ex':
                print("Программа завершила свою работу")
                break
            else:
                print("Ошибка! Такой команды нет.")
                break
        elif command == '2':
            print("Вы попали в пользовательское меню")
            print("Здесь вы можете искать книги и выводить список всех книг")
            print("Команды:\n"
                  "find - поиск книги\n"
                  "all - отоброзить все книги\n"
                  "ex - выход\n")
            user_command = input("Введите команду: ")
            if user_command.lower() == 'find':
                print("Здесь вы можете искать книгу по названию,"
                      "автору или по году издания")
                print("1 - по автору, 2 - по названию, 3 - по году издания")
                srch_book = input("Введите команду: ")
                if srch_book == '1':
                    author = input("Введите имя автора: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(author)
                    break
                if srch_book == '2':
                    title = input("Введите название книги: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(title)
                    break
                if srch_book == '3':
                    year = int(input("Введите год издания: "))
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(year)
                    break
                else:
                    print("Ошибка! Такой команды нет.")
                    break
            if user_command.lower() == 'all':
                getAllBook()
                break
            if user_command.lower() == 'ex':
                print("Программа завершила свою работу")
                break
        elif command == '3':
            print("Приложение завершило свою работу.")
            break
        else:
            print("Ошибка! Такой команды нет.")
            break


