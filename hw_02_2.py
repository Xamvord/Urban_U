str = input('Введи рандомное число: ')
num = float(str)

if num == 0:
    print('Да это же ноль!')
if num % 1 == 0:
    print('Начнём с того, что это целое.')
if num % 1 != 0:
    print('Начнём с того, что это число с точечкой.')
if num != 'число':
    print('Кстати, не могу не упомянуть, что', num, '- это вовсе не строка "число", а число.')
if num > 0:
    print('А число-то - положительное!')
if num < 0:
    print('А число-то - отрицательное!')
if num <= -10000:
    print('Довольно маленькое число!')
if num % 5 == 0:
    print('Ничоси, число делится на 5!')
if num == 10:
    print('В десяточку!')
if 0 < num < 0.5 :
    print('Чего так мало-то?!')
if 0.5 < num < 41 :
    print('Маловато ты ввёл...')
if 41 <= num < 59 :
    print('Чё-т около полтоса.')
if num != 0.5:
    print('И это точно не ноль-пять.')
if num == 0.5:
    print('О! Это хорошее число...')
if num >= 10000:
    print('Довольно большое число!')

