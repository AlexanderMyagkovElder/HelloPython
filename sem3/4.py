# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

stroka=''
number=int(input('Введите число: '))
while number!=0:
    stroka=str(number%2)+stroka
    number=number//2
print(stroka)
