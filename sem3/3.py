# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_1=[1.1, 1.2, 3.1, 5.0, 10.01]
list_2=[]
for i in range(len(list_1)):
    list_2.append((list_1[i]-int(list_1[i])))
difference=max(list_2)-min(list_2)
print(difference)