# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
number=input("Введите вещественное число: ")
sum=0
if '.' in number:
    number=number.split('.')
    before_comma=int(number[0])
    after_comma =int(number[1])
    while before_comma>0:
        num=before_comma%10
        sum+=num
        before_comma=before_comma//10
    while after_comma>0:
        num=after_comma%10
        sum+=num
        after_comma=after_comma//10
else:
    int_number=int(number)
    while int_number>0:
        num=int_number%10
        sum+=num
        int_number=int_number//10
print(sum)