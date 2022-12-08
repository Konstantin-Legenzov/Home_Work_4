# 3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

# f = open('Lastnames.txt','r', encoding="utf8")
# print(*f)

from functions import get_list_data
from typing import List

def string_to_up(our_text: list, find_symbol: str) -> str:
    for i in range(len(our_text)):
        if find_symbol in our_text[i]:
            our_text[i] = our_text[i].upper()
    return our_text

our_file = get_list_data('Lastnames.txt')
print(string_to_up(our_file,'5'))

with open('Lastnames.txt', 'w', encoding='utf=8') as data:
    for i in range(len(our_file)):
        data.writelines(f'{our_file[i]}\n')




# # имя файла
# FILENAME = "Latnames.txt"
# # определяем пустой список
# messages = list()
 
# for i in range(4):
#     message = input("Введите строку " + str(i+1) + ": ")
#     messages.append(message + "\n")
 
# # запись списка в файл
# with open(FILENAME, "a") as file:
#     for message in messages:
#         file.write(message)
 
# # считываем сообщения из файла
# print("Считанные сообщения")
# with open(FILENAME, "r") as file:
#     for message in file:
#         print(message, end="")