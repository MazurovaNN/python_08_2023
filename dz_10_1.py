# Введите ваше решение ниже
class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth
    
    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif not 10 < self.max_depth < 50:
            return 'Средневодная рыба'
        else:
            return 'Глубоководная рыба'

class Mammal(Animal):
    def __init__(self, name, weight ):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.name == 'Error':
            return ''
        if self.weight < 1:
            return 'Малявка'
        elif 1 > self.weight < 200:
            return 'Обычный'
        else:
            return 'Гигант'
        
class AnimalFactory:
    def create_animal(animal_type , *args):
        if animal_type ==  'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else: return Mammal('Error', 'Error')

animal2 = AnimalFactory.create_animal('Fish', 'Salmon', 50)
print(animal2.depth())