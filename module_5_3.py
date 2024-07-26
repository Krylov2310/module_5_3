print('Домашняя работа по уроку "Перегрузка операторов."')
print('Задача "Нужно больше этажей":')
print('Студент Крылов Эдуард Васильевич')
thanks = 'Благодарю за внимание :-)'
print()


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self


# Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'h1 = {h1}')
print(f'h2 = {h2}')
print(f'__eq__ h1 == h2 = {h1 == h2}') # __eq__

h1 = h1 + 10 # __add__
print(f'__add__ h1 = h1 + 10 = {h1}')
print(f'__eq__ h1 == h2 = {h1 == h2}')

h1 += 10 # __iadd__
print(f'__iadd__ h1 += 10 = {h1}')

h2 = 10 + h2 # __radd__
print(f'__radd__ h2 = 10 + h2 = {h2}')

print(f'__gt__ h1 > h2: {h1 > h2}') # __gt__
print(f'__ge__ h1 >= h2: {h1 >= h2}') # __ge__
print(f'__lt__ h1 < h2: {h1 < h2}') # __lt__
print(f'__le__ h1 <= h2: {h1 <= h2}') # __le__
print(f'__ne__ h1 != h2: {h1 != h2}') # __ne__
print()
print(thanks)