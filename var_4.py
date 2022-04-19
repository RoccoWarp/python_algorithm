import sys
num = input('Введите число целое трехзначное число ')
summary = 0
mult = 1
for i in num:
    summary += int(i)
    mult *= int(i)
print(f'Сумма = {summary}')
print(f'Произведение = {mult}')
print(f'Выделенно памяти под переменные {sys.getsizeof(num) + sys.getsizeof(summary) + sys.getsizeof(mult)} байт')
