from dataclasses import dataclass
import json

FILENAME = 'database_book.json'

#Класс для подключения к файлу json, чтения и записи данных в файл
@dataclass #для автоматического определения метода __init__ чтобы определение класса было более компактным
class ConnectFile:
    filename: str

    @classmethod #для доступа к методу из самого класса
    def read_file(cls, filename: str) -> dict:
        with open(filename, 'r', encoding="utf-8") as library_file:
            return json.load(library_file)
    @classmethod #для доступа к методу из самого класса
    def write_file(cls, filename, data) -> json:
        with open(filename, 'w', encoding='utf-8') as library_file:
            return json.dump(data, library_file, ensure_ascii=False, indent=4)



def create_book(title: str, author: str, year: int):
    print("Добавить книгу в библиотеку.")
    data = {
        'books': {
            'title': title,
            'author': author,
            'year': year,
        }
    }
    ConnectFile.write_file(FILENAME, data=data)
    

create_book("Война и мир", "Л.Н.Толстой", 18)

#print("~~~~~~ Добро пожаловать в библиотеку ~~~~~~")
