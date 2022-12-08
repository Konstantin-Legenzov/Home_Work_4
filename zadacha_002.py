# 2 - Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

a = list(input())
b = list(map(int, a))
b.sort(reverse=False)
print(b)

Third_list = []

for i in range(0, len(b)):
    if i in b:
        Third_list.append(i)

print(Third_list)

# from typing import List

# def original_list(lst: list) -> list:
#     new_list = []
#     for i in range(len(lst)):
#         if not[i] in lst:
#             new_list.append(lst[i])
#     return new_list















