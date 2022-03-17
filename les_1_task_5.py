first_letter = ord(input('Первая буква '))
second_letter = ord(input('Вторая буква '))
first_letter = first_letter - ord('a') + 1
second_letter = second_letter - ord('a') + 1
letters_between = second_letter - first_letter
print(first_letter)
print(second_letter)
print(letters_between)
