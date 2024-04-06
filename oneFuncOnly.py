#Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных
class Animal: # в этом коде только звуки
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
 # (например, различный звук для `make_sound()`).
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "чирик-чирик"
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "рёв"

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "пшш"

#3. продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

#Создайте классы для сотрудников, например,
# `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Работник зоопарка кормит {animal.name}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветелинар лечит {animal.name}")

bird = Bird("Голубь", 4, 60)
mammal = Mammal("Тигр", 8, 'оранжевый окрас')
reptile = Reptile("Змея", 1, 'зеленая чешуя')

zoo_keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)


