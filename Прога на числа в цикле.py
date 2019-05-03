print('Вам нужно ввести 10 разных чисел по отдельности.')
b = []
a = True
while a:
    q = int(input('Введите любое целое число: '))
    w = int(input('Введите любое целое число: '))
    e = int(input('Введите любое целое число: '))
    r = int(input('Введите любое целое число: '))
    t = int(input('Введите любое целое число: '))
    y = int(input('Введите любое целое число: '))
    u = int(input('Введите любое целое число: '))
    i = int(input('Введите любое целое число: '))
    o = int(input('Введите любое целое число: '))
    p = int(input('Введите любое целое число: '))
    a = False
    b.append(q)
    b.append(w)
    b.append(e)
    b.append(r)
    b.append(t)
    b.append(y)
    b.append(u)
    b.append(i)
    b.append(o)
    b.append(p)
    b.sort()
    for x in b:
        print(x*10)
    else:
        print('Конец программы.')






