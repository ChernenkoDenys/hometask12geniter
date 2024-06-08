# Напишіть функцію-генератор з назвою count_down, 
# яка отримує число і повертає зворотній відлік від цього числа до 0.


def count_down(num: int):
    while num >= 0:
        yield num
        num -= 1


for i in count_down(10):
    print(i)
