# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y)

number=int(input('Введите номер четверти(от 1 до 4): '))
if (number<1 or number>4):
    print('Вводите корректные значения!')
elif (number ==1):
    print('x(0, +max),y(0,+max)')
elif (number ==2):
    print('x(-max, 0),y(0,+max)')
elif (number ==3):
    print('x(-max, 0),y(-max, 0)')
elif (number ==4):
    print('x(0, +max),y(-max, 0)')