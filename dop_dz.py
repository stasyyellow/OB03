import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan #размах крыла wingspan

    def make_sound(self):
        return "чирик-чирик"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color #цвет шерсти

    def make_sound(self):
        return "рёв"


class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color # цвет чешуи

    def make_sound(self):
        return "пшш"


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Работник зоопарка кормит {animal.name}")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def animal_sound(self):
        for animal in self.animals:
            print(animal.make_sound())

    def info(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            if isinstance(animal, Bird):
                unique_feature = f"Размах крыльев: {animal.wingspan}"
            elif isinstance(animal, Mammal):
                unique_feature = f"Окрас: {animal.fur_color}"
            elif isinstance(animal, Reptile):
                unique_feature = f"Чешуя: {animal.scale_color}"
            else:
                unique_feature = "Неизвестная особенность"
            print(f"Имя: {animal.name}, Возраст: {animal.age}, {unique_feature}")
            print(f"Голоса: {animal.make_sound()}")
            print()

        print("Сотрудники зоопарка:")
        for staff_member in self.staff:
            if isinstance(staff_member, ZooKeeper):
                print("Смотритель зоопарка")
            elif isinstance(staff_member, Veterinarian):
                print("Ветеринар")
            else:
                print("Неизвестный сотрудник")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.animals, self.staff), file)

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.animals, self.staff = pickle.load(file)


bird = Bird("Голубь", 4, "60")
mammal = Mammal("Тигр", 8, 'оранжевый')
reptile = Reptile("Змея", 1, 'зеленая')

zoo_keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

# Сохранение данных в файл
zoo.save_to_file("zoo_data.pkl")

# Загрузка данных из файла
zoo.load_from_file("zoo_data.pkl")

# Вывод информации о зоопарке после загрузки
print("После загрузки из файла:")
zoo.animal_sound()
print()
zoo.info()



# #Библиотека pickle в Python предоставляет возможность сериализации и десериализации объектов Python. Сериализация - это процесс преобразования объектов Python в поток байтов, который затем можно сохранить в файл или передать по сети. Десериализация - это процесс восстановления объектов Python из потока байтов.
#
# В случае кода, который я предоставил выше,
# библиотека pickle используется для сохранения данных о зоопарке (списка животных и сотрудников) в файл
# и их последующей загрузки из файла. Вот как это работает в контексте кода:
#
# Сохранение данных в файл:
#
# Метод save_to_file объекта zoo принимает имя файла в качестве аргумента.
# Внутри метода save_to_file используется функция pickle.dump(),
# которая преобразует данные о зоопарке в поток байтов и записывает его в указанный файл.

# Загрузка данных из файла:
#
# Метод load_from_file объекта zoo также принимает имя файла в качестве аргумента.
# Внутри метода load_from_file используется функция pickle.load(), которая читает данные из файла
# и преобразует их обратно в объекты Python (список животных и сотрудников).
# Таким образом, библиотека pickle обеспечивает простой способ сохранения и загрузки объектов Python
# из файлов, что делает её полезным инструментом для работы с данными в Python. Однако следует помнить,
# что использование pickle может быть небезопасным, если данные, которые вы загружаете, не являются доверенными.