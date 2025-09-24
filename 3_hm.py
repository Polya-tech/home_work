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


def month_of_year(month): #сделала разными способами вывод месяца по номеру.  Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)
    if month in [12, 1, 2]:
        return('winter')
    elif month in range(3, 6):
        return('spring')
    elif 6 <= month <= 8:
        return('summer')
    elif 9 <= month <= 11:
        return('autumn')

print(month_of_year(9))



def map(a, b, c): #5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
    if (a + b + c) > 10:
        return('YES')
    else:
        return('NO')

print(map(12, 0, 1))



def positive(number):
    count = 0
    for num in number:
        if num > 0:
            count += 1
    return count

list = [98, -5, -4, -3, -3]
result = positive(list)
print(result)


#Функция на вход получает 2 переменные.Кол-во лет (int). Кол-во месяцев (int). Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

def calculate_days(year, month=29):

      return (year*12) * month

print(calculate_days(100))













