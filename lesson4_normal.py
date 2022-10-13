# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
    lst = [1, 1]
    i = 2
    while i <= m:
        lst.append(lst[i - 1] + lst[i - 2])
        i += 1
    return lst[n:]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    j = 0
    while j < len(origin_list) - 1:
        i = 0
        while i + j < len(origin_list) - 1:
            if origin_list[i] > origin_list[i + 1]:
                # swap
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
            i += 1
        j += 1
    return origin_list
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def is_paral(a1, a2, a3, a4):
    # Определим функцию для проверки косинуса угла
    def cos_angle(b1, b2, b3):
        a = (b1[0] - b2[0]) * (b1[0] - b3[0]) + (b1[1] - b2[1]) * (b1[1] - b3[1])
        b = math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2)
        c = math.sqrt((b1[0] - b3[0]) ** 2 + (b1[1] - b3[1]) ** 2)
        return a / (b * c)

    cos_a1 = cos_angle(a1, a2, a4)
    cos_a2 = cos_angle(a2, a3, a1)
    cos_a3 = cos_angle(a3, a4, a2)
    cos_a4 = cos_angle(a4, a3, a1)

    # проверяем равенство углов и сумму соседних углов,
    # т.е. проверяем свойства параллелограма
    if cos_a1 == cos_a3 and cos_a2 == cos_a4 and (cos_a1 + cos_a2) == 0.0 and (cos_a3 + cos_a4) == 0.0:
        return True
    else:
        return False