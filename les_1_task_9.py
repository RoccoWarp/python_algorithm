a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
