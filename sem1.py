# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
# *Примеры:*- 5, 25 -> да  - 4, 16 -> да   - 25, 5 -> да   - 8,9 -> нет
first_number=int(input('Введите первое число: '))
second_number=int(input('Введите второе число: '))
if (first_number**2==second_number or second_number**2==first_number):
    print('да')
else:
    print('нет')