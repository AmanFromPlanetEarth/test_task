import json

class ConnectFile:
    """Класс для подключения к файлу json, для чтения и записи данных в файл"""
    @staticmethod
    def read_file(filename: str) -> dict:
        try:
            with open(filename, 'r', encoding="utf-8") as library_file:
                return json.load(library_file)
        except FileNotFoundError:
            """Если файл не найден, возвращаем пустую структуру данных"""
            return {'books': []}
        except json.JSONDecodeError:
            """Если файл поврежден, возвращаем пустую структуру данных"""
            print("Ошибка! Файл может быть поврежден")
            return {'books': []}
        except Exception as e:
            print(f"Произошла ошибка при чтении файла {e}")
            return {'books': []}

    @staticmethod
    def write_file(filename, data):
        try:
            with open(filename, 'w', encoding='utf-8') as library_file:
                return json.dump(data, library_file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Произошла ошибка при записи в файл {e}")