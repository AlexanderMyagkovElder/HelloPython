# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение 
# второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, 
# если из последовательности удалить наибольший элемент.
# Пример: 1 7 9 0 Вывод: 7
range_numbers=[1,7,9,0]
maximum=range_numbers[0]
maximum_index=0
for i in range(len(range_numbers)-1):
    if range_numbers[i]>maximum:
        maximum=range_numbers[i]
        maximum_index=i
del range_numbers[maximum_index]
print(max(range_numbers))
