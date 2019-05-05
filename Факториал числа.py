#Эта программа даёт возможность пользователю найти факториал заданного им числа. 
#Также тут используется документация внутри функции factorial(x), которую можно вывести с помощью команды __doc__.
#

def factorial(x):
    '''В данной программе мы ищем факториал заданного числа x.
    f(x)=x!
    Для этого нужно задать число переменной х.
    Как посчитать факториал. Пример:
                                     1!=1
                                     2!=2*1=2
                                     3!=3*2*1=6
                                     4!=4*3*2*1=24
                                     5!=5*4*3*2*1=120
                                     6!=6*5*4*3*2*1=720.'''
    a = 1

    if ((x == 0) or (x == 1)):
        return a
    while x > 1:  
        a *= x     
        x -= 1     
    return a       
                  
                   

print(factorial.__doc__)
x = int(input('Введите значение х: '))
print(factorial(x))
