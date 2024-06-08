# Напишіть ітератор CyclicIterator, 
# який бере довільний ітерабельний об'єкт і циклічно перебирає його до нескінченності. 
# Наприклад [”a”, “b”, “c”] → a, b, c, a, b, c, a, b…..


class CyclicIterator:
    
    def __init__(self, elements):
        self.elements = elements
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self): 
        while True:
            if self.index == len(self.elements):
                self.index = 0

            result = self.elements[self.index]
            self.index += 1
            return result        
        
for i in CyclicIterator([1, 2, 3]):
    print(i)