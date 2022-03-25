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

# print(min_num)
# print(max_num)
min_nun_index = array.index(min_num)
max_num_index = array.index(max_num)
array[min_nun_index], array[max_num_index] = array[max_num_index], array[min_nun_index]
print(array)
