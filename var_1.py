import sys
num = input('Введите число целое трехзначное число ')
# print(sys.getsizeof(num))
a = num[0]
b = num[1]
c = num[2]
# print(sys.getsizeof(a)+sys.getsizeof(b)+sys.getsizeof(c))
a = int(a)
b = int(b)
c = int(c)
# print(sys.getsizeof(a)+sys.getsizeof(b)+sys.getsizeof(c))
print(f'Сумма = {a + b + c}')
print(f'Произведение = {a * b * c}')
print(f'Выделенно памяти под переменные {sys.getsizeof(num)+sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)} байт')
