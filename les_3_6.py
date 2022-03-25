import random
SIZE = 10
MIN_NUM = 0
MAX_NUM = 100
array = [random.randint(MIN_NUM, MAX_NUM) for i in range(SIZE)]
print(array)
min_num = array[0]
max_num = array[0]
for el in range(len(array)):
    if min_num >= array[el]:
        min_num = array[el]
    elif max_num <= array[el]:
        max_num = array[el]

print(f'Минимальное число {min_num}')
print(f'Максимальное число {max_num}')
a = array.index(min_num)
b = array.index(max_num)
# print(a)
# print(b)
if a < b:
    aa = array[a + 1: b]
    summ = 0
    for i in aa:
        summ += i
    print(f'Сумма между мин и макс числами {summ}')
else:
    bb = array[b+1:a]
    summ = 0
    for i in bb:
        summ += i
    print(f'Сумма {summ}')
