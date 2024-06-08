# Створіть ітератор, який буде фільтрувати значення. Ітератор приймає ітеровану послідовність та функцію. 
# Якщо функція на елементі поверне True то ми повертаємо цей елемент. 
# Важливо, працювати з цим ітератором за допомогою циклу while проходячись по ньому за допомогою методів ітератора.


class FilterIterator:
    
    def __init__(self, elements, func):
        self.elements = elements
        self.func = func
        self.index = 0
            
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.elements):
            raise StopIteration
        
        if self.func(self.elements[self.index]):
            print(self.elements[self.index])
            self.index += 1
        else:
            self.index += 1
        

f_iter = FilterIterator([1, 2, 3, 4], lambda x: x % 2 == 0)
while True:
    try:
        next(f_iter)
    except StopIteration as e:
        break
