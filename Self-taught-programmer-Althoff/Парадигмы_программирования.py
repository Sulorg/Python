#Примеры
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Создано!")
        
or1 = Orange(10, "темный апельсин")
or1.weight = 100
or1.color = "светлый апельсин"
print(or1)
print(or1.weight)
print(or1.color)

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Создано!")

or1 = Orange(4,"Светлый апельсин")
or2 = Orange(8, "Темный апельсин")
or3 = Orange(14, "Желтый апельсин")

class Orange():
    def __init__(self, w, c):
       """Вес в граммах"""
       self.weight = w
       self.color = c
       self.mold = 0
       print ("Создано!")

    def rot(self, days, temp):
        self.mold = days * temp
orange = Orange(6, "апельсин")
print(orange.mold)
orange.rot(10,33)
print(orange.mold)

#Прямоугольник
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = 1

    def area(self):
        return self.width * self.len
    def change_size(self, w, l):
        self.width = w
        self.len = 1
rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())



