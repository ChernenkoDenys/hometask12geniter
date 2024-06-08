# Напишіть функцію-генератор перестановок, 
# яка отримує список елементів 
# і видає усі можливі перестановки цих елементів.
from math import factorial



def permutations(list_elements: list):
    if len(list_elements) <= 1:
            yield list_elements
            
        

for i in permutations([1, 2, 3]):
 print(i)