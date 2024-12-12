import json

class ConnectFile:
    """Класс для подключения к файлу json, для чтения и записи данных в файл"""
    @staticmethod
    def read_file(filename: str) -> dict:
        with open(filename, 'r', encoding="utf-8") as library_file:
            return json.load(library_file)
    @staticmethod
    def write_file(filename, data):
        with open(filename, 'w', encoding='utf-8') as library_file:
            return json.dump(data, library_file, ensure_ascii=False, indent=4)