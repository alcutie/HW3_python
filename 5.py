# создаем список с вводимыми числами
number_list = list(map(int, input().split()))

# создаем переменную для подсчета пар одинаковых элементов
pairs = 0

# цикл для прохождения по всем элементам из списка number_list для первого числа пары
for i in range(len(number_list)):
    # создаем еще один цикл для прохождения по всем элементам списка после текущего i для второго числа пары
    for j in range(i + 1, len(number_list)):
        # если элементы пары равны (первый элемент равен второму)
        if number_list[i] == number_list[j]:
            # то прибавляем 1 для подсчета всех пар одинаковых элементов
            pairs += 1

# выводим результат подсчета
print(pairs)
