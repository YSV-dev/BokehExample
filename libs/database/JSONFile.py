import json


class JSONFile:
    @staticmethod
    def read_file(file_path: str) -> dict:
        result: dict = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                str_result: str = ""
                for line in f:
                    str_result += line
                result = json.loads(str_result)
        except FileExistsError as e:
            e.print_exc()
            print("Error while reading file", e)
        finally:
            return result

    @staticmethod
    def write_file(file_path: str, json_obj):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                print(json_obj)
                json.dump(json_obj, f, ensure_ascii=False)
        except Exception as e:
            print("Error while writing file", e)
