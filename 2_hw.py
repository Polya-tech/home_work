def task_1():
    yo = 38
    print(yo, "относится к типу", type(yo))

    bam = 12.85
    print(bam, 'относится к типу', type(bam))

    zap = "Hello Python"
    print(zap, 'относится к типу', type(zap))

    pow = ["apple", 123, True]
    print(pow, 'относится к типу', type(pow))

    bool_bob = True
    print(bool_bob, 'относится к типу', type(bool_bob))


task_1()


#
def task_2():
    a = [1, 2, 3, 5, 8, 13, 21] #последовательность Фибоначчи
    print("a[:3] = ", a[:3])

task_2()



def task_3(number: int) -> int:
    return number ** 2




print(task_3(3))


