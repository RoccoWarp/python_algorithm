import random
SIZE = 10
MIN_NUM = -100
MAX_NUM = 100
array = [random.randrange(MIN_NUM, MAX_NUM) for i in range(SIZE)]
print(array)


# def bubble_sort(our_array):
#     for i in range(len(our_array)):
#         for j in range(len(our_array) - 1):
#             if our_array[j] > our_array[j + 1]:
#                 our_array[j], our_array[j + 1] = our_array[j + 1], our_array[j]
#     return our_array
#
#
# print(bubble_sort(array))
def rev_sort(my_array, reverse=False):
    sign = int(reverse) * 2 - 1
    # n = 1
    # while n < len(array):
    for i in range(len(my_array)):
        for j in range(len(my_array) - 1):
            if my_array[j] * sign < my_array[j + 1] * sign:
            # if my_array[j] > my_array[j + 1]:
                my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
                # is_sorted = False
        # if is_sorted:
        #     break
        # n += 1
    return array


print(rev_sort(array, reverse=True))
