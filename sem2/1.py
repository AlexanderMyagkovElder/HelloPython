# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
number=input("Введите вещественное число: ")
sum=0
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
print(sum)