import random
SIZE = 10
MIN_NUM = 0
MAX_NUM = 100
array = [random.randint(MIN_NUM, MAX_NUM) for i in range(SIZE)]
print(array)
array_index = []
for i in array:
    if i % 2 == 0:
        array_index.append(array.index(i))
print(array_index)
