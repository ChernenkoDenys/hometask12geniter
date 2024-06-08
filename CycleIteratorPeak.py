# Додайте до попереднього ітератора CycleIterator метод peek, 
# який буде підглядувати та повертати наступне значення, але не переходити на наступну ітерацію. 
# Наприклад ітератор вже повернув a, b наступний елемент - c, якщо я викличу peek він його поверне, 
# а якщо я викличу next() або в циклі наступну ітерацію викличу він повинен все одно повернути c



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
    
    def peak(self):
        if self.index == len(self.elements):
            return self.elements[0]
        return self.elements[self.index]    
        
        
cycle_iter = CyclicIterator([1, 2, 3])
print(next(cycle_iter))
print(cycle_iter.peak())
print(next(cycle_iter))
print(next(cycle_iter))
print(cycle_iter.peak())

