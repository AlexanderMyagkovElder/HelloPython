# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
numbers=[2,3,4,5,6]
multy=[]
if (len(numbers)%2==0):
    for i in range(len(numbers)//2):
        multy.append(numbers[i]*numbers[len(numbers)-i-1])
else:
    for i in range(len(numbers)//2+1):
        multy.append(numbers[i]*numbers[len(numbers)-i-1])
print(multy)