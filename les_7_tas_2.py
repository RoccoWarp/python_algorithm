import random


def m_sort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        array[0], array[1] = array[1], array[0]
        return array

    left = m_sort(array[:len(array) // 2])
    right = m_sort(array[len(array) // 2:])

    i = j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1

    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


SIZE = 10
LIMIT = 50
data = [random.uniform(0, LIMIT) for _ in range(SIZE)]
print(data)
m_sort(data)
print(data)
