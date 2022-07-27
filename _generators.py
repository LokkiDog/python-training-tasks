
def f1 ():
    """
    На входе программа получает список целых чисел s. Ваша задача - вывести следующие списки по одному в строке:

    Список, состоящий из квадратов s.
    Список, состоящий из остатков деления на 11 элементов s.
    Список, состоящий только из чётных элементов s.
    Список, состоящий только из элементов s с нечётным количеством цифр.
    Список, состоящий только из двухзначных элементов s, записанных 2 раза подряд.
    Список, состоящий из элементов s, стоящих на позициях, не кратных 3.

    Входные данные
    В единственной строке записаны числа, разделённые пробелами.

    Выходные данные
    В каждой из шести строк выведите соответствующий список в стандартном формате python'а."""


    s = '8 5 15 101 42 1'

    a = [int(x) ** 2 for x in s.split(' ')]
    b = [int(x) % 11 for x in s.split(' ')]
    c = [int(x) for x in s.split(' ') if int(x) % 2 == 0]
    d = [int(x) for x in s.split(' ') if len(x) % 2 != 0]
    e = [int(x+x) for x in s.split(' ') if len(x) == 2]
    f = [int(x) for i, x in enumerate(s.split(' ')) if i % 3 != 0]

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

def f2():
    """
    В этом массиве n = 5 строк, m = 6 столбцов
    Заполните массив целыми числами по образцу в виде таблицы умножени

    Результат:
    0  0  0  0  0  0
    0  1  2  3  4  5
    0  2  4  6  8 10
    0  3  6  9 12 15
    0  4  8 12 16 20
    """
    n, m = 5 ,6
    a = [[x * y for x in range(m)] for y in range(n)]
    print(a)

def f3():
    """Пусть дан текст:

    t = Генератор – это итератор, элементы которого
    можно перебирать (итерировать) только один раз.
    Итератор – это объект, который поддерживает функцию next()
    для перехода к следующему элементу коллекции

    Написать функцию-генератор для выделения слов из этого текста 
    (слова разделяются пробелом, либо переносом строки ‘\n’). 
    Список всех слов при этом в функции не создавать.
    """

    t = '''Генератор – это итератор, элементы которого можно перебирать (итерировать) только один раз.
    Итератор – это объект, который поддерживает функцию next()для перехода к следующему элементу коллекции'''

    def splitt(string):
        # word = ''
        # for letter in string:
        #     if letter not in [' ', '\n',]:
        #         word += letter
        #     else:
        #         yield word
        #         word = ''

        for word in string.split():
            yield word
    
    s = splitt(t)
    for i in range(11):
        print(f'{i}: {next(s)}')

def f4():
    ''' Написать генератор, который на вход принимает числои генирирует
        последовательность,которая возводит данное число в следующую степень.

        Входные данные:
        2
        Выходные данные
        2 4 8 16 ...
    '''

    def gen(number):
        pow = 1
        while True:
            yield number ** pow
            pow += 1
    
    g = gen(3)
    for i in range(10):
        print(next(g))
    
f4()