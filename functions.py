def get_list_data(filename: str) -> str:
    # Возвращает список из строк файла
    # Args: 
    # filename - имя файла
    # Returns:
    # List[str]
    with open(filename, encoding='utf8') as file:
        return file.read().split('\n')