def arguments(): #2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел
    a = 9
    b = 9

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'Оба числа одинаковые'

print(arguments())



def difference(): #Функция на вход получает два произвольных числа. Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”
    a = 2346
    b = 2211

    if (a - b) == 135:
        return('yes')

    else:
        return('no')

print(difference())





