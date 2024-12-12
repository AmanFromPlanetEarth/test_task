from connect_class import ConnectFile
from database.database import FILENAME



def createBook(title: str, author: str, year: int) -> None:
    """Добавление книги: Пользователь вводит title, author и year,
      после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”."""
    
    data = ConnectFile.read_file(FILENAME)
    
    if data['books']:
        """Этот метот не совсем корректен для генерации ID, тк оставляет дыры после удаления книги
        метот uuid.uuid4() подходит лучше но ID получается слишком длинным"""
        new_id = max(book['id_book'] for book in data['books']) + 1
    else:
        new_id = 1
    
    book_data = {
        'title': title,
        'author': author,
        'year': year,
        'status': 'В наличии',
        'id_book': new_id
    }
    
    for elem in data['books']:
        """Проверяем наличие книги в библиотеке,
        если книга имеется в библиотеке, то мы ее не заносим в библиотеку"""
        if title == elem['title']:
            return f"Книга с названием {title} уже есть в библиотеке"

    data['books'].append(book_data)
    ConnectFile.write_file(FILENAME, data=data)
    
    return f"Книга {title} добавлена в библиотеку"
    


def deleteBook(id: int) -> None:
    """ Удаление книги: Пользователь вводит idкниги, которую нужно удалить."""
    
    data = ConnectFile.read_file(FILENAME)

    book_found = False

    for i, elem in enumerate(data['books']):
        if id == elem['id_book']:
            del data['books'][i]
            book_found = True
            print(f"Книга с ID {id} успешно удалена.")
    
    ConnectFile.write_file(FILENAME, data=data)

    if not book_found:
        print(f"Книга с таким ID не найдена")

    

def findBook(searchBook: str | int) -> None:
    """Поиск книги: Пользователь может искать книги по title, author или year"""
    data = ConnectFile.read_file(FILENAME)

    for elem in data['books']:
        if searchBook == elem['title'] or searchBook == elem['author'] or searchBook == elem['year']:
            print(
                "Название: ", elem['title'], 
                "Автор: ", elem['author'],
                "Год издания: ", elem['year'],
                "Статус: ", elem['status'],
                "ID: ", elem['id_book']
                )



def getAllBook() -> None:
    """Отображение всех книг: 
    Приложение выводит список всех книг с их id, title, author, year и status"""
    data = ConnectFile.read_file(FILENAME)
    for i in data['books']:
        print("\n")
        for k, books in i.items():
            print(f"{k}: ", books)



def changeStatusBook(id: int, status: str) -> None:
    """Изменение статуса книги:
    Пользователь вводит id книги и новый статус (“в наличии” или “выдана”)"""

    data = ConnectFile.read_file(FILENAME)

    for book in data['books']:
        if id == book['id_book']:
            book['status'] = status
            break
        
    ConnectFile.write_file(FILENAME, data=data)

