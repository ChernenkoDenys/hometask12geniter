# Напишіть функцію-генератор перестановок, 
# яка отримує список елементів 
# і видає усі можливі перестановки цих елементів.


def permutations(lst):
    c = [0] * len(lst)
    yield lst[:]
    
    i = 0
    while i < len(lst):
        if c[i] < i:
            if i % 2 == 0:
                lst[0], lst[i] = lst[i], lst[0]
            else:
                lst[c[i]], lst[i] = lst[i], lst[c[i]]
            yield lst[:]
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1



    
            
for i in permutations([1, 2, 3]):
    print(i)