import sys
num = int(input('Введите натуральное трёхзначное число: '))
a = num // 100
b = num % 100 // 10
c = num % 10
print(f'Сумма = {a + b + c}')
print(f'Произведение = {a * b * c}')
print(f'Выделенно памяти под переменные {sys.getsizeof(num) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)} байт')
