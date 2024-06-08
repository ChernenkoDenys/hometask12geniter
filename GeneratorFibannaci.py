# Напишіть генератор Фібоначчі, який видає числа у послідовності Фібоначчі


def fibonacci(number: int):
    i = 0
    previous = 0
    previous_second = 0
    while i <= number:
        if i == 0:
            yield 0
            i += 1
            
        elif i == 1:
            previous_second = 1
            yield 1
            i += 1
            
        else:
            res = previous_second + previous
            previous = previous_second
            previous_second = res
            yield res
            i += 1

            


for i in fibonacci(15):
 print(i)