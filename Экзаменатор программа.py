ball = 0
koll = 0
doc = open(u'D:/dist/q.txt', 'r')
while True:
    vopros = doc.readline().strip()
    if (not vopros):
        break
    otvet1 = doc.readline().strip()
    otvet2 = doc.readline().strip()
    otvet3 = doc.readline().strip()
    kod_otveta = doc.readline().strip()
    print(vopros)
    print('1.' + otvet1)
    print('2.' + otvet2)
    print('3.' + otvet3)
    a = input('Введите номер правильного ответа и нажмите Enter: ')
    koll = koll + 1
    if (a == kod_otveta):
        ball = ball + 1

print('Вы ответили правильно на ' + str(ball) + ' из ' + str(koll) + ' вопросов.')
