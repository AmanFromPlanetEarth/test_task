from app.urls import *


print("Добро пожаловать в приложение 'Библиотека'")
print("В этом приложении вы можете посмотреть список всех книг и выбрать понравившуюся")

if __name__=='__main__':

    while True:
        command: str = input("Введите:\n1 - если хотите зайти как администратор\n"
                        "2 - как пользователь\n3 - выход\n")
        if command == '1':
            print("Вы попали в пользовательское меню администратора")
            print("Здесь вы можете добавлять книги в библиотеку,"
                  "удалять книги,"
                  "искать книгу,"
                  "отображать список всех книг,"
                  "и изменять статус")
            print("Команды:"
                  "add - добавить книгу"
                  "del - удалить книгу,"
                  "find - поиск книги,"
                  "all - отоброзить все книги,"
                  "ch - изменить статус"
                  "ex - выход")
            admin_command = input("Введите команду: ")
            if admin_command.lower() == 'add':
                title: str = input("Введите название: ")
                author: str = input("Введите автора: ")
                year: int = int(input("Введите год издания книги: "))
                input("Нажмите 'Enter' чтобы продолжить")
                cr_book = createBook(title, author, year)
                print(cr_book)
            if admin_command.lower() == 'del':
                id_book: int = int(input("Чтобы удалить книгу введите ее ID: "))
                input("Нажмите 'Enter' чтобы продолжить")
                deleteBook(id_book)
            if admin_command.lower() == 'find':
                print("Здесь вы можете искать книгу по названию,"
                      "автору или по году издания")
                print("1 - по автору, 2 - по названию, 3 - по году издания")
                srch_book = input("Введите команду: ")
                if srch_book == '1':
                    author = input("Введите имя автора: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(author)
                if srch_book == '2':
                    title = input("Введите название книги: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(title)
                if srch_book == '3':
                    year = int(input("Введите год издания: "))
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(year)
            if admin_command.lower() == 'all':
                getAllBook()
            if admin_command.lower() == 'ch':
                id_book: int = int(input("Введите ID книги"))
                status: str = input("Введите статус")
                input("Нажмите 'Enter' чтобы продолжить")
                changeStatusBook(id_book, status)
            if admin_command.lower() == 'ex':
                print("Программа завершила свою работу")
                break
        if command == '2':
            print("Вы попали в пользовательское меню")
            print("Здесь вы можете искать книги и выводить список всех книг")
            print("Команды:"
                  "find - поиск книги,"
                  "all - отоброзить все книги,"
                  "ex - выход")
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
                if srch_book == '2':
                    title = input("Введите название книги: ")
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(title)
                if srch_book == '3':
                    year = int(input("Введите год издания: "))
                    input("Нажмите 'Enter' чтобы продолжить")
                    findBook(year)
            if user_command.lower() == 'all':
                getAllBook()
            if user_command.lower() == 'ex':
                print("Программа завершила свою работу")
                break

        if command == '3':
            print("Приложение завершило свою работу.")
            break


