def pribavka (zarplata, kniga):
    k = 0
    if (kniga > 20):
        k = round((kniga - 20) * 0.02 * zarplata)
    return k

a = int(input('Введите вашу зарплату: '))
b = int(input('Введите сколько вы продали книг: '))

def pribavka_budet ():
    if (b > 10):
        с = pribavka(a, b)
        print('В этом месяце прибавка к зарплате составит: ' + str(с))
    else:
        print('В этом месяце у вас не будет прибавки. Вы продали слишком мало книг.')

print(pribavka_budet())