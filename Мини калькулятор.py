#Это реализация псевдокалькулятора. Построен на операторе if, elif, else.
#Также тут используется модуль colorama для изменения цвета выводимого текста. 



from colorama import init
from colorama import Fore, Back, Style

print(Fore.GREEN)
print(Back.CYAN)

sho = input('Какую операцию произвести нужно? (+, -, *, /): ')

print(Back.GREEN)

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

print(Back.BLUE)

if (sho == '+'):
    c = a + b
    print('Результат: ' + str(c))
elif (sho == '-'):
    c = a - b
    print('Результат: ' + str(c))
elif (sho == '*'):
    c = a * b
    print('Результат: ' + str(c))
elif (sho == '/'):
    c = a / b
    print('Результат: ' + str(c))
else:
    print('Введена не правильная операция, вывести результат невозможно!')

input()
